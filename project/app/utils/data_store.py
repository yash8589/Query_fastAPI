# app/utils/data_store.py
from typing import Dict, Any

DATA_STORE: Dict[str, Dict[str, Any]] = {}


def store_extracted_content(file_id: str, text: list, tables: list):
    DATA_STORE[file_id] = {"text": text, "tables": tables}


def get_extracted_content(file_id: str):
    return DATA_STORE.get(file_id, None)
