# import required modules
import json

# ask for user info
input_name = input("Enter filename: ")
output_name = input("Enter output filename: ")
ar_rate = float(input(r'Enter a rate eg. 1.1: '))

# NOTE: output_name will automatically be determined by the AR multiplier
# in the final program
# NOTE: may need to change variable name in final program as well

# attempt to open the chart file
try:
    chart = json.load(open(input_name, 'r', encoding='utf-8'))

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
        # check if key exists
        note['approach_rate']

        # if key exists, multiply the already existing value by ar_rate
        note['approach_rate'] *= ar_rate

    # if key doesn't exist, create the key
    except KeyError:
        
        # change approach rate of each note to chosen multiplier
        note['approach_rate'] = ar_rate

# export the chart file
with open(output_name, 'w') as output_file:
    json.dump(chart, output_file, indent=3)
