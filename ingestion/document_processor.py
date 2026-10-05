from pathlib import Path

from ingestion.pdf_loader import load_pdf
from ingestion.docx_loader import load_docx
from ingestion.txt_loader import load_txt


def process_document(file_path):
    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".docx":
        return load_docx(file_path)

    elif extension == ".txt":
        return load_txt(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )