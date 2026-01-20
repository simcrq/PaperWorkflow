import os
import yaml
import time
import sys
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
from tqdm import tqdm

from utils.pdf_handler import PDFProcessor
from utils.llm_handler import LLMHandler
from utils.prompt_builder import PromptBuilder
from utils.workflow_utils import find_pdf_files, determine_mode
from utils.md_merger import merge_markdown_files

logger.remove()
# 设置 level="INFO"，但要过滤更高级别
md_outputs = []

logger.add(
    sys.stderr,
    format= "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{message}</level>",
    filter=lambda r: r["level"].no in (20, 40),
    colorize=True
)


def load_config(config_path="config.yaml"):
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def process_single_paper(paper_info, config, pdf_processor, llm_handler):
    """
    处理单篇论文的完整流程
    """
    paper_id = paper_info['id']
    pdf_path = paper_info['file_path']
    folder_path = paper_info['folder_path']
    file_name = paper_info['file_name']
    
    # 1. 确定模式
    mode = determine_mode(paper_id, config['processing_rules'])
    logger.info(f"正在处理子目录 [{paper_id}] 下pdf, 处理模式: {mode}")
    
    output_filename = f"Summary_{mode}_{file_name.replace('.pdf', '')}.md"
    output_path = os.path.join(folder_path, output_filename) # 默认保存在同级目录
    
    # 检查是否已存在
    if os.path.exists(output_path):
        logger.warning(f"Output for {paper_id} already exists. Skipping.")
        return
    md_outputs.append(output_path)


    try:
        # 2. PDF -> Markdown
        start_time = time.time()
        md_content = pdf_processor.convert_to_markdown(pdf_path)
        logger.debug(f"[{paper_id}] PDF converted in {time.time() - start_time:.2f}s")
        
        # 3. Build Prompt
        # 获取配置
        remove_refs = config.get('processing_rules', {}).get('remove_references', True)
        prompt = PromptBuilder.build_summary_prompt(md_content, mode, remove_refs=remove_refs)
        
        # 4. LLM Extraction
        summary = llm_handler.summarize(prompt)
        
        # 5. Save Result
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Summary: {file_name}\n")
            f.write(f"- **ID**: {paper_id}\n")
            f.write(f"- **Mode**: {mode}\n")
            f.write(f"- **Date**: {time.strftime('%Y-%m-%d')}\n\n")
            f.write(summary)
            
        logger.success(f"[{paper_id}] Summary saved to {output_path}")

        
        
    except Exception as e:
        logger.error(f"[{paper_id}] Failed: {str(e)}")


def main():
    # Setup Logger
    logger.add("logs/workflow_{time}.log", rotation="500 MB")
    
    # Load Config
    if not os.path.exists("config.yaml"):
        logger.error("Config file not found!")
        return
    config = load_config()
    
    # Initialize Handlers
    try:
        pdf_processor = PDFProcessor(config)
        llm_handler = LLMHandler(config)
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return

    # Find Files
    input_dir = config['paths']['input_dir']
    if not os.path.exists(input_dir):
        logger.error(f"Input directory not found: {input_dir}")
        return
    papers = find_pdf_files(input_dir)
    # file_paths = [item['file_path'] for item in papers]
    # print(file_paths)
    # return
    logger.info(f"共找到 {len(papers)} 篇论文待处理。")
    logger.info(f"本项目已在github开源, 仓库地址:https://github.com/SimCr/PaperWorkflow")
    
    # Concurrent Processing
    max_workers = config['concurrency']['max_workers']
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用 list 强制执行，配合 tqdm 显示进度
        list(tqdm(executor.map(lambda p: process_single_paper(p, config, pdf_processor, llm_handler), papers), total=len(papers)))

    # Optional Post-Processing Steps
    # 1.合并所有Markdown文件
    if config.get('processing_rules', {}).get('is_merger_md', False):
        logger.info("正在合并所有Markdown文件...")
        merge_markdown_files(md_outputs, os.path.join(config['paths']['merge_output_dir'], f"Merged_Summaries+{time.strftime('%Y%m%d')}.md"))

if __name__ == "__main__":
    main()
