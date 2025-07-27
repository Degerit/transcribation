from fastapi import APIRouter
from services.wisperService import WisperService
import os
router = APIRouter(
    prefix = "/function",
    tags = ["models"],
    responses = {404 : {"description" : "Not found"}}
)

@router.get("/transcribe/{file_path:path}")
async def transcribation(file_path : str):
    service = WisperService()
    result = service.transcribe(f"transcribation/files/{file_path}")
    return {"text" : result}
