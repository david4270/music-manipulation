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

def pitchShifter(filename, diff = 0):
    wf = wave.open(filename, 'rb')
    params = wf.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    data = wf.readframes(nframes)
    wf.close()

    # Convert data to numpy array
    data = np.frombuffer(data, dtype=np.int16)

    # Apply FFT to convert signal to frequency domain
    fft = np.fft.fft(data)

    # Calculate frequency shift factor
    shift_factor = 2 ** (diff / 12)

    # Scale frequency domain signal by shift factor
    shifted_fft = np.zeros_like(fft)

    #shifted_fft = np.zeros(len(fft) * int(shift_factor))
    for i in range(len(shifted_fft)):
        shifted_fft[i] = fft[int(i / shift_factor)]

    # Apply IFFT to convert signal back to time domain
    shifted_data = np.fft.ifft(shifted_fft).real.astype(np.int16)

    #print(params)
    # Write shifted data to new WAV file
    wf = wave.open('shifted.wav', 'wb')
    wf.setparams(params)
    #wf.setframerate(int(framerate / shift_factor))
    wf.writeframes(shifted_data.tobytes())
    wf.close()
    


def timeStretcher(filename, stretch_factor = 1.0):
    wf = wave.open(filename, 'rb')
    params = wf.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    data = wf.readframes(nframes)
    wf.close()

    # Convert data to numpy array
    data = np.frombuffer(data, dtype=np.int16)

    # Apply FFT to convert signal to frequency domain
    fft = np.fft.fft(data)

    # Scale frequency domain signal by stretch factor
    stretched_fft = np.zeros_like(fft)
    #stretched_fft = np.zeros(len(fft) * int(stretch_factor))
    for i in range(len(stretched_fft)):
        stretched_fft[i] = fft[int(i * stretch_factor)]

    # Apply IFFT to convert signal back to time domain
    shifted_data = np.fft.ifft(stretched_fft).real.astype(np.int16)

    # Write shifted data to new WAV file
    wf = wave.open('stretched.wav', 'wb')
    wf.setparams(params)
    wf.writeframes(shifted_data.tobytes())
    wf.close()



def phaseVocoder(filename, rate):
    wf = wave.open(filename, 'rb')
    params = wf.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    data = wf.readframes(nframes)
    wf.close()

    # Convert data to numpy array
    data = np.frombuffer(data, dtype=np.int16)

    # Apply FFT to convert signal to frequency domain
    fft = np.fft.fft(data)

    # Phase vocoder algorithm
    phases = np.angle(fft)
    magnitudes = np.abs(fft)
    modified_magnitudes = np.interp(np.arange(0, len(magnitudes)), np.arange(0, len(magnitudes), rate), magnitudes) 
    print(phases.shape, modified_magnitudes.shape)
    modified_fft = modified_magnitudes * np.exp(phases * 1j)

    # Apply IFFT to convert signal back to time domain
    shifted_data = np.fft.ifft(modified_fft).real.astype(np.int16)

    # Write shifted data to new WAV file
    wf = wave.open('phase_vocoded.wav', 'wb')
    wf.setparams(params)
    wf.writeframes(shifted_data.tobytes())
    wf.close()
