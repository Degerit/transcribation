from fastapi import APIRouter
from services.wisperService import wisperService

router = APIRouter(
    prefix = "/api",
    tags = ["models"],
    responses = {404 : {"description" : "Not found"}}
)

@router.get("/transcribe/{file_path:path}")
async def transcribation(file_path : str):
    service = wisperService()
    result = service.transcribe(f"../files/{file_path}")
    return {"text" : result}
