from fastapi import APIRouter, UploadFile, File
from servises.CServiseModels import WisperServise

router = APIRouter(
    prefix = "/function",
    tags = ["models"],
    responses = {404 : {"description" : "Not found"}}
)

@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size  # в байтах
    }

@router.get("/transcribe")
async def transcribation():
    servise = WisperServise()
    result = servise.transcribe("../files/test.wav")
    return {"text" : result}