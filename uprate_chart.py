# import required modules
import json

# ask for user info
input_name = input("Enter filename: ")
output_name = input("Enter output filename: ")
rate = float(input("Enter a rate eg. 1.1: "))

# NOTE: output_name will automatically be determined by the rate chosen
# by the user in the final program

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

# loop through tempo_list in the chart file and change each tempo value
# (the tempo value determines the speed of the chart)
for tempo in chart['tempo_list']:
    tempo['value'] = round(tempo['value'] / rate)

# export the chart file
with open(output_name, 'w') as output_file:
    json.dump(chart, output_file, indent=3)
