# NOTE: had to comment target_BPM assignment for ICUP. (line 94)
# to get this program to work on its own, uncomment line 94

# Original author: dendroarboritree

import tkinter as tk
from tkinter import filedialog
import json
from sys import platform

chart = []

def ok(msg):
    ok = tk.Tk()
    ok.title('!')
    #ok.maxsize(100, 75)
    ok.minsize(120, 75)
    ok.resizable(0,0)
    if platform == 'win32':
        ok.attributes('-toolwindow', True)
    ok_label = tk.Label(ok,text=msg)
    ok_label.pack(side='top',fill='x',pady=10)
    ok_btn = tk.Button(ok,text='ok',command=ok.destroy)
    ok_btn.pack()
    ok.mainloop()

def flatten():
    global chart
    global target_BPM_input

    # initialize magic numbers
    TIME = 1 / (chart['time_base'] * 1000000)
    MAGIC = 1.367

    # calculate page lengths
    # tempo_list from the chart file
    tempos = chart['tempo_list']
    # page_list from the chart file
    pages = chart['page_list']
    # list of page lengths in seconds
    page_len_list = []
    # start of the current page, first page starts at 0
    page_start = 0
    # index for navigating tempos#the last tick length was calculated up to
    tempo_index = 0
    #last tick checked and added up to page_len_sum
    last_checked_tick = 0

    # calculates the the length in seconds between start and end ticks given
    def calc_span(end, start, value):
        return (end - start) * value * TIME

    # calculate AR
    def calc_ar(page_size, page_ratio, previous_page_size):
        calc_temp = previous_page_size * (MAGIC - page_ratio)
        calc_temp = MAGIC / (page_size * page_ratio + calc_temp)
        return max([calc_temp, 1])

    # iterate through page list to calculate length of every page
    for page in pages:
        page_len_sum = 0

        # look for tempo changes
        while tempo_index + 1 < len(tempos) and \
                tempos[tempo_index + 1]['tick'] <= page['end_tick']:

            page_len_sum += calc_span(tempos[tempo_index + 1]['tick'],
                                    last_checked_tick,
                                    tempos[tempo_index]['value'])
            last_checked_tick = tempos[tempo_index + 1]['tick']
            tempo_index += 1

        # check for any remaining ticks after last checked tick
        if last_checked_tick < page['end_tick']:
            page_len_sum += calc_span(page['end_tick'],
                                    last_checked_tick,
                                    tempos[tempo_index]['value'])

        # update to next page
        page_start = page['end_tick']
        last_checked_tick = page_start
        page_len_list.append(page_len_sum)
        page_len_sum = 0

    # duplicate page length for the first page
    page_len_list.insert(0, page_len_list[0])

    # oops
    # print(page_len_list)

    # actual ar flattening

    #calculate target AR
    #target_BPM = float(target_BPM_input.get())
    target_AR = calc_ar(1 / (target_BPM / 120), 0, 1 / (target_BPM / 120))

    # desired ar calculation method for convenice
    def calc_target_ar(page_size, page_ratio, previous_page_size):
        return round(target_AR / calc_ar(page_size, page_ratio, previous_page_size), 3)

    # loop through note_list
    for note in chart['note_list']:
        if not note['page_index'] == 0:
            page_start = pages[note['page_index']-1]['end_tick']
        else:
            page_start = 0
        page_ticks = pages[note['page_index']]['end_tick'] - page_start
        page_ratio = (note['tick'] - page_start) / page_ticks
        # page_index + 1 instead of just page_index cuz first page was duplicated
        ar = calc_target_ar(page_len_list[note['page_index']+1],
                            page_ratio,
                            page_len_list[note['page_index']])
        if ar != 1.00:
            note['approach_rate'] = ar
        else:
            if 'approach_rate' in note:
                del note['approach_rate']
        # print(page_len_list[note['page_index']+1])


def open_file():
    global chart
    global input_name
    input_name.set(filedialog.askopenfilename(
                initialdir = './',
                title = 'Select Cytus 2 file',
                filetypes = (('plain text','*.txt'),
                            ('json','*.json'),
                            ('All files','*.*'))))
    try:
        chart = json.loads(open(input_name.get(), 'r', encoding = 'utf-8').read())
    except FileNotFoundError:
        ok('File not found')
        return
    except json.JSONDecodeError:
        ok('Invalid input file')
        return
    except:
        ok('Unknown Error')
        return

def save_file():
    global chart
    try:
        output_name = filedialog.asksaveasfilename(
                initialdir = './',
                defaultextension = '.txt',
                title = 'Select output file',
                filetypes = (('plain text','*.txt'),
                            ('json','*.json'),
                            ('All files','*.*')))
        if output_name == '':
            ok('Invalid Filename')
            return

        flatten()

        output_file = open(output_name, 'w')
        output_file.write(json.dumps(chart, indent = 3))
        output_file.close()
        ok('done')
    except Exception as exception:
        ok(str(exception))
        print(str(exception))


def flattenGUI():
    global menu
    global chart
    global input_name
    global target_BPM_input

    menu = tk.Tk()
    menu.title("Brick's shitty AR flattener")

    input_name = tk.StringVar()
    input_label = tk.Entry(
        menu,
        textvariable = input_name,
        width = 30,
        relief = tk.SUNKEN,
        font = 'Arial 12'
    )
    input_label.grid(
        row = 0,
        column = 0,
        columnspan = 4,
        padx = 10,
        pady = 10
    )
    target_BPM_input = tk.StringVar()
    target_label = tk.Entry(
        menu,
        textvariable = target_BPM_input,
        width = 10,
        relief = tk.SUNKEN,
        font = 'Arial 12'
    )
    target_label.grid(
        row = 0,
        column = 4,
        columnspan = 2,
        padx = 10,
        pady = 10
    )
    open_btn = tk.Button(
        menu,
        text='Select File',
        width=10,
        height=1,
        font='Arial 10',
        command=open_file
    )
    open_btn.grid(
        row=0,
        column=7,
        padx=10,
        pady=10
    )

    def input_validity():
        if len(chart) < 2:
            return 'Invalid Chart'
        try:
            if float(target_BPM_input.get()) < 120:
                return 'Invalid Target BPM'
        except:
            return 'Invalid Target BPM'
        return 'valid'

    save_btn = tk.Button(
        menu,
        text='Flatten!',
        width=10,
        height=2,
        font='Arial 10',
        command=lambda:save_file() \
            if input_validity() == 'valid' \
            else ok(input_validity())
    )
    save_btn.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )

    menu.resizable(0, 0)
    menu.mainloop()

if __name__ == '__main__':
    flattenGUI()
