import pyaudio
import wave
import sys
import matplotlib.pyplot as plot
import numpy as np



def main():
    wf = wave.open('example.wav', 'rb')
    

    sample_width = wf.getsampwidth()
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

    
    
    wf = wave.open('example.wav', 'rb')
    p = pyaudio.PyAudio()
    
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


if __name__ == '__main__':
    main()
