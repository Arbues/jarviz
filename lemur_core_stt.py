import os
import tempfile
from google.cloud import speech
from scipy.io.wavfile import write
import keyboard
import sounddevice as sd

# Google Speech-to-Text client initialization
def init_speech_client():
    return speech.SpeechClient()

def record_audio(fs=44100):
    print("Press 'q' to start recording.")
    keyboard.wait('q')  # Espera hasta que se presione 'q' para comenzar
    print("Recording... Press 'q' to stop.")
    recording = sd.rec(int(10 * fs), samplerate=fs, channels=2, dtype='int16')
    keyboard.wait('q')  # Espera hasta que se presione 'q' para detener
    sd.stop()
    return recording

# Save the recording to a temporary file
def save_recording(recording, fs=44100):
    temp_file = tempfile.mktemp(suffix='.wav', prefix='temp_audio_')
    write(temp_file, fs, recording)  # Write the audio file
    print(f"Audio saved to {temp_file}")
    return temp_file

# Transcribe the audio file
def transcribe_audio(file_path, lang='es-ES'):
    client = init_speech_client()
    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code=lang,
        audio_channel_count=2
    )
    response = client.recognize(config=config, audio=audio)
    transcript = "".join(result.alternatives[0].transcript for result in response.results)
    return transcript
