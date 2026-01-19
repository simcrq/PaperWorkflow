import re

class PromptBuilder:
    @staticmethod
    def build_summary_prompt(markdown_content, mode='skim', remove_refs=True):
        """
        构建 XML 格式的 Prompt
        mode: 'skim' (浏览) 或 'deep_read' (精读)
        remove_refs: 是否去除参考文献
        """
        
        # 预处理：去除参考文献
        if remove_refs:
            content_clean = PromptBuilder.remove_references(markdown_content)
            print("References 已清除")
        else:
            content_clean = markdown_content
            print("References 保留")
        
        instruction = ""
        if mode == 'deep_read':
            instruction = """
作为该领域的研究专家，请仔细阅读以下论文内容。
请生成一份详细的总结报告，包含以下部分：
1. **核心发现**：论文解决了什么问题？发现了什么新现象？
2. **技术细节**：具体使用了什么方法（如 DFT 参数、泛函、计算设置）？关键公式或推导是什么？
3. **数据结果**：主要的实验或计算数据是什么？
4. **结论与意义**：这项工作对领域有什么贡献？
请注意：保留关键的数据指标和专业术语。
"""
        else: # skim
            instruction = """
作为研究助理，请快速浏览以下论文。
请生成一份简短的摘要，包含：
1. **研究目的**：这篇论文想干什么？
2. **主要结论**：他们得出了什么结论？
3. **核心方法**：用了一两句话概括方法。
"""

        prompt = f"""
<instruction>
{instruction}
</instruction>

<paper_content>
{content_clean[:30000]} 
</paper_content> 
"""
        # 注意：这里做了简单的长度截断 [:30000] 防止 token 溢出，根据模型能力调整
        return prompt

    @staticmethod
    def remove_references(text):
        """
        简单去除参考文献部分
        """
        # 匹配常见的参考文献标题，不区分大小写
        patterns = [
            r"##\s*References",
            r"##\s*参考文献",
            r"#\s*References",
            r"###\s*References"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return text[:match.start()]
        
        return text
