# app/utils/text_extractor.py
import pdfplumber
import os
from typing import List


def extract_text_and_tables(file_path: str):
    extracted_text = []
    extracted_tables = []

    # Check file extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                # Extract text
                text = page.extract_text()
                if text:
                    # Split into paragraphs if needed
                    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
                    extracted_text.extend(paragraphs)

                # Extract tables
                tables = page.extract_tables()
                if tables:
                    for table in tables:
                        extracted_tables.append(table)
    elif ext in [".txt"]:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            paragraphs = [p.strip() for p in content.split("\n") if p.strip()]
            extracted_text.extend(paragraphs)
        # No tables expected in .txt by default, unless you parse
    else:
        # TODO: Implement OCR here if scanned PDF
        pass

    return extracted_text, extracted_tables
