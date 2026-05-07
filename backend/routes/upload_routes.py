from fastapi import APIRouter, UploadFile, File
import shutil
import os
from backend.rag.chunker import split_text
from backend.rag.embeddings import generate_embeddings
from backend.rag.vectordb import store_chunks

from backend.services.pdf_service import extract_text_from_pdf

router = APIRouter()

UPLOAD_FOLDER = "uploads"

@router.post("/upload")

async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    chunks = split_text(extracted_text)

    embeddings = generate_embeddings(chunks)

    store_chunks(chunks, embeddings)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text[:3000]
    }