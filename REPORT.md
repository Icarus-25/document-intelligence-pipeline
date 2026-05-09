# Document Intelligence Pipeline Report

## Tool/Library Evaluation

**Choice: Docling (IBM)**

I selected Docling as the core document conversion engine for its broad format support which includes PDF and DOCX. Docling uses advanced layout detection and table structure analysis, making it well-suited for converting complex documents into clean, readable Markdown.

**Strengths:**
- Supports multiple input formats with a unified API
- Intelligent table structure detection via TableFormer models
- Built-in OCR support for scanned PDFs
- Converts directly to structured Markdown, avoiding intermediate JSON processing
- Active development and good community documentation

**Limitations:**
- OCR on large scanned PDFs is memory-intensive and slower
- Complex multi-column layouts sometimes have imperfect reading order
- Embedded images are extracted as descriptions only, not saved as separate files
- Requires significant model downloads on first use (HuggingFace dependencies)

## Failure Modes

**1. Scanned/Image-Based PDFs:**
Text-based PDFs parse cleanly, but scanned documents (where text is part of an image) require OCR. Docling's RapidOCR engine handles this automatically, but extraction quality degrades on heavily compressed or low-resolution scans. We accepted this limitation because true OCR improvement would require user-supplied configuration.

**2. Complex Page Layouts:**
Documents with multiple columns, text boxes, or floating elements sometimes have messy reading order in the output. The layout model does its best, but Markdown's linear structure cannot fully capture 2D spatial relationships. We mitigated this by keeping error handling clear—failed conversions write error files rather than silently failing.

## Real-World Applications

1. **Legal/Compliance Document Processing:** Convert contract PDFs and policies to searchable, versioned Markdown for Git repositories and compliance audits.

2. **Research Paper Digitization:** Transform scanned academic papers and reports into clean text documents for archival systems or LLM training datasets.

3. **Content Management Workflows:** Batch-convert Word documents and PDFs into Markdown for static site generators, enabling content teams to work in version control.

## Design Decision: Markdown-Only Output

We chose to export only Markdown files rather than both Markdown and JSON. This decision prioritizes **simplicity and usability**:

- **Readability:** Markdown is human-readable out of the box; JSON requires parsing
- **Storage:** Single `.md` file per document is simpler than managing `.md` + `.json` pairs
- **Maintenance:** Reducing output types reduces code complexity and testing burden
- **Portability:** Markdown works with any text editor and version control system

For users needing structured data, they can still parse the Markdown programmatically or request the feature. This reflects a philosophy of "do one thing well" over feature bloat.

---

**Conclusion:** Docling provides a robust foundation for document conversion. While limitations exist around scanned PDFs and complex layouts, the pipeline handles typical real-world documents well and offers clear, maintainable code for future improvements.
