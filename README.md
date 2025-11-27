# 🎙 ElevenLabs Voice Automation App
A custom Python-based text-to-speech (TTS) application built using the ElevenLabs API.  
Designed to generate **consistent, production-ready character voices** for GTI Studios’ animated series, including:

- Space Bear & Her Kitty Cat Acolytes  
- Samurai Sass  
- Additional GTI Studios projects  

This tool automates the entire voice pipeline from **text input → AI-generated audio → saved WAV/MP3 files**, and is built to integrate directly into your AI-driven animation workflow (ComfyUI → Lip Sync → Editing → Final Export).

---

## ⭐ Features

### 🎭 Multi-Character Voice System  
Define and switch between character profiles (e.g., Captain Bear, Onyx, FluffyBear, Samurai Sass).

### ⚙️ Automated Text-to-Speech Rendering  
Enter any dialogue → instantly generate high-quality WAV/MP3 audio files.

### 💾 Automatic File Saving  
Outputs audio with clean, structured filenames for easy import into editing or animation timelines.

### 🔐 Secure API Key Handling  
Uses environment variables (`.env`) for API key storage — **no hardcoded secrets**.

### 🔄 Production-Ready Voice Consistency  
Ensures stable, repeatable voice identity across multiple episodes, scenes, and projects.

### 🔌 Integrates With Full AI Animation Pipelines  
Works seamlessly with:
- ComfyUI workflows  
- Lip-sync tools  
- n8n automation  
- Video editors (Resolve, Premiere, CapCut)  
- Larger GTI Studios production systems  

---

## 🧰 Tech Stack

- **Python 3.x**  
- **ElevenLabs API**  
- **Requests** (HTTP client)  
- **dotenv** (environment variable handling)  
- **JSON**  
- Optional: Simple CLI or UI depending on configuration  

---

## 📦 Installation

Clone or download the repository:

```bash
git clone https://github.com/GTIstudios/elevenlabs-voice-app
cd elevenlabs-voice-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
ELEVENLABS_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### **Generate a voice line**

```bash
python app.py \
  --text "Captain Bear reporting for duty." \
  --voice "CaptainBear" \
  --output "captain_bear_line1.mp3"
```

### **Basic Python example**

```python
from elevenlabs import generate, save

audio = generate(
    text="Welcome to GTI Studios!",
    voice="BrightNarrator",
    model="eleven_multilingual_v2"
)

save(audio, "output.mp3")
```

---

## 🗂 Output Files

The app saves audio using clean filenames such as:

```
captainbear_scene03_line12.wav
samuraisass_intro01_line04.mp3
```

Perfect for:
- ComfyUI lip-sync nodes  
- Timeline-based editing  
- Batch animation pipelines  
- Automated n8n workflows  

---

## 📂 Project Structure

```
elevenlabs-voice-app/
│
├── app.py
├── voices/
│   └── voice_profiles.json
├── examples/
│   ├── sample_output_1.mp3
│   ├── sample_output_2.mp3
├── assets/
│   └── (add screenshots or waveform images)
├── .env
├── requirements.txt
└── README.md
```

---

## 🖼 Screenshots / Assets
(Optional — recommended for professionalism.)

Add an `/assets/` folder with:

```
voice-ui-example.png
waveform-example.png
tool-overview.png
```

You can embed them like this:

```markdown
![Voice App Screenshot](assets/voice-ui-example.png)
```

---

## 🧪 Example Workflow Integration

### **Animation Pipeline Example (Space Bear & Her Kitty Cat Acolytes)**

```
Script → ElevenLabs Voice App
       → Lip-Sync JSON / Audio
       → ComfyUI Animation
       → Video Sequence Assembly
       → Final 4K Export (Topaz)
```

This app is responsible for **100% of the voice generation** in GTI Studios’ productions.

---

## 💡 Skills Demonstrated

- API integration (ElevenLabs TTS)
- Python scripting & CLI tooling
- Audio file handling & processing
- Environment variable security
- Production workflow design
- Modular voice profile management
- Animation pipeline integration
- GitHub documentation & structure

---

## 🧱 Extended Description

The ElevenLabs Voice Automation App was built to solve a real production need:  
GTI Studios requires consistent, repeatable, character-specific voice generation for multiple animated series. Traditional voice acting pipelines are slow, expensive, and inconsistent—especially during iterative production.

This tool provides a **reliable, script-driven system** for generating lines rapidly while keeping every character’s identity intact.

Key goals behind the project:

1. **Speed** – generating hundreds of lines in minutes.  
2. **Consistency** – character voices must stay identical across episodes.  
3. **Scalability** – quickly expand to new characters and languages.  
4. **Integration** – audio must feed directly into animation workflows.  
5. **Security** – API keys handled safely with `.env`.

This app demonstrates the practical side of applying generative audio models inside a real animation pipeline.

---

## 🚧 Future Enhancements

- [ ] Full batch mode (generate entire script at once)  
- [ ] Streamlit UI for web control panel  
- [ ] Integration with n8n for automated text → voice → upload  
- [ ] Automatic lip-sync JSON export  
- [ ] Multi-language character support  
- [ ] Real-time voice preview tool  

---

## 📄 License
MIT License
