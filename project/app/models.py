# app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class FileUploadResponse(BaseModel):
    file_id: str
    status: str


class ProcessRequest(BaseModel):
    file_id: str


class ProcessResponse(BaseModel):
    file_id: str
    extracted_text: List[str]
    extracted_tables: List[
        List[List[str]]
    ]  # List of tables, each table is a list of rows, each row a list of cells


class QueryRequest(BaseModel):
    file_id: str
    query: str


class QueryResponse(BaseModel):
    query: str
    response: Dict[str, Any]
