from google.cloud import texttospeech

# Google Text-to-Speech client initialization
def init_tts_client():
    return texttospeech.TextToSpeechClient()

# Convert text to speech and save as an MP3
def text_to_speech(text):
    client = init_tts_client()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="es-PE", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    output_path = "output_tts.mp3"
    with open(output_path, "wb") as out:
        out.write(response.audio_content)
    return output_path
