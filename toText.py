from gtts import gTTS
import os

# Function to convert text to audio
def text_to_audio(text, output_file="output.mp3"):
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    # Save the audio file
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

# Example usage
text = "Hello, welcome to the text to speech conversion demo!"
output_file = "output.mp3"  # Replace with desired output file name
text_to_audio(text, output_file)
