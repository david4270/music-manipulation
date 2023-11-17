import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import numpy as np

import src.listenclip as listenclip
import src.plotclip as plotclip
import src.recordclip as recordclip
import src.manipulateclip as manipulateclip

# Example wav from: https://www2.cs.uic.edu/~i101/SoundFiles/
# WAV file format - https://docs.fileformat.com/audio/wav/
# also useful - http://soundfile.sapp.org/doc/WaveFormat/

# Read WAV file - https://docs.python.org/3/library/wave.html
# Read WAV file in scipy - https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html

# real-time music manipulation? or sound analysis (guitar tuner?)
# two different projects?

def main():
    
    filename = 'example.wav'
    #filename = 'guitar_c3.wav'
    foldername = os.path.join(os.getcwd(),'assets')
    filename = os.path.join(foldername,filename)

    
    #plotclip.plotclip_all(filename)
    #plotclip.plotclip_all_fft(filename)
    #plotclip.spectrogram_all(filename)
    #plotclip.plotclip_animate_waveform(filename, False, fps=30)
    #plotclip.plotclip_animate_waveform(filename, True, fps=6)
    #plotclip.plotclip_animate_fft(filename, True, fps=4.8)

    #listenclip.listen2Music(filename)

    #recordclip.livestream_voice()

    #manipulateclip.test(filename)
    manipulateclip.pitchShifter(filename, 12)
    manipulateclip.timeStretcher(filename, 0.5)
    manipulateclip.phaseVocoder(filename, 0.5)

if __name__ == '__main__':
    main()
