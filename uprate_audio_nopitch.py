# import the required modules
from pydub import AudioSegment
import soundfile as sf
import pyrubberband # WARNING: import broken. this file doesn't work for now

# ask for user info
title = input("Enter file title: ")
input_name = input("Enter filename: ")
rate = float(input("Enter rate (e.g. 1.1): "))

# attempt to open the audio file
try:
    audio = AudioSegment.from_file(input_name)

# if the file is not found, print an error message
except FileNotFoundError:
    print('ERROR: File not found!')
    input()
    exit()

# export audio file as .wav file
# (pyrubberband can only work with .wav files)
audio.export(title + '.wav', format='wav')


# open .wav file
y, sr = sf.read(title + '.wav')

# change pitch alongside playback speed
y_speed = pyrubberband.time_stretch(y, sr, rate)
y_pitch = pyrubberband.pitch_shift(y, sr, rate)

# export .wav file with the altered playback speed
sf.write(('new.' + title + '.wav'), y_stretch, sr, format='wav')


# open .wav file with altered speed using AudioSegment
audio_rate_wav = AudioSegment.from_file('new.' + title + '.wav')

# export the file
# (filename comes from file "title" and the chosen rate)
audio_rate.export(title + ".audio_" + str(rate) + "x.ogg", format="ogg")
