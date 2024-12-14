# app/main.py
from fastapi import FastAPI
from app.routers import upload, process, query, visualize

app = FastAPI(
    title="File Processing and Query System",
    description="Upload files, extract content, and query with LLM",
)

app.include_router(upload.router)
app.include_router(process.router)
app.include_router(query.router)
app.include_router(visualize.router)
