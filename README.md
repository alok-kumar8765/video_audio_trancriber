# 🎙️ AI Audio & Video Transcriber

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)
![OpenAI Whisper](https://img.shields.io/badge/AI-OpenAI%20Whisper-00A67E.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An intuitive, locally-hosted web application built with Python, Streamlit, and OpenAI's Whisper model that converts media files (`.mp3`, `.mp4`, `.wav`, etc.) into accurate text transcriptions without sending data to external paid APIs.

---

## 📐 Table of Contents

* [About the Project](#-about-the-project)
* [Key Features](#-key-features)
* [Prerequisites](#-prerequisites)
* [Setup Guide](#-setup-guide)
* [How to Use](#-how-to-use)
* [Pros & Cons](#-pros--cons)
* [Contributing](#-contributing)
* [License](#-license)
* [Acknowledgments & Thanks](#-acknowledgments--thanks)

---

## 🧐 About the Project

Transcribing recorded meetings, lectures, interviews, and videos manually is time-consuming. Commercial speech-to-text API services often come with recurring costs and privacy concerns regarding uploading personal or confidential recordings to external servers.

**AI Audio & Video Transcriber** leverages OpenAI's open-source **Whisper** model to provide powerful speech recognition directly on your machine. Paired with a user-friendly Streamlit web interface, you can upload media files, preview audio playback, and export clean text files in a few simple clicks.

---

## ✨ Key Features

* 📁 **Multi-Format Support:** Handles common audio and video media files including `.mp3`, `.mp4`, `.wav`, `.m4a`, and `.mpeg`.
* 🔒 **Privacy First:** Performs transcription processing locally on your machine—no data is sent to third-party web services.
* ⚡ **OpenAI Whisper Powered:** Utilizes state-of-the-art automatic speech recognition (ASR) trained on thousands of hours of diverse multilingual data.
* ⬇️ **Export Functionality:** Instant download of completed transcriptions in plain text (`.txt`) format.
* 🎨 **Interactive UI:** Built-in web interface powered by Streamlit featuring audio preview controls and progress state indicators.

---

## ⚙️ Prerequisites

Before getting started, make sure your system meets the following requirements:

1. **Python 3.8+** installed on your system.
2. **FFmpeg** installed and added to your system's PATH variable (required by Whisper for audio processing/conversion).
   * **Windows (via Chocolatey):** `choco install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/).
   * **macOS (via Homebrew):** `brew install ffmpeg`
   * **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`

---

## 🚀 Setup Guide

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alok-kumar8765/video_audio_trancriber
   cd video_audio_trancriber
   ```

2. **Create and Activate a Virtual Environment:**
   * **Windows:**
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   * **macOS/Linux:**
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install Required Packages:**
   ```bash
   pip install streamlit openai-whisper torch
   ```

---

## 🛠️ How to Use

1. **Launch the Streamlit App:**
   ```bash
   python -m streamlit run app.py
   ```
2. **Access the Interface:**
   Open your browser at `http://localhost:8501`.
3. **Transcribe Your File:**
   * Click **Browse files** or drag and drop your `.mp3` or `.mp4` file into the file upload box.
   * Click **Transcribe Audio**.
   * Review the generated text in the transcription box and click **Download Transcription as TXT** to save your result.

---

## ⚖️ Pros & Cons

### Pros
* ✅ **No API Fees:** Free to run locally without subscribing to external paid services.
* ✅ **High Accuracy:** Powered by OpenAI Whisper's deep learning architecture.
* ✅ **Data Privacy:** Your uploaded audio and video recordings remain local to your machine.
* ✅ **Multilingual Support:** Handles multiple languages and automatically translates foreign languages to English if configured.

### Cons
* ⚠️ **Hardware Dependent:** Processing speeds depend on your computer's CPU/GPU performance (larger Whisper models require a dedicated GPU for optimal speed).
* ⚠️ **FFmpeg Requirement:** System requires FFmpeg installed locally to handle video/audio containers.
* ⚠️ **Initial Load Time:** The AI model is downloaded on the first run, which may take a few minutes depending on network speed.

---

## 🤝 Contributing

Contributions are always welcome! Whether you want to add support for SRT subtitle generation, custom model size selection, or UI improvements:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewFeature`).
3. Commit your Changes (`git commit -m 'Add NewFeature'`).
4. Push to the Branch (`git push origin feature/NewFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙏 Acknowledgments & Thanks

* **[OpenAI Whisper](https://github.com/openai/whisper):** For developing and open-sourcing an incredible state-of-the-art speech recognition model.
* **[Streamlit](https://streamlit.io/):** For providing an elegant framework to turn Python scripts into interactive web applications effortlessly.
* **[PyTorch](https://pytorch.org/):** For powering the underlying machine learning framework.

---
*Created with ❤️ for simple, accessible, and private media transcription.*