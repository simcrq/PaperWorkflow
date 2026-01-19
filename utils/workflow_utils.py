from loguru import logger
import os

def find_pdf_files(root_dir):
    """
    遍历目录查找所有 PDF 文件
    返回列表: [{'id': '4586', 'path': '...'}]
    """
    pdf_list = []
    
    # 假设结构是 root_dir/ID/*.pdf
    for item in os.listdir(root_dir):
        sub_path = os.path.join(root_dir, item).replace('\\', '/')
        if os.path.isdir(sub_path): # 4586, 4587...
            # 在子文件夹中找 pdf
            for file in os.listdir(sub_path):
                if file.endswith('.pdf'):
                    pdf_list.append({
                        'id': item, # 文件夹名作为 ID
                        'folder_path': sub_path,
                        'file_path': os.path.join(sub_path, file).replace('\\', '/'),
                        'file_name': file
                    })
                    continue # 每个 ID 文件夹只处理一个 PDF？假设是这样
    
    return pdf_list

def determine_mode(paper_id, rules_config):
    """
    根据 ID 和配置判断阅读模式
    """
    # 强制转字符串比较
    paper_id = str(paper_id)
    
    if 'deep_read_ids' in rules_config and paper_id in rules_config['deep_read_ids']:
        return 'deep_read'
    
    if 'skim_ids' in rules_config and paper_id in rules_config['skim_ids']:
        return 'skim'
        
    return rules_config.get('default_mode', 'skim')
