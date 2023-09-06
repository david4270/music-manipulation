import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import numpy as np

import src.listenclip as listenclip
import src.plotclip as plotclip
import src.recordclip as recordclip

# Example wav from: https://www2.cs.uic.edu/~i101/SoundFiles/

# real-time music manipulation? or sound analysis (guitar tuner?)
# two different projects?

def main():
    filename = 'example2.wav'
    foldername = os.path.join(os.getcwd(),'assets')
    filename = os.path.join(foldername,filename)

    
    plotclip.plotclip_all(filename)
    plotclip.plotclip_all_fft(filename)
    plotclip.spectrogram_all(filename)
    #plotclip.plotclip_animate_waveform(filename, False, fps=30)
    plotclip.plotclip_animate_waveform(filename, True, fps=6)
    plotclip.plotclip_animate_fft(filename, True, fps=6)

    #listenclip.listen2Music(filename)

    #recordclip.livestream_voice()


if __name__ == '__main__':
    main()
