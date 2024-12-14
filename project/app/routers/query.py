# app/routers/query.py
from fastapi import APIRouter, HTTPException
from app.models import QueryRequest, QueryResponse
from app.utils.data_store import get_extracted_content
from app.utils.llm_client import query_llm

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_content(payload: QueryRequest):
    file_id = payload.file_id
    content = get_extracted_content(file_id)
    if not content:
        raise HTTPException(status_code=404, detail="Processed content not found")

    # Combine extracted text for the prompt
    text_snippet = "\n".join(content["text"][:50])  # First 10 paragraphs
    prompt = f"""
    You are an intelligent assistant. Analyze the following text and answer the user's query.

    Text:
    {text_snippet}

    Query:
    {payload.query}
    """
    llm_response = query_llm(prompt)
    return QueryResponse(query=payload.query, response={"summary": llm_response})
