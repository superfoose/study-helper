import sounddevice as sd
import numpy as np
import wave
import os

def speak():
# Set parameters
    duration = 5  # Recording duration in seconds
    sample_rate = 44100  # Sample rate (samples per second)

    # Record audio
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Wait for recording to finish
    print("Finished recording.")

    # Save the recorded audio to a WAV file
    wavefile = wave.open("output.wav", "wb")
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)  # 16-bit PCM
    wavefile.setframerate(sample_rate)
    wavefile.writeframes(audio_data.tobytes())
    wavefile.close()

    from openai import OpenAI
    client = OpenAI(api_key='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')

    audio_file = open("output.wav", "rb")
    transcript = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
    )
    os.remove("output.wav")
    print(transcript)

    chat = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": transcript + " explain this for חזותי",
                        }
                    ],
                    model="gpt-3.5-turbo",
                )
    teach = chat.choices[0].message.content.strip()
    print(teach)
    return teach

speak()