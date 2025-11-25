import requests
import time
import re
import os
import platform

# Optional: playsound only if running locally
try:
    from playsound import playsound
    can_play_audio = True
except ImportError:
    can_play_audio = False

# ===== CONFIG =====
API_KEY = "sk_71c880e3f5c60243ae50ae7b9be03282c52cff799c9e6fb8"

# ===== FETCH VOICES =====
def fetch_voices(api_key):
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {"xi-api-key": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        voices_data = response.json().get("voices", [])
        return {v["name"]: v["voice_id"] for v in voices_data}
    except Exception as e:
        print(f"❌ Failed to fetch voices: {e}")
        return {}

voices = fetch_voices(API_KEY)
if not voices:
    print("⚠ No voices available. Exiting.")
    exit()

# ===== DISPLAY VOICES =====
print("\nAvailable voices:")
voice_names = list(voices.keys())
for i, name in enumerate(voice_names, start=1):
    print(f"{i}. {name}")

# ===== GET VOICE SELECTION =====
while True:
    choice = input(f"\nSelect a voice [1-{len(voice_names)}]: ")
    if choice.isdigit() and 1 <= int(choice) <= len(voice_names):
        choice_num = int(choice)
        break
    else:
        print("⚠ Invalid input. Please enter a number from the list.")

voice_name = voice_names[choice_num - 1]
voice_id = voices[voice_name]
print(f"✅ Selected voice: {voice_name}")

# ===== GET TEXT INPUT =====
text = input("\nEnter the text you want to generate: ")

# ===== CALL API =====
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
payload = {"text": text}
headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"DEBUG: status_code = {response.status_code}")
    if response.status_code != 200:
        print(f"❌ Error: {response.text}")
        exit()
except Exception as e:
    print(f"❌ Failed to call Eleven Labs API: {e}")
    exit()

# ===== SAVE MP3 =====
recordings_dir = os.path.join(os.getcwd(), "recordings")
os.makedirs(recordings_dir, exist_ok=True)

snippet = re.sub(r'\W+', '', text[:10])
timestamp = int(time.time())
filename = f"{voice_name}_{snippet}_{timestamp}.mp3"
filepath = os.path.join(recordings_dir, filename)

with open(filepath, "wb") as f:
    f.write(response.content)

print(f"\n✅ Audio saved at: {filepath}")

# ===== AUTO-OPEN MP3 ON WINDOWS =====
if platform.system() == "Windows":
    try:
        os.startfile(filepath)
        print("ℹ Audio opened in default player.")
    except Exception as e:
        print(f"⚠ Could not open audio automatically: {e}")
else:
    print("ℹ Auto-play skipped (not Windows).")
