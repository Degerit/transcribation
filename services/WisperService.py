import torch
import whisper
import librosa

class WisperService:
    def transcribeeee(self, name):
        self.name = name
        audio, sr = librosa.load(self.name, sr=16000)
        model = whisper.load_model("tiny").to("cuda")
        result = model.transcribe(audio, language="ru", fp16= torch.cuda.is_available())
        return result["text"]
