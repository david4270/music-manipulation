import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import struct

def record_clip():
    ()

def livestream_voice():
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 44100, input = True, output = True, frames_per_buffer=4096)

    data = stream.read(4096)
    data_int = struct.unpack(str(8192)+'B', data)

    print(data_int)