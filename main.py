import torch
import whisper
import librosa

file_name = "test.wav"

class WisperServise:
    def transcribe(self, name):
        self.name = name
        audio, sr = librosa.load(self.name, sr=16000)
        model = whisper.load_model("tiny").to("cuda")
        result = model.transcribe(audio, language="ru", fp16= torch.cuda.is_available())
        return result["text"]

wisper_servise = WisperServise()
transcription = wisper_servise.transcribe(file_name)
print(transcription)
