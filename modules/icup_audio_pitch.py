# import required modules
from pydub import AudioSegment
import ffmpeg
import fleep

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

    # export the file
    audio_rate.export(get_output_name(filename, rate),
                      format=get_format(filename))


def get_format(filename):
    '''Function to get the file extension of a chosen file.'''

    with open(filename, 'rb') as file:
        info = fleep.get(file.read(128))

    # if audio file is ogg format (commonly used format in Cytoid
    # where info.extension returns a list of two strings instead of
    # a single string)
    if info.extension == ['oga', 'ogv']:

        # set file_format to ogg
        file_format = 'ogg'

    else:

        # for other extensions, let file_format be
        # same as info.extension
        file_format = info.extension[0]

    return file_format


def get_output_name(filename, rate):
    '''Function that returns the output name for an audio file being
    worked with.'''

    # get the index of the last dot in filename
    last_dot = filename.rfind('.')

    # if file does not have extension (no dot in filename),
    # put the rate after the entire filename
    if last_dot == -1:
        output_name = (filename
                       + '_'
                       + str(rate)
                       + 'x.'
                       + get_format(filename))

    # otherwise, create the output name by putting the rate
    # in between the filename and the extension
    else:
        output_name = (filename[:last_dot]
                       + '_'
                       + str(rate)
                       + 'x.'
                       + get_format(filename))

    return output_name
