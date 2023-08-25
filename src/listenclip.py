import pyaudio
import wave
import sys
import matplotlib.pyplot as plot
import numpy as np

def listen2Music(filename):

    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    sample_width = wf.getsampwidth()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    frame_rate = int(sample_rate/30)
    stream = p.open(format = 
                    p.get_format_from_width(sample_width),
                    channels = sample_channel,
                    rate = sample_rate,
                    output=True)

    data = wf.readframes(frame_rate)
    
    while data != b'':
        stream.write(data)
        data = wf.readframes(frame_rate)
    
    stream.close()
    p.terminate()