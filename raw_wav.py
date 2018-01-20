#written by ythuo
import wave
import os
import numpy as np

file_list =open("hraw1.lst")
for line in file_list:
    line = line.strip('\n')
    f = open(line,'rb')
    str_data = f.read()
    a = line[56:67]
    wave_file = "/home/disk3/ythuo/wav/" + a + ".wav"
    wave_out=wave.open(wave_file,'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(1)
    wave_out.setframerate(8000)
    wave_out.writeframes(str_data)
