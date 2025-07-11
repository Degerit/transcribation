from fastapi import APIRouter
from servises.CServiseModels import WisperServise

router = APIRouter(
    prefix = "/function",
    tags = ["models"],
    responses = {404 : {"description" : "Not found"}}
)

@router.get("/transcribe")
async def transcribation():
    servise = WisperServise()
    result = servise.transcribe("./files/test.wav")
    return {"text" : result}
