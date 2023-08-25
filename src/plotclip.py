import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import numpy as np

# To-do
# - Animated waveform
# - partial waveform, fft, spectrogram
# - support stereo (or manipulate to support)
# - add more flexibility to functions
# - display (plot) in different shapes - not only wave (bar graph?)

# show waveform of entire clip
def plotclip_all(filename):
    wf = wave.open(filename, 'rb')
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")
    #print(sample_rate/30)

    if sample_channel == 2:
        print("Stereo not supported")
        return

    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    plot.plot(time,wf_raw, color = "blue")
    plot.show()

# show spectrogram of entire clip
def spectrogram_all(filename):
    wf = wave.open(filename, 'rb')
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")
    
    if sample_channel == 2:
        print("Stereo not supported")
        return

    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    plot.specgram(wf_raw, Fs = sample_rate, vmin = -20, vmax = 50)
    plot.colorbar()
    plot.show()

# show fft of entire clip
def plotclip_all_fft(filename):
    wf = wave.open(filename, 'rb')
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")
    #print(sample_rate/30)

    if sample_channel == 2:
        print("Stereo not supported")
        return

    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    
    fft_spectrum = np.fft.rfft(wf_raw)
    freq = np.fft.rfftfreq(wf_raw.size, d = 1./sample_rate)
    fft_spectrum_abs = np.abs(fft_spectrum)

    plot.plot(freq,fft_spectrum_abs, color = "blue")
    plot.show()

# animate clip waveform?
