import speech_recognition as sr
from pydub import AudioSegment

# Step 1: Convert MP3 to WAV
def mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")
    print(f"Converted {mp3_file} to {wav_file}")

# Step 2: Transcribe Audio (WAV) to Text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
    
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("Transcription: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# File paths
mp3_file = "wilfrid.mp3"
wav_file = "wilfridH.wav"

# Convert MP3 to WAV
mp3_to_wav(mp3_file, wav_file)

# Transcribe WAV to text
audio_to_text(wav_file)
