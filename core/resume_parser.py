import fitz

def extract_resume_text(file_path):
    """Extract text from a PDF resume."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
