import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import matplotlib.animation as animation
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

    #print(np.shape(wf_raw))
    #print(wf_raw)
    
    #print(sample_rate/30)

    if sample_channel == 2:
        print("Stereo not supported")
        return

    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    #print(len(wf_raw)/sample_rate)
    #print(np.size(time))

    fft_spectrum = np.fft.rfft(wf_raw)
    freq = np.fft.rfftfreq(wf_raw.size, d = 1./sample_rate)
    fft_spectrum_abs = np.abs(fft_spectrum)

    plot.plot(freq,fft_spectrum_abs, color = "blue")
    plot.show()

# animate clip waveform?
def plotclip_animated_test(filename):
    wf = wave.open(filename, 'rb')
    
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    sample_size = int(sample_rate/30)

    fig = plot.figure()
    ax = plot.axes(xlim = (0, sample_size), ylim = (-2**15,2**15))
    line, = ax.plot([],[],lw=2)

    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        x = np.linspace(0, sample_size-1, sample_size)
        wf_raw = wf.readframes(sample_size)
        """
        if len(wf_raw) == 0:
            line.set_data(x,np.empty(len(x)))
            return line,
        """
        #print(i)
        y = np.frombuffer(wf_raw, "int16")
        #print(y)
        line.set_data(x,y)
        
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1800, interval=1000/30, repeat = False, blit=True)

    """
    fig, ax = plot.subplots()

    x = np.linspace(0, sample_size-1, sample_size)
    line, = ax.plot(x, np.random.rand(sample_size))
    ax.set_ylim(-2**15,2**15)
    ax.set_xlim(0, sample_size)
    
    wf_raw = wf.readframes(sample_size)
    
    while wf_raw != b'':

        wf_raw = np.frombuffer(wf_raw, "int16")
        
        #wf_raw = np.frombuffer(wf_raw, "int16")
        #print(wf_raw)
        #wf_raw = [i for i in wf_raw]
        #wf_raw = np.array(wf_raw)
        #print(wf_raw)
        #print(len(wf_raw))
        line.set_ydata(wf_raw)
        fig.canvas.draw()
        fig.canvas.flush_events()

        wf_raw = wf.readframes(sample_size)
    """
    #plot.show()
        

    