import pyaudio
# List all audio input devices
p = pyaudio.PyAudio()
i = 0
n = p.get_device_count()
while i < n:
    dev = p.get_device_info_by_index(i)
    if dev['maxInputChannels'] > 0:
        print(str(i)+'. '+dev['name'])
    i += 1