
## PaperWorkflow V0.1
基于 MinerU 和 OpenAI compatible API 的自动化论文阅读与总结工作流。

### 开始：
克隆本仓库到本地：
1.  **填写配置**：
*   具体配置说明见 `iconfig.yaml` 文档。
    *   将 `iconfig.yaml`复制为 `config.yaml`。
    *   打开 `config.yaml`。
    *   填入你的 MinerU 和 OpenAI (或中转) 的 `API Key`。
    *   **关键**：在 `processing_rules` 部分，把那些论文编号规则，填入 `deep_read_ids` （精读）和 `skim_ids` （浏览）列表中。注意这里的 ID 需要对应你的**文件夹名称**（如 `4586`）。

2.  **安装依赖**：
*   使用uv进行包管理。请打开命令行，进入该目录运行：
```shell
cd PaperWorkflow
uv sync
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3.  **运行程序**：
```shell
python main.py
```

### 代码功能亮点：
*   **分级阅读**：自动根据 ID 区分精读/浏览，发送不同的 Prompt。
*   **XML 包装**：应用 XML 格式包装正文内容和提示词，提高模型遵循度。
*   **并发加速**：使用多线程同时处理多篇 PDF，效率翻倍, 注意并发数不能太高。
*   **结果回填**：生成的总结会自动保存到原 PDF 所在的文件夹内，文件名如 `Summary_deep_read_PaperTitle.md`。
*   **自动跳过**：如果输出文件已存在，则跳过该论文处理，避免重复工作。

请先尝试配置并在小范围内测试（例如先只放一个 ID 在列表里）。


### 文件树
```shell
PaperWorkflow/
├── INput/                  # 输入文件夹，按任务 ID 存放 PDF
│   └── Task1/
│       ├── 111.pdf
│       └── 222.pdf
├── temp_markdowns/         # 转换过程中的临时 Markdown 或 API 结果
├── utils/
│   ├── __init__.py
│   ├── pdf_api_handler.py  # 处理 API 转换逻辑
│   ├── pdf_handler.py      # PDF 处理统一入口
│   ├── pdf_local_handler.py # 处理本地 CLI 转换逻辑
│   └── prompt_builder.py   # 构建 AI 提示词与预处理
├── config.yaml             # 配置文件（API Key、路径、阅读模式）
├── main.py                 # 程序主入口
├── pyproject.toml          # 项目依赖配置 (uv)
├── README.md               # 项目说明文档
└── uv.lock                 # 依赖锁定文件
```
### 致谢与开发声明
本项目为论文处理自动化工作流，开发与实现过程中使用Gemini3及Miner U在线API文档提供技术辅助，所有核心逻辑、流程设计及功能验证由本人完成。
#### API说明
1. 第三方API：[MinerU](https://github.com/opendatalab/mineru) 在线 API 用于 PDF 转换与文本提取
前往 https://mineru.net/apiManage/ 申请MinerU API key
2. OpenAI 兼容 API：可使用 OpenAI 官方 API 或其他兼容的中转服务。


Made changes.
---
contributed by : SimCr
