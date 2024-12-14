# app/routers/process.py
from fastapi import APIRouter, HTTPException
from app.models import ProcessRequest, ProcessResponse
from app.utils.text_extractor import extract_text_and_tables
from app.utils.data_store import store_extracted_content
import os

router = APIRouter()


@router.post("/process", response_model=ProcessResponse)
async def process_file(payload: ProcessRequest):
    file_id = payload.file_id
    # Find the file by file_id in upload folder
    from app.utils.file_handler import UPLOAD_FOLDER

    file_path = None
    for fname in os.listdir(UPLOAD_FOLDER):
        if fname.startswith(file_id):
            file_path = os.path.join(UPLOAD_FOLDER, fname)
            break

    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")

    extracted_text, extracted_tables = extract_text_and_tables(file_path)
    store_extracted_content(file_id, extracted_text, extracted_tables)
    return ProcessResponse(
        file_id=file_id,
        extracted_text=extracted_text,
        extracted_tables=extracted_tables,
    )
