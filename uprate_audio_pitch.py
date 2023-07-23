# import the required modules
from pydub import AudioSegment
import ffmpeg

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

# manually override samplerate
# (how many samples to play per second)
audio_framerate = audio._spawn(audio.raw_data, overrides={
    'frame_rate': int(audio.frame_rate * rate)
    })

# convert altered samplerate to the original standard samplerate
# (allows the audio to be played properly on other programs)
audio_rate = audio_framerate.set_frame_rate(audio.frame_rate)

# export the file
# (filename comes from file "title" and the chosen rate)
audio_rate.export(title + ".audio_" + str(rate) + "x.ogg", format="ogg")


