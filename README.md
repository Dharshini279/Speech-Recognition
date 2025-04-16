# Speech Recognition System

This project is a **Speech Recognition System** built using **Hugging Face's Wav2Vec2 model**. It's designed to convert spoken words into text, offering two different ways to interact with it:

1. **Console Mode**: You can process audio files from your computer, including those that were uploaded via Google Colab, and transcribe them into text.
2. **Gradio UI**: This provides an easy-to-use interface where you can record audio using your microphone and see the transcription in real-time.

## Features
- **Speech-to-Text Conversion**: The system uses the Wav2Vec2 model to convert speech into written text accurately.
- **Two Modes**:
  - **Console Mode**: This allows you to upload audio files from your computer and have them transcribed.
  - **Gradio UI**: You can record your voice through the browser and get the transcription instantly.
- **Pre-processing**: Before transcription, the audio is prepared and formatted to make sure it’s ready for the Wav2Vec2 model to process.
- **Real-time Transcription**: When using Gradio, the system listens to you as you speak and gives you transcriptions in real time.

## How It Works

### 1. Console Mode
In **Console Mode**, you can upload pre-recorded audio files (which may have been uploaded from Google Colab). The system processes the audio, converts it into the right format, and then feeds it into the Wav2Vec2 model to get a transcription.

### 2. Gradio UI
The **Gradio UI** provides a simple web interface that makes it easy to interact with the system. Here's what you can do:
- **Record Audio** using your microphone.
- **Get Real-time Transcription** as you speak.
- **Upload Audio Files** for transcription.

The Gradio interface connects directly to the Wav2Vec2 model, allowing you to transcribe speech into text quickly and easily.

---

## Key Technologies Used
- **Wav2Vec2 (Hugging Face)**: This advanced speech-to-text model is used for high-quality transcription.
- **Gradio**: This library lets you build user-friendly interfaces for machine learning models without much hassle.
- **Google Colab**: Colab is used to handle and upload audio files that will be processed by the system.

---

## How the Model Works
1. **Audio Preprocessing**: First, the audio data is processed to make sure it's in the right format (correct sample rate, mono-channel, etc.).
2. **Console Mode**: Users upload pre-recorded audio files, and the system transcribes them using the Wav2Vec2 model.
3. **Gradio Mode**: Users can record audio in real time using their microphone. The audio is processed and transcribed on the spot.
4. The Wav2Vec2 model then generates **logits output**, and the system decodes this into the final transcription.

---

## Summary
- **Console Mode** is designed to process and transcribe audio files that you upload from your computer or Google Colab.
- **Gradio UI** allows you to interact directly with the system by recording your voice and getting transcriptions instantly.
- This project offers a flexible and intuitive way to convert speech into text, either through pre-recorded files or live audio.

---
