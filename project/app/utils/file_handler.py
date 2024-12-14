# app/utils/file_handler.py
import uuid
import os

UPLOAD_FOLDER = "uploaded_files"


def save_file(file) -> str:
    # file is a Starlette UploadFile
    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
