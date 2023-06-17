# import the required modules
from pydub import AudioSegment

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

# create a version of the audio file with a different playback speed
audio_rate = audio.speedup(playback_speed=rate)

# export the file (filename comes from file "title" and the chosen rate)
audio_rate.export(title + ".audio_" + str(rate) + "x.ogg", format="ogg")



