# import required modules
import json

def create_file(rate):
    '''Function that updates the information in a level.json file.'''
    
    # attempt to open the level.json file

    # NOTE: the level.json file will get renamed to beta.level.json before
    # being worked with in the final program
    try:
        json_file = json.load(open('beta.level.json', 'r', encoding='utf-8'))

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

    # add rate to level id, separated by an underscore
    json_file['id'] += '_' + str(rate) + 'x'

    # add rate to title inside existing square brackets 
    if square_brackets(json_file['title']) == True:
        json_file['title'] = (json_file['title'][:-1]
                              + ' '
                              + str(rate)
                              + 'x]')

    # add rate to title in new square brackets
    else:
        json_file['title'] += ' [' + str(rate) + 'x]'

    # add rate to title_localized inside existing square brackets
    try: 
        if square_brackets(json_file['title_localized']) == True:
            json_file['title_localized'] = (json_file['title_localized'][:-1]
                                            + ' '
                                            + str(rate)
                                            + 'x]')

        # add rate to title_localized in new square brackets    
        else:
            json_file['title_localized'] += ' [' + str(rate) + 'x]'

    # if the chart has no title_localized, skip this step
    except KeyError:
        pass

    # open level.json file and export the new json_file information
    with open('level.json', 'w', encoding='utf-8') as output_file:
        json.dump(json_file, output_file, indent=3, ensure_ascii=False)

    # TODO: update audio and chart paths in final program


# function to check for square brackets e.g. [Hard]
def square_brackets(string):
    '''The function checks whether title or title_localized have square 
    brackets. Square brackets are a convention used by some charters 
    that include information describing the chart(s), and is not
    considered part of the song title. If square brackets are detected
    in the song title, the rate will be inserted inside the square 
    brackets instead of being appended at the end of the title.
    '''
    if '[' in string and string.endswith(']'):
        return True
    else:
        return False
