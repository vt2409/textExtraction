# 🎙️ Audio to Text Conversion using Whisper

## 📌 Overview
This project extracts text from audio files using OpenAI's **Whisper** model. It enables automatic speech recognition (ASR) to transcribe spoken words into text efficiently.

## 🚨 Important Note
⚠ **Python 3.13 is not supported** due to compatibility issues with the `ctypes` library, which Whisper relies on for loading dependencies. It is recommended to use **Python 3.10 or 3.11** for stable execution.

## 🛠️ Requirements
- **OpenAI Whisper** (for transcription)
- **Python 3.10 or 3.11** (avoid 3.13 due to `ctypes` issues)

## 🚀 Features
✅ Converts speech to text with high accuracy  
✅ Supports multiple audio formats (MP3, WAV, etc.)  
✅ Works offline using Whisper's local model  
✅ Can process long-duration audio files  

## 📂 Folder Structure
```
project-folder/
│-- src
│   │-- text-extraction.mp3
│-- documents/
│   │-- sample_audio.mp3
│-- README.md
```

## 📜 License
This project is open-source and available under the **MIT License**.

---
🚀 **Start converting speech to text effortlessly!** 🎧

