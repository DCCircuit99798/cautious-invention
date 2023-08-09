# import required modules
import json

def create_file(filename, rate):
    '''Function to change the speed of a Cytoid chart file.'''
    
    # attempt to open the chart file
    try:
        chart = json.load(open(filename, 'r', encoding='utf-8'))

    # print error message if file is not found
    except FileNotFoundError:
        print('ERROR: File not found!')
        input()
        exit()

    # print error message if text file is not valid json
    except json.JSONDecodeError:
        print('ERROR: Invalid input file!')
        input()
        exit()

    # loop through tempo_list in the chart file and change each tempo value
    # (the tempo value determines the speed of the chart)
    for tempo in chart['tempo_list']:
        tempo['value'] = round(tempo['value'] / rate)

    # export the chart file
    with open(get_output_name(filename, rate), 'w') as output_file:
        json.dump(chart, output_file, indent=3)
        

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
                       + 'x')

    # otherwise, create the output name by putting the rate
    # in between the filename and the extension
    else:
        output_name = (filename[:last_dot]
                       + '_'
                       + str(rate)
                       + 'x'
                       + filename[last_dot:])

    return output_name
