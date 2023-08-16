# import required modules
import ar_flattener_but_it_has_a_gui as brick_flatten
import json

def create_file(filename, ar_value):
    '''Function to change the approach rate of all notes in a Cytoid
    chart to the same effective value.'''

    # attempt to open the chart file and allow brick_flatten module
    # to use the file
    brick_flatten.chart = json.loads(open(
        filename,
        'r',
        encoding='utf-8').read())

    # give ar_value to brick_flatten module
    brick_flatten.target_BPM = ar_value

    # flatten AR of all notes in Cytoid chart
    brick_flatten.flatten()

    # export the chart file
    with open(get_output_name(filename, ar_value), 'w') as output_file:
        json.dump(brick_flatten.chart, output_file, indent=3)

def get_output_name(filename, ar_value):
    '''Function that returns the output name for a chart file being
    worked with.'''

    # get the index of the last dot in filename
    last_dot = filename.rfind('.')

    # if file does not have extension (no dot in filename),
    # put the rate after the entire filename
    if last_dot == -1:
        output_name = (filename
                       + '_ar_c'
                       + str(ar_value))

    # otherwise, create the output name by putting the rate
    # in between the filename and the extension
    else:
        output_name = (filename[:last_dot]
                       + '_ar_c'
                       + str(ar_value)
                       + filename[last_dot:])

    return output_name
