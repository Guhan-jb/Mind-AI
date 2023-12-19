import sounddevice as sd
from scipy.io.wavfile import write
import openai
openai.api_key="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"
def record_and_save_audio(filename="audio.wav", duration=5, samplerate=44100):
    print("Recording audio... Press Ctrl+C to stop.")
    try:
        # Record audio from the default microphone
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='int16')
        sd.wait()

        # Save the audio data to a WAV file
        write(filename, samplerate, audio_data)
        with open("audio.wav", "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                file = audio_file,
                model = "whisper-1",
                response_format="text",
            )
        return(transcript)
    except KeyboardInterrupt:
        print("\nRecording stopped.")

def transcribe():
    with open("audio.wav", "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format="text",
            language="en"
        )
    print(transcript)
if __name__ == "__main__":
    output_filename = "audio.wav"
    record_and_save_audio(output_filename)
