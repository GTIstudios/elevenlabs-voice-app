# ElevenLabs Voice Automation App

A custom Python-based text-to-speech (TTS) application built using the ElevenLabs API.  
Designed to generate consistent character voices for GTI Studios’ animated series, including **Space Bear & Her Kitty Cat Acolytes** and **Samurai Sass**.

This tool automates the entire voice pipeline: text input → AI-generated audio → saved production-ready files.  
Built to integrate directly with an AI animation workflow (ComfyUI → Editing → Final Export).

---

## ⭐ Features

- 🎙 **Multi-character voice system**  
  Define and switch between multiple voice profiles (e.g., Captain Bear, Onyx, Samurai Sass).

- ⚙️ **Automated text-to-speech rendering**  
  Enter dialogue text and instantly output high-quality WAV/MP3 audio.

- 💾 **Automatic file saving**  
  Saves audio with structured filenames for easy import into animation/editor timelines.

- 🔐 **Secure API key handling**  
  Uses environment variables for API keys — no hardcoded secrets.

- 🔄 **Production-ready voice consistency**  
  Ensures stable voice identity across multiple episodes and scenes.

- 🔌 **Integrates with larger AI animation pipelines**  
  Works seamlessly with lip-sync tools, ComfyUI animation, and video editing workflows.

---

## 🧰 Tech Stack

- Python 3.x  
- ElevenLabs API  
- Requests (HTTP client)  
- dotenv (environment variable handling)  
- JSON  
- Optional: simple CLI or UI depending on configuration

---

## 📦 Installation

1. **Clone or download the repository:**

```bash
git clone https://github.com/YourUsername/elevenlabs-voice-app
cd elevenlabs-voice-app
