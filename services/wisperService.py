import torch
import whisper
import librosa

class wisperService:
    def __init__(self):
        self.model = whisper.load_model("tiny").to("cuda")

    def transcribe(self, name):
        self.name = name
        audio, sr = librosa.load(self.name, sr=16000)
        result = self.model.transcribe(audio, language= None, fp16= torch.cuda.is_available())
        return result["text"]
