# app/routers/visualize.py
from fastapi import APIRouter, HTTPException
from app.models import ProcessRequest
from app.utils.data_store import get_extracted_content

router = APIRouter()


@router.get("/visualize/{file_id}")
async def visualize_content(file_id: str):
    content = get_extracted_content(file_id)
    if not content:
        raise HTTPException(status_code=404, detail="No content found")
    return content
