# import the required modules
from pydub import AudioSegment
import ffmpeg

def create_file(filename, rate):
    '''Function to change the speed and pitch of an audio file
       and export the new audio file.'''

    # attempt to open the audio file
    try:
        audio = AudioSegment.from_file(filename)

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

    # get the index of the last dot in filename
    last_dot = filename.rfind('.')

    # create the output name by putting the rate
    # in between the filename and the extension
    output_name = (filename[:last_dot]
                   + '_'
                   + str(rate)
                   + 'x'
                   + filename[last_dot:])

    # export the file
    audio_rate.export(output_name)
