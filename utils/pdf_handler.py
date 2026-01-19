import os
from loguru import logger
from .pdf_local_handler import LocalPDFProcessor
from .pdf_api_handler import ApiPDFProcessor

class PDFProcessor:
    def __init__(self, config):
        self.config = config
        self.temp_dir = config['paths']['temp_dir']
        self.mode = config['api']['mineru']['mode']
        
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
            
        if self.mode == 'local_cli':
            self.processor = LocalPDFProcessor(config)
        elif self.mode == 'api':
            self.processor = ApiPDFProcessor(config)
        else:
            raise ValueError(f"Unknown PDF processing mode: {self.mode}")

    def convert_to_markdown(self, pdf_path):
        """
        将 PDF 转换为 Markdown
        返回转换后的 Markdown 内容字符串
        """
        file_name = os.path.basename(pdf_path).replace('.pdf', '')

        # 确保 temp_dir 是绝对路径
        abs_temp_dir = os.path.abspath(self.temp_dir).replace('\\', '/')
        
        # MinerU (无论是 local 还是 api 模式，我们都约定输出到 file_name 子目录)
        output_path = os.path.join(abs_temp_dir, file_name)
        
        # 1. 检查缓存
        cached_content = self._check_cache(output_path, file_name)
        if cached_content:
            return cached_content

        logger.info(f"Converting PDF: {file_name} using {self.mode}")

        try:
            # 2. 执行转换
            # 传入 abs_temp_dir 作为根目录，处理器内部会处理到 file_name 子目录
            self.processor.process(pdf_path, abs_temp_dir)
            
            # 3. 读取结果
            return self._read_result(output_path, file_name)

        except Exception as e:
            logger.error(f"Error processing PDF {pdf_path}: {str(e)}")
            raise e
            
    def _check_cache(self, output_path, file_name):
        possible_paths = [
            os.path.join(output_path, f"{file_name}.md"),
            os.path.join(output_path, "auto", f"{file_name}.md"),
            os.path.join(output_path, "hybrid_auto", f"{file_name}.md"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                logger.info(f"Using cached markdown for {file_name} from {path}")
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
        return None
        
    def _read_result(self, output_path, file_name):
        # 尝试在可能的子目录中查找生成的 Markdown 文件
        possible_paths = [
            os.path.join(output_path, f"{file_name}.md"),
            os.path.join(output_path, "auto", f"{file_name}.md"),
            os.path.join(output_path, "hybrid_auto", f"{file_name}.md"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                logger.info(f"Found markdown file at: {path}")
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()

        # 如果预定义路径都没找到，尝试遍历查找
        logger.warning(f"Markdown file not found in common paths, checking subfolders of {output_path}...")
        for root, dirs, files in os.walk(output_path):
            for file in files:
                # 优先匹配同名 md 文件
                if file == f"{file_name}.md":
                    found_path = os.path.join(root, file)
                    logger.info(f"Found markdown file at: {found_path}")
                    with open(found_path, 'r', encoding='utf-8') as f:
                        return f.read()
        
        # 如果还找不到，尝试找任意 md 文件
        for root, dirs, files in os.walk(output_path):
            for file in files:
                if file.endswith(".md"):
                    found_path = os.path.join(root, file)
                    logger.info(f"Found markdown file (fallback) at: {found_path}")
                    with open(found_path, 'r', encoding='utf-8') as f:
                        return f.read()
            
        raise FileNotFoundError(f"Converted Markdown file not found in {output_path}")


