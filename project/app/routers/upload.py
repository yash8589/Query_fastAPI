# app/routers/upload.py
from fastapi import APIRouter, UploadFile, File
from app.models import FileUploadResponse
from app.utils.file_handler import save_file
import os

router = APIRouter()


@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    file_path = save_file(file)
    filename = os.path.basename(file_path)  # Extracts the filename correctly
    file_id = filename.split("_")[0]  # Now split by underscore to get the UUID file_id
    return FileUploadResponse(file_id=file_id, status="uploaded")
