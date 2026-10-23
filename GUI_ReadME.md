# 🎙️ AI Audio & Video Transcriber (Desktop GUI)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![AI Engine](https://img.shields.io/badge/AI-OpenAI%20Whisper-orange.svg)](https://github.com/openai/whisper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A clean, responsive desktop application built with **Python**, **Tkinter**, and **OpenAI's Whisper AI model** to convert audio and video files into accurate text transcripts locally on your machine.

---

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Prerequisites](#-prerequisites)
- [Setup & Installation](#-setup--installation)
- [Usage Guide](#-usage-guide)
- [Use Cases](#-use-cases)
- [Pros & Cons](#-pros--cons)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 📌 About The Project

Transcribing meetings, lectures, interviews, and media clips usually requires third-party cloud services that come with subscription fees, privacy risks, or file size limits. 

This project provides a **100% offline-first, local desktop GUI solution** where users can load MP3 audio or MP4 video files, observe real-time progress, edit or view the generated output, copy text directly to clipboard, or export it into a **PDF document**.

---

## ✨ Key Features

- 🖥️ **Responsive Modern Tkinter GUI:** Automatically scales layout when resizing or maximizing the window.
- ⚡ **Background Threading:** Keeps the application smooth and responsive (prevents "Not Responding" freezes while processing large files).
- 📊 **Visual Progress Tracking:** Animated status indicators and progress bar during AI processing.
- 📋 **One-Click Clipboard Copy:** Effortlessly copy generated transcriptions to your clipboard.
- 📄 **Export to PDF:** Save transcriptions directly as neatly formatted `.pdf` files.
- 🔒 **Privacy First:** All transcriptions are processed locally on your PC — no data is sent to external servers.

---

## ⚙️ Prerequisites

Before running the application, make sure you have:

1. **Python 3.8+** installed on your system.
2. **FFmpeg** installed on your OS (required by Whisper for audio extraction from media files):
   - **Windows:** Install via `choco install ffmpeg` or `winget install ffmpeg`.
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

---

## 📥 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alok-kumar8765/video_audio_trancriber](https://github.com/alok-kumar8765/video_audio_trancriber)
   cd video_audio_trancriber