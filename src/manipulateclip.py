import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import math

def test(filename, diff = 0):
    ()

def changePitch(filename, diff = 0):
    wf = wave.open(filename, 'rb')
    param_wf = list(wf.getparams())
    param_wf[3] = 0
    param_wf = tuple(param_wf)
    wf_channel = wf.getnchannels()
    
    ww = wave.open('towrite.wav','w')
    ww.setparams(param_wf)

    freq = 20
    sample_rate = wf.getframerate()
    size = sample_rate//freq
    count = int(wf.getnframes()/size)
    print(count)

    #shift = 2 ** (diff/12)
    shift = 2
    for frameno in range(count):
        wf_raw = wf.readframes(size)
        wf_raw = np.fromstring(wf_raw, dtype=np.int16)
        new_frames = []
        for i in range(wf_channel):
            wf_data = wf_raw[i::wf_channel]
            frame = np.fft.fft(wf_data)
            x = np.fft.fftfreq(wf_data.size, d = 1./sample_rate)
            #print(x)
            x *= 2 ** (1/12)
            #print(x)
            #newframe = frame * 2**(1/12) - frame
            #frame = np.roll(frame, newframe)
            #frame[0:int(shift)] = 0
            #new_frame = np.fft.irfft(frame)
            new_frame = np.fft.ifft(frame)
            new_frames.append(new_frame)
        new_stack = np.column_stack([nf for nf in new_frames]).ravel().astype(np.int16)
        ww.writeframes(new_stack.tostring())
    
    wf.close()
    ww.close()
        

        
