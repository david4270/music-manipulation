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

    num_frames = wf.getnframes()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")
    #print(sample_rate/30)

    if sample_channel > 1:
        wf_raw = wf_raw[::sample_channel]
        #wf_raw = wf_raw[1::2]
        #print("Stereo not supported")
        #return

    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    plot.plot(time,wf_raw, color = "blue")
    plot.show()

# show spectrogram of entire clip
def spectrogram_all(filename):
    wf = wave.open(filename, 'rb')

    num_frames = wf.getnframes()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")
    #print(wf_raw)

    #print(wf_raw.shape)
    
    if sample_channel > 1:
        wf_raw = wf_raw[::sample_channel]
    """
    if sample_channel == 2:
        print("Stereo not supported")
        return
    """
    
    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    plot.specgram(wf_raw, Fs = sample_rate, vmin = -20, vmax = 50)
    plot.colorbar()
    plot.show()

# show fft of entire clip
def plotclip_all_fft(filename):

    wf = wave.open(filename, 'rb')
    num_frames = wf.getnframes()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    
    wf_raw = wf.readframes(-1)
    wf_raw = np.frombuffer(wf_raw, "int16")

    #print(np.shape(wf_raw))
    #print(wf_raw)
    
    #print(sample_rate/30)
    if sample_channel > 1:
        wf_raw = wf_raw[::sample_channel]
    """
    if sample_channel == 2:
        print("Stereo not supported")
        return
    """
    time = np.linspace(0,len(wf_raw)/sample_rate, num = len(wf_raw))
    #print(len(wf_raw)/sample_rate)
    #print(np.size(time))

    fft_spectrum = np.fft.rfft(wf_raw)
    freq = np.fft.rfftfreq(wf_raw.size, d = 1./sample_rate)
    fft_spectrum_abs = np.abs(fft_spectrum)

    plot.plot(freq,fft_spectrum_abs, color = "blue")
    plot.show()

# animate clip waveform?
def plotclip_animate_waveform(filename, play_music = False, fps = 30):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    
    sample_width = wf.getsampwidth()
    num_frames = wf.getnframes()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    frames_per_second = fps  # can use 30 - for playing music smoothly, use 6 
    sample_size = int(sample_rate/frames_per_second)

    if play_music:
        stream = p.open(format = p.get_format_from_width(sample_width), channels=sample_channel, rate = sample_rate, output = True)
    #print(num_frames, sample_rate)

    fig = plot.figure()
    ax = plot.axes(xlim = (0, sample_size), ylim = (-2**15,2**15))
    line, = ax.plot([],[],lw=2)

    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        x = np.linspace(0, sample_size-1, sample_size)
        wf_raw = wf.readframes(sample_size)

        
        #print(i)
        y = np.frombuffer(wf_raw, "int16")
        if sample_channel > 1:
            y = y[::sample_channel]
        if play_music:
            stream.write(wf_raw)
        #print(y)
        line.set_data(x,y)
        
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(num_frames/sample_size), interval=1000/frames_per_second, repeat = False, blit=True)

    plot.show()

    if play_music:
        print("finished")
        stream.close()
        p.terminate()
        

# animate fft
def plotclip_animate_fft(filename, play_music = False, fps = 30):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    
    sample_width = wf.getsampwidth()
    num_frames = wf.getnframes()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()
    frames_per_second = fps  # can use 30 - for playing music smoothly, use 6 
    sample_size = int(sample_rate/frames_per_second)

    if play_music:
        stream = p.open(format = p.get_format_from_width(sample_width), channels=sample_channel, rate = sample_rate, output = True)
    #print(num_frames, sample_rate)

    fig = plot.figure()
    ax = plot.axes(xlim = (0, sample_rate/2), ylim = (0,10**7))
    line, = ax.plot([],[],lw=2)

    def init():
        line.set_data([],[])
        return line,

    def animate(i):
        #x = np.linspace(0, sample_size-1, sample_size)
        wf_raw = wf.readframes(sample_size)
        #print(i)
        wf_buf = np.frombuffer(wf_raw, "int16")
        
        if sample_channel > 1:
            wf_buf = wf_buf[::sample_channel]
        
        fft_spectrum = np.fft.fft(wf_buf)
        x = np.fft.fftfreq(wf_buf.size, d = 1./sample_rate)
        y = np.abs(fft_spectrum)
        #inverst_fft = np.rint(np.fft.ifft(fft_spectrum)).astype(int)
        
        #print(wf_buf)
        #print(inverst_fft)

        #inverst_fft = inverst_fft.tobytes()
        
        if play_music:
            stream.write(wf_raw)
            #stream.write(inverst_fft)
        #print(np.shape(y))
        line.set_data(x,y)
        
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(num_frames/sample_size), interval=1000/frames_per_second, repeat = False, blit=True)

    plot.show()

    if play_music:
        print("finished")
        stream.close()
        p.terminate()

#further idea - how about adding bunch of filters?

# visualisation idea
# https://www.youtube.com/watch?v=5LfD-hxbX0E&ab_channel=OutofScope


# https://www.youtube.com/watch?v=MavAU3adGk4&ab_channel=Mr.PSolver