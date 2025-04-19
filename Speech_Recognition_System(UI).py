import gradio as gr
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
model.eval()

def transcribe_audio(audio_tensor):
    sample_rate, data = audio_tensor
    audio_tensor = torch.tensor(data)
    audio_tensor = audio_tensor.to(torch.float32)
    if len(audio_tensor.shape) > 1:
        audio_tensor = audio_tensor.mean(dim=0, keepdim=True)
    if audio_tensor.shape[0] < 16000:
        return "Audio too short. Please upload at least 1 second of audio."
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        audio_tensor = resampler(audio_tensor)
        sample_rate=16000
    input_values = processor(audio_tensor.squeeze().numpy(), sampling_rate=16000, return_tensors="pt", padding=True).input_values
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    return transcription

gr.Interface(fn=transcribe_audio, inputs="audio", outputs="text").launch(share=True, debug=True)

