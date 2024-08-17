#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

import pyaudio
import wave



dst_path = "your_file_path/your_file_name.wav"
chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100
time = 30 # in seconds

audio = pyaudio.PyAudio()

stream = audio.open(format=format, channels=channels,
                    rate=rate, input=True,
                    frames_per_buffer=chunk)

frames = []
for i in range(0, int(rate / chunk * time)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(dst_path, 'wb')
waveFile.setnchannels(channels)
waveFile.setsampwidth(audio.get_sample_size(format))
waveFile.setframerate(rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()
