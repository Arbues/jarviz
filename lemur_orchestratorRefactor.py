import os
from lemur_core_tts import text_to_speech
from lemur_core_stt import record_audio, save_recording, transcribe_audio
from lemur_core_llm import handle_query
from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    """ Plays an MP3 file using pydub. """
    print("Playing audio...")
    # audioSegment = AudioSegment()
    audio = AudioSegment.from_file(file_path)
    play(audio)
    os.remove(file_path)  # Clean up the audio fileqq

def main():
    try:
        # Step 1: Record and transcribe audioqq
        print("Please speak into the microphone...")
        audio = record_audio()
        audio_file_path = save_recording(audio)
        print("Transcribing audio...")
        transcript = transcribe_audio(audio_file_path)
        print(f"Transcript: {transcript}")
        os.remove(audio_file_path)  # Clean up the audio file

        # Step 2: Process the transcription with the LLM
        response_text = handle_query(transcript)
        print(f"LLM Response: {response_text}")

        # Step 3: Convert the response to speech
        speech_file_path = text_to_speech(response_text)
        print(f"Speech file created at: {speech_file_path}")
        print("play",speech_file_path)
        # Step 4: Play the response audio
        play_audio(speech_file_path)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
