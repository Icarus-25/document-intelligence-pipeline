import logging
from pathlib import Path

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_document(input_path: str | Path, output_dir: Path = Path("outputs")):
    input_path = Path(input_path)
    output_dir.mkdir(exist_ok=True)
    
    try:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_table_structure = True

        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options
                )
            }
        )
        
        logger.info(f"Processing: {input_path.name}")
        result = converter.convert(str(input_path))
        
        md_content = result.document.export_to_markdown()
        
        base_name = input_path.stem
        
        (output_dir / f"{base_name}.md").write_text(md_content, encoding="utf-8")
        
        logger.info(f"✅ Successfully processed {input_path.name}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to process {input_path.name}: {e}")
        error_path = output_dir / f"{input_path.stem}_ERROR.md"
        error_path.write_text(f"# Error Processing {input_path.name}\n\nError: {str(e)}", encoding="utf-8")
        return False


def main():
    documents = [
        "docs/Test_Doc_1.pdf",
        "docs/Test_Doc_2.docx",
        "docs/Test_Doc_3.pdf",
    ]
    
    success = 0
    for doc in documents:
        if Path(doc).exists():
            if process_document(doc):
                success += 1
        else:
            logger.warning(f"⚠️ File not found: {doc}")
    
    logger.info(f"Pipeline finished. Successfully processed {success}/{len(documents)} documents.")

if __name__ == "__main__":
    main()