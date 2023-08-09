# import required modules
import json

def create_file(filename, ar_value):
    '''Function to change the approach rate of all notes in a Cytoid
    chart by the same flat multiplier.'''

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

    # loop through all notes in note_list
    for note in chart['note_list']:

        try:
            # if key exists, multiply the already existing value by ar_rate
            note['approach_rate'] *= ar_value

        # if key doesn't exist, create the key
        except KeyError:
            
            # change approach rate of each note to chosen multiplier
            note['approach_rate'] = ar_value

    # export the chart file
    with open(get_output_name(filename, ar_value), 'w') as output_file:
        json.dump(chart, output_file, indent=3)

def get_output_name(filename, ar_value):
    '''Function that returns the output name for a chart file being
    worked with.'''

    # get the index of the last dot in filename
    last_dot = filename.rfind('.')

    # if file does not have extension (no dot in filename),
    # put the rate after the entire filename
    if last_dot == -1:
        output_name = (filename
                       + '_ar'
                       + str(ar_value)
                       + 'x')

    # otherwise, create the output name by putting the rate
    # in between the filename and the extension
    else:
        output_name = (filename[:last_dot]
                       + '_ar'
                       + str(ar_value)
                       + 'x'
                       + filename[last_dot:])

    return output_name
