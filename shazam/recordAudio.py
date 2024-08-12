import sounddevice as sd
import wavio as wv

def record_audio():
    # Sampling frequency
    # freq = 44100
    freq = 22050
    
    # Recording duration
    duration = 6
    
    # Start recorder 
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    
    # Record audio
    print("recording starts")
    sd.wait()
    print("recording stopped")
    
    # raw audio
    return recording.tobytes()

# record_audio()
# raw_audio_data = record_audio()
# print(f"Raw audio data length: {len(raw_audio_data)} bytes")