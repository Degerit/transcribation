from fastapi import APIRouter
from services.CServiceModels import WisperService

router = APIRouter(
    prefix = "/function",
    tags = ["models"],
    responses = {404 : {"description" : "Not found"}}
)

@router.get("/transcribe")
async def transcribation():
    service = WisperService()
    result = service.transcribe("./files/test.wav")
    return {"text" : result}
