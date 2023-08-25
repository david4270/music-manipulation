import pyaudio
import wave
import sys
import os
import matplotlib.pyplot as plot
import numpy as np

import src.listenclip as listenclip
import src.plotclip as plotclip


def main():
    filename = 'example.wav'
    foldername = os.path.join(os.getcwd(),'assets')
    filename = os.path.join(foldername,filename)

    plotclip.plotclip_all(filename)
    plotclip.plotclip_all_fft(filename)
    plotclip.spectrogram_all(filename)

    listenclip.listen2Music(filename)

    """
    
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    sample_width = wf.getsampwidth()
    sample_channel = wf.getnchannels()
    sample_rate = wf.getframerate()    
    frame_rate = int(sample_rate/30) #735

    print(sample_width, sample_channel, sample_rate, frame_rate)
    stream = p.open(format = 
                    p.get_format_from_width(sample_width),
                    channels = sample_channel,
                    rate = sample_rate,
                    output=True)

    data = wf.readframes(frame_rate)
    
    #print(data[0], data[1], data)
    #data_arr = [i for i in data]
    #newdata = np.array(data_arr)
    #plot.plot(newdata)
    #plot.show()
    
    while data != b'':
        
        data_arr = [i for i in data]
        print(max(data_arr))
        newdata = np.array(data_arr)
        plot.plot(newdata)
        plot.show()
        
        #print(data)
        stream.write(data)
        data = wf.readframes(frame_rate)
    
    stream.close()
    p.terminate()
    """


if __name__ == '__main__':
    main()
