import pynput.keyboard
import sounddevice as sd
import numpy as np

def pitch_to_key(pitch):
    if pitch < 70:
        return pynput.keyboard.KeyCode.from_char('w')
    elif pitch < 60:
        return pynput.keyboard.KeyCode.from_char('a')
    elif pitch < 300:
        return pynput.keyboard.KeyCode.from_char('s')
    elif pitch < 
     
def audio_callback(indata, frames, time, status):
    pitch = calculate_pitch(indata)
    key = pitch_to_key(pitch)
    if key is not None:
        controller = pynput.keyboard.Controller()
        with controller.pressed(key):
            pass
          
def calculate_pitch(audio):
    pitch = process_audio(audio)
    return pitch

sample_rate = 44100
duration = 0.1

with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))

