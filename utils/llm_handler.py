from openai import OpenAI
from loguru import logger
import os

class LLMHandler:
    def __init__(self, config):
        self.config = config
        llm_conf = config['api']['llm']
        
        self.client = OpenAI(
            api_key=llm_conf['api_key'],
            base_url=llm_conf['base_url']
        )
        self.model = llm_conf['model_name']
        self.timeout = llm_conf.get('timeout', 120)

    def summarize(self, prompt_content):
        """
        调用 LLM 进行总结
        """
        try:
            logger.info(f"第2/2步:Sending request to LLM {self.model}...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant."},
                    {"role": "user", "content": prompt_content}
                ],
                timeout=self.timeout
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM request failed: {str(e)}")
            return f"Error generating summary: {str(e)}"
