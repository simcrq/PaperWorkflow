import os
import subprocess
from loguru import logger

class LocalPDFProcessor:
    def __init__(self, config):
        self.config = config

    def process(self, pdf_path, output_dir):
        """
        使用本地 MinerU CLI转换
        pdf_path: PDF文件绝对路径
        output_dir: 输出的根目录 (MinerU会在这个目录下创建以文件名命名的子目录)
        """
        # 确保 output_dir 是绝对路径
        abs_output_dir = os.path.abspath(output_dir).replace('\\', '/')
        
        # 这里的命令参数可能需要根据实际 config 调整，目前按照原代码硬编码
        # 如果 config 中有更多配置，可以在这里读取
        cmd = [
            "mineru", 
            "-p", pdf_path, 
            "-o", abs_output_dir,
            "-b", "hybrid-http-client",
            "-u", "http://127.0.0.1:30000"
        ]
        logger.info(f"Running command: {' '.join(cmd)}")
        
        # Windows 下命令行输出可能为 GBK，使用 errors='replace' 防止报错
        result = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
        
        if result.returncode != 0:
            logger.error(f"MinerU conversion failed: {result.stderr}")
            logger.error(f"MinerU stdout: {result.stdout}") # 记录 stdout 辅助排查
            raise Exception(f"Conversion failed for {pdf_path}")
        else:
            logger.debug(f"MinerU Output: {result.stdout}")
            if result.stderr:
                 logger.warning(f"MinerU Stderr: {result.stderr}")
