from fastapi import FastAPI
from routers.transcribe import router

app = FastAPI()
app.include_router(router)

@app.get("/test")
def read_root():
    return 1111
