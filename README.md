# Document Intelligence Pipeline

Converts real-world PDFs/DOCX into structured Markdown using **Docling** (IBM).

## Features
- Processes multiple document formats
- Extracts headers, lists, tables, code blocks, images (with descriptions)
- Graceful error handling
- Outputs saved to `/outputs/`

## Quick Start
```bash
pip install -r requirements.txt
python pipeline.py
```