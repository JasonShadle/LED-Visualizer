import pyaudio, math, time
import numpy as np
from scipy.fftpack import fft
import audioop

np.set_printoptions(suppress=True)
CHUNK = 4096
RATE = 44100
INDEX = 1
SCALE = 1000
EXPONENT = 7

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt32,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=INDEX)

vol = 0
max = 0
maxCount = 0
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int32)
    freq = fft(data) # frequencies via Fast Fourier transform
    vol = int((vol + audioop.rms(data, 2)) / 2) # sequiential average

    # calculate volume from 0 to 1, 1 being max
    if vol > max:
        max = vol
        maxCount = 0
    elif maxCount > 10:
        max *= .99
    else:
        maxCount+= 1
    
    # find 
    print((vol+1)/(max+1))
    time.sleep(.01)