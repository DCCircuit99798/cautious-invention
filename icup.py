# import required modules
import json
import math
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import sys
from zipfile import ZipFile
import zipfile

# add modules folder to system path
sys.path.append(str(Path(os.getcwd()) / 'modules'))
sys.path.append(str(Path(os.getcwd()) / 'modules' / 'ffmpeg'))

# import third party modules
import pydub
from pydub import AudioSegment
import ffmpeg

# import custom modules
import icup_audio_pitch
import icup_chart
import icup_cmod
import icup_xmod

class App(tk.Tk):
    '''Create the main window of the program'''

    # constants for user input boundaries
    RATES_LOWER = 0.5
    RATES_UPPER = 3
    RATE_INC_LOWER = 0.01
    RATE_INC_UPPER = 0.25
    XMOD_LOWER = 0.01
    XMOD_UPPER = 4
    CMOD_LOWER = 120
    CMOD_UPPER = 500
    OUTPUT_NUM_UPPER = 20

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Idiot Caleb's Uprating Project")
        self.geometry('485x338')
        self.configure(bg='#1e2129')
        self.resizable(False, False)

        # call method to configure styles
        self.__configure_styles()

        # call method to create widgets
        self.__create_widgets()
        

    def __create_widgets(self):
        '''Creates labels, buttons, and frames to form the layout of
        the program.'''
        
        # add label for program title
        title_label = ttk.Label(
            self,
            text="Idiot Caleb's Uprating Project",
            style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3)

        # create instances of OuterFrame for other widgets to be placed in
        self.frame0 = OuterFrame(self, 0)
        self.frame1 = OuterFrame(self, 1)
        self.frame2 = OuterFrame(self, 2)

        # create border frames to contain widgets and visible frames
        self.choose_file_border = BorderFrame(self.frame0)
        self.choose_file_border.configure(style='ChooseFile.WidgetBorder.TFrame')
        self.choose_file_border.pack(
            padx=(8,0), # left padding
            pady=(0,4)) # bottom padding

        self.diffs_border = BorderFrame(self.frame0)
        self.diffs_border.configure(style='Diffs.NormalBorder.TFrame')
        self.diffs_border.pack(
            padx=(8,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space

        self.rates_border = BorderFrame(self.frame1)
        self.rates_border.configure(style='Rates.NormalBorder.TFrame')
        self.rates_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.BOTH, # take up rest of vert and horz space
            expand=True) # space in frame1 is shared between rates and rate inc

        
        self.rate_inc_border = BorderFrame(self.frame1)
        self.rate_inc_border.configure(style='RateInc.NormalBorder.TFrame')
        self.rate_inc_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.BOTH, # take up rest of vert and horz space
            expand=True) # space in frame1 is shared between rates and rate inc

        self.ar_border = BorderFrame(self.frame2)
        self.ar_border.configure(style='AR.NormalBorder.TFrame')
        self.ar_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space

        self.start_border = BorderFrame(self.frame2)
        self.start_border.configure(style='WidgetBorder.TFrame')
        self.start_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.X) # take up all horz space

        # create buttons and frames for layout of program
        self.choose_file_button = ttk.Button(
            self.choose_file_border,
            text='Choose File',
            command=self.choose_file)
        self.choose_file_button.pack(
            padx=1,
            pady=1,
            fill=tk.X) # take up all horz space
        
        self.diffs_frame = DifficultiesFrame(self.diffs_border)
        self.diffs_frame.configure(style='Normal.TFrame')
        self.diffs_frame.pack(
            padx=1, # between border frame and visible frame
            pady=1,
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space

        self.rates_frame = RatesFrame(self.rates_border)
        self.rates_frame.configure(style='Normal.TFrame')
        self.rates_frame.pack(
            padx=1,
            pady=1,
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space
        
        self.rate_inc_frame = RateIncrementFrame(self.rate_inc_border)
        self.rate_inc_frame.configure(style='Normal.TFrame')
        self.rate_inc_frame.pack(
            padx=1,
            pady=1,
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space

        self.ar_frame = AROptionsFrame(self.ar_border)
        self.ar_frame.configure(style='Normal.TFrame')
        self.ar_frame.pack(
            padx=1,
            pady=1,
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space
        
        self.start_button = ttk.Button(
            self.start_border,
            text='Start!',
            command=self.check_user_validity)
        self.start_button.pack(
            padx=1,
            pady=1,
            fill=tk.X) # take up all horz space

    def __configure_styles(self):
        '''Configures the styles of all the widgets in the program.'''
        
        # create style object for the program
        self.style = ttk.Style(self)

        # use ttk theme that allows widget background colours
        # to be changed
        self.style.theme_use('alt')

        # configure all text in the program
        self.style.configure(
            '.',
            font=('Tahoma', 12),
            foreground='#ffffff')

        # change background colour of all labels to
        # same colour as outer frames
        self.style.configure(
            'TLabel',
            background='#2d2d39')

        # title ttk label
        self.style.configure(
            'Title.TLabel',
            font=('Tahoma', 24),
            background='#1e2129')

        # heading ttk labels
        self.style.configure(
            'Heading.TLabel',
            font=('Tahoma', 8, 'bold'))

        # ttk buttons
        self.style.configure(
            'TButton',
            background='#536cde',
            borderwidth=0)
        self.style.map(
            'TButton',
            background = [('pressed', '#536cde'),
                          ('active', '#6c81d9')],
            foreground = [('pressed', '#ffffff'),
                          ('active', '#ffffff')]
            )
        
        # ttk radiobuttons
        self.style.configure(
            'TRadiobutton',
            background='#2d2d39',
            indicatorcolor='#2d2d39')
        self.style.map(
            'TRadiobutton',
            background = [('pressed', '#2d2d39'),
                          ('active', '#2d2d39')],
            foreground = [('pressed', '#ffffff'),
                          ('active', '#ffffff')],
            indicatorcolor = [('selected', '#2d2d39'),
                              ('pressed', '#2d2d39')]
            )

        # ttk comboboxes
        self.style.configure(
            'TCombobox',
            fieldbackground='#2d2d39', # bg of entry field
            selectbackground='#2d2d39', # bg of entry text when selected
            selectforeground='#ffffff', # colour of "entry" text
            background='#bac5f5' # the down button
            )
        self.style.map(
            'TCombobox',
            fieldbackground = [('pressed', '#2d2d39'),
                               ('active', '#2d2d39')],
            selectbackground = [('pressed', '#2d2d39'),
                                ('active', '#2d2d39')],
            selectforeground = [('pressed', '#ffffff'),
                                ('active', '#ffffff')],
            background = [('pressed', '#d5dbf2'),
                          ('active', '#bac5f5')]
            )

        global ttk_ar_options_combo_width
        ttk_ar_options_combo_width = 2

        # tk checkbuttons
        global tk_check_font, tk_check_bg, tk_check_activebg, tk_check_fg, \
               tk_check_activefg, tk_check_selectcolor

        tk_check_font = ('Tahoma', 12)

        tk_check_bg = '#2d2d39'
        tk_check_activebg = '#2d2d39'

        tk_check_fg = '#ffffff'
        tk_check_activefg = '#ffffff'

        tk_check_selectcolor = '#2d2d39'
        
        # tk entry fields
        global tk_entry_font, tk_entry_bg, tk_entry_fg, \
               tk_entry_borderwidth, tk_entry_insertbackground, \
               tk_rates_entry_width, tk_rate_increment_entry_width, \
               tk_ar_options_entry_width

        tk_entry_font = ('Tahoma', 12)

        tk_entry_bg = '#2d2d39'
        tk_entry_fg = '#ffffff'

        tk_entry_borderwidth = 0

        tk_entry_insertbackground = '#ffffff' # text "cursor" colour

        tk_rates_entry_width = 5 # not being used - depends on width of entry in rate inc
        tk_rate_increment_entry_width = 5
        tk_ar_options_entry_width = 5


        # tk text widgets (error messages)
        global tk_error_font, tk_error_bg, tk_error_fg, tk_error_borderwidth, \
               tk_error_state, tk_error_wrap, tk_error_height, tk_error_width

        tk_error_font = ('Tahoma', 8)

        tk_error_bg = '#2d2d39'
        tk_error_fg = '#ee9f9f'

        tk_error_borderwidth = 0

        tk_error_wrap = tk.WORD

        tk_error_width = 1 # width controlled by sticky=tk.EW within frame


        # border frames
        self.style.configure(
            'WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'NormalBorder.TFrame',
            background='#aeb9ef')

        # visible frames (that contain widgets)
        self.style.configure(
            'Normal.TFrame',
            background='#2d2d39')

        # outer invisible frames
        self.style.configure(
            'TFrame',
            background='#1e2129')

        # styles for individual borders to be configured for errors
        self.style.configure(
            'Diffs.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'Rates.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'RateInc.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'AR.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'Diffs.Required.TLabel',
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'Rates.Required.TLabel',
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'ChooseFile.WidgetBorder.TFrame',
            background='#ee9f9f')

        self.style.configure(
            'ARCombo1.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'ARCombo2.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'ARCombo3.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry1.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry2.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry3.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        # mark Cytoid level as invalid before user opens a file
        self.level_validity = False

    def choose_file(self):
        '''Allows the user to open the Cytoid level file to be
        worked with.'''

        # variable to keep track of validity of Cytoid level
        self.level_validity = True

        # open menu to let user choose file
        # and tracks the path of the chosen file
        self.user_level_path = filedialog.askopenfilename(
            initialdir = './',
            defaultextension = '*.*',
            title = 'Open a Cytoid level file',
            filetypes = (('.CYTOIDLEVEL file','*.cytoidlevel'),
                         ('.zip file','*.zip'),
                         ('All files','*.*'))
            )
        
        # display messagebox if user does not select a file
        if self.user_level_path == '':
            messagebox.showerror(
                    'Error',
                    'Please select a file'
            )

            self.level_validity = False

            # configure 'choose file' button border to red
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')

            # prevent the rest of the level validity checks
            # from running
            return

        # convert level path to Path object then to string
        # (make checks for unexpected files easier)
        self.user_level_path = str(Path(self.user_level_path))

        # if there are unexpected files in the current working
        # directory and the user chooses not to continue
        if self.unexpected_files() == False:

            # mark Cytoid level file as invalid
            self.level_validity = False

            # configure 'choose file' button border to red
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')
            
            # exit the function without extracting any files
            return

        # create list of files to delete after all files have
        # been checked
        self.files_to_delete = []

        # reset styles to default
        self.style.configure(
            'ChooseFile.WidgetBorder.TFrame',
            background='#ffffff')

        # try to open the Cytoid level file (read mode)
        try:
            with ZipFile(self.user_level_path, 'r') as level:

                # extract level.json file from Cytoid level file
                # (level.json is required for all levels)
                try:
                    level.extract('level.json')
                    self.files_to_delete.append('level.json')

                # if level.json does not exist, display error message
                # and mark Cytoid level file as invalid
                except KeyError:
                    messagebox.showerror(
                        'Error',
                        'level.json file does not exist within ' \
                        'Cytoid level file'
                    )

                    self.level_validity = False

                    # configure 'choose file' button border to red
                    self.style.configure(
                        'ChooseFile.WidgetBorder.TFrame',
                        background='#ee9f9f')

                    # prevent the rest of the level validity checks
                    # from running
                    return

        # if selected file is not a .zip file, display error
        # message and mark Cytoid level file as invalid
        except zipfile.BadZipFile:
            messagebox.showerror(
                'Error',
                'Please select a valid .zip file ' \
                '(.cytoidlevel is acceptable)'
            )

            self.level_validity = False

            # configure 'choose file' button border to red
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')

            # prevent the rest of the level validity checks
            # from running
            return
                

        # open level.json to get paths of other needed files
        try:
            with open('level.json', 'r', encoding='utf-8') as outfile:
                self.user_json = json.load(outfile)

            # check if level.json has id and title
            # (required to be able to play in-game)
            if (self.user_json['id'] in (None, '') or
                self.user_json['title'] in (None, '')):
                messagebox.showerror(
                    'Error',
                    'level.json is missing required keys ' \
                    '(id, title)'
                    )

                self.level_validity = False

                # configure 'choose file' button border to red
                self.style.configure(
                    'ChooseFile.WidgetBorder.TFrame',
                    background='#ee9f9f')

                # remove the extracted level.json file
                os.remove('level.json')

                # prevent the rest of the level validity checks
                # from running
                return

        # if level.json file is invalid JSON, display error messagebox
        # and mark Cytoid level as invalid
        except json.JSONDecodeError:
            messagebox.showerror(
                'Error',
                'level.json file within Cytoid level file is invalid'
            )

            self.level_validity = False

            # configure 'choose file' button border to red
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')

            # remove the extracted level.json file
            os.remove('level.json')

            # prevent the rest of the level validity checks
            # from running
            return

        # if level.json does not have id, title, or charts;
        # display error messagebox and mark Cytoid level as invalid
        except KeyError:
            messagebox.showerror(
                'Error',
                'level.json is missing required keys ' \
                '(id, title)'
            )

            self.level_validity = False

            # configure 'choose file' button border to red
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')

            # remove the extracted level.json file
            os.remove('level.json')

            # prevent the rest of the level validity checks
            # from running
            return

        # list of available diffs with valid music and chart files
        self.diffs_available = []

        # variable that states if Cytoid level file has music file
        self.has_music = True

        # opens the Cytoid level file in read mode
        with ZipFile(self.user_level_path, 'r') as level:

            # extract and open music file from Cytoid level file
            try:
                level.extract(self.user_json['music']['path'])
                self.files_to_delete.append(self.user_json['music']['path'])
                AudioSegment.from_file(self.user_json['music']['path'])

            # if key or audio file does not exist,
            # or audio file is invalid
            # then level file does not contain music file
            except (KeyError, IndexError, pydub.exceptions.CouldntDecodeError) as e:
                self.has_music = False

            # attempt to iterate through each diff in level.json
            try:
                for chart in self.user_json['charts']:
                    
                    # get chart
                    try:
                        level.extract(chart['path'])
                        self.files_to_delete.append(chart['path'])
                        json.loads(
                            open(chart['path'], 'r', encoding='utf-8').read())

                    # if key doesn't exist in level.json or
                    # chart file does not exist or
                    # chart file is not valid json,
                    # check next diff in level.json (this diff is invalid)
                    except (KeyError, json.JSONDecodeError) as e:
                        continue

                    # check if music_override path key exists
                    try:
                        chart['music_override']['path']

                    # if music_override path key does not exist
                    except KeyError:

                        # if there is no music,
                        # check next diff (this diff is invalid,
                        # an audio file is required)
                        if self.has_music == False:
                            continue

                        # if there is a music file and no music_override,
                        # this diff is valid
                        else:
                            self.diffs_available.append(chart['type'])

                    # get music_override
                    try:
                        level.extract(chart['music_override']['path'])
                        self.files_to_delete.append(chart['music_override']['path'])
                        AudioSegment.from_file(chart['music_override']['path'])

                        # if there is a valid music_override file,
                        # this diff is valid
                        self.diffs_available.append(chart['type'])

                    # if audio file is missing or invalid,
                    # check next diff in level.json (this diff is invalid)
                    except (KeyError, IndexError, pydub.exceptions.CouldntDecodeError) as e:
                        continue

            # if "charts" key isn't in level.json
            except KeyError:

                # display messagebox
                messagebox.showerror(
                    'Error',
                    'No charts found in level.json'
                    )

                # mark Cytoid level as invalid
                self.level_validity = False

                # configure 'choose file' button border to red
                self.style.configure(
                    'ChooseFile.WidgetBorder.TFrame',
                    background='#ee9f9f')
                
                # delete all extracted files so far
                for path in self.files_to_delete:

                    try:
                        os.remove(path)

                    # if file was already deleted,
                    # move on to text file
                    # (sometimes music and music_override
                    # paths are duplicates)
                    except FileNotFoundError:
                        pass
                
                # prevent the rest of the level validity checks
                # from running
                return
                
                        
        # if no valid diffs, display error message and mark the
        # Cytoid level file as invalid
        if self.diffs_available == []:
            messagebox.showerror(
                'Error',
                'No valid diffs within Cytoid level file - ' \
                'Your chart or audio files may be invalid. ' \
                'Are your charts in c1 format?' # speaking from epxerience...
                )

            self.level_validity = False

        # if level is valid
        if self.level_validity == True:

            # configure 'choose file' button border to white
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ffffff')

            # if difficulty not available,
            # disable the corresponding checkbutton in diffs frame
            # and deselect the difficulty

            # if difficulty is available,
            # enable the corresponding checkbutton
            if 'easy' not in self.diffs_available:
                self.diffs_frame.easy_check.configure(state='disabled')
                self.diffs_frame.easy_var.set(0)

            else:
                self.diffs_frame.easy_check.configure(state='normal')

            if 'hard' not in self.diffs_available:
                self.diffs_frame.hard_check.configure(state='disabled')
                self.diffs_frame.hard_var.set(0)

            else:
                self.diffs_frame.hard_check.configure(state='normal')

            if 'extreme' not in self.diffs_available:
                self.diffs_frame.ex_check.configure(state='disabled')
                self.diffs_frame.ex_var.set(0)

            else:
                self.diffs_frame.ex_check.configure(state='normal')
                

        # configure 'choose file' button border to red if level is invalid
        if self.level_validity == False:
            self.style.configure(
                'ChooseFile.WidgetBorder.TFrame',
                background='#ee9f9f')

        # delete extracted files after everything has been checked
        for path in self.files_to_delete:

            try:
                os.remove(path)

            # if file was already deleted, move on to text file
            # (sometimes music and music_override paths are duplicates)
            except FileNotFoundError:
                pass

    def unexpected_files(self):
        '''This function is used by the choose_file and
        check_user_validity functions to check if there are any
        unexpected files in the current working directory that may be
        overwritten and deleted when files are being worked with.'''

        # create list of expected files and directories in the
        # ICUP folder
        self.expected_files = ['icup.py',
                               'modules',
                               '.git',
                               '.gitattributes']

        # append path of chosen Cytoid level to list of
        # expected files
        self.expected_files.append(self.user_level_path)
        
        # set default confirmation value if messagebox does not appear
        # (no unexpected files)
        confirm = True

        # loop through paths of all files in current working directory
        for path in os.listdir():

            # if extra file is detected
            if path not in self.expected_files:

                # (this accounts for user_level_path being an
                # absolute path)
                if str(Path(os.getcwd()) / path) not in self.expected_files:

                    # display messagebox to confirm if user wants
                    # to continue
                    confirm = messagebox.askyesno(
                        title='Confirmation',
                        message='Extra files have been detected in ' \
                        'this folder that may be deleted or ' \
                        'overwritten when the Cytoid level file is ' \
                        'worked with. Do you wish to continue?')

                    # exit the loop so that messagebox only appears once
                    break

        # return confirmation value
        return confirm
            

    def check_user_validity(self):
        '''This function checks the validity of the user input before
        working with the necessary files.'''

        # create variables to keep track of user info
        self.user_diffs = []
        self.user_min = None
        self.user_max = None
        self.user_rate_inc = None
        self.user_ar_options = []

        # variable to keep track of validity of user input
        self.user_validity = True

        # reset styles to default
        self.style.configure(
            'Diffs.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'Diffs.Required.TLabel',
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'Rates.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'Rates.Required.TLabel',
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'RateInc.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'AR.NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'ARCombo1.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'ARCombo2.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'ARCombo3.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry1.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry2.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'AREntry3.WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        # clear all error text messages
        # allow text in error text widgets to be edited
        self.diffs_frame.error_text.configure(state='normal')
        self.rates_frame.error_text.configure(state='normal')
        self.rate_inc_frame.error_text.configure(state='normal')
        self.ar_frame.error_text1.configure(state='normal')
        self.ar_frame.error_text2.configure(state='normal')
        self.ar_frame.error_text3.configure(state='normal')
        
        # clear error message in text widgets
        self.diffs_frame.error_text.delete('1.0', tk.END)
        self.rates_frame.error_text.delete('1.0', tk.END)
        self.rate_inc_frame.error_text.delete('1.0', tk.END)
        self.ar_frame.error_text1.delete('1.0', tk.END)
        self.ar_frame.error_text2.delete('1.0', tk.END)
        self.ar_frame.error_text3.delete('1.0', tk.END)

        # prevent text from being edited
        self.diffs_frame.error_text.configure(state='disabled')
        self.rates_frame.error_text.configure(state='disabled')
        self.rate_inc_frame.error_text.configure(state='disabled')
        self.ar_frame.error_text1.configure(state='disabled')
        self.ar_frame.error_text2.configure(state='disabled')
        self.ar_frame.error_text3.configure(state='disabled')
        
        # check status of difficulty checkboxes and add
        # difficulties to the list if they are selected
        if self.diffs_frame.easy_var.get() == 1:
            self.user_diffs.append('easy')

        if self.diffs_frame.hard_var.get() == 1:
            self.user_diffs.append('hard')

        if self.diffs_frame.ex_var.get() == 1:
            self.user_diffs.append('extreme')

        # if no difficulties are selected (invalid)
        if self.user_diffs == []:

            # display error message
            # configure diffs frame styles
            # mark user input as invalid
            self.diffs_error(
                'At least one difficulty must be selected'
                )

        # get value of minimum and maximum rates
        try:
            self.user_min = float(self.rates_frame.min_var.get())
            self.user_max = float(self.rates_frame.max_var.get())

            # if rates are less than 0.1 or more than 3 (invalid)
            if (self.user_min < self.RATES_LOWER or
                self.user_min > self.RATES_UPPER or
                self.user_max < self.RATES_LOWER or
                self.user_max > self.RATES_UPPER):

                # display error message
                # configure rates frame styles
                # mark user input as invalid
                self.rates_error(
                    'Rates must be between {} and {} ' \
                    '(inclusive)'.format(self.RATES_LOWER, self.RATES_UPPER)
                    )

            # if maximum rate less than minimum rate (invalid)
            elif self.user_max < self.user_min:

                # display error message
                # configure rates frame styles
                # mark user input as invalid
                self.rates_error(
                    'Maximum rate cannot be less than minimum'
                    )

        # if entry fields are empty (invalid)
        except ValueError:

            # display error message
            # configure rates frame styles
            # mark user input as invalid
            self.rates_error('Rates must be valid numbers')

        # if custom increment is selected, get value from entry field
        if self.rate_inc_frame.var.get() == 'Custom':
            try:
                self.user_rate_inc = float(self.rate_inc_frame.custom_var.get())

                # if rate increment less than 0.01 or more than 0.25
                # (invalid)
                if (self.user_rate_inc < self.RATE_INC_LOWER or
                    self.user_rate_inc > self.RATE_INC_UPPER):

                    # display error message
                    # configure rate inc frame style
                    # mark user input as invalid
                    self.rate_inc_error(
                        'Rate increment must be between {} and {} ' \
                        '(inclusive)'.format(self.RATE_INC_LOWER, self.RATE_INC_UPPER)
                        )

            # if input is not valid number (invalid)
            except ValueError:

                # display error message
                # configure rate inc frame style
                # mark user input as invalid
                self.rate_inc_error(
                    'Rate increment must be a valid number'
                    )

        # otherwise get rate increment from radio buttons
        else:
            self.user_rate_inc = float(self.rate_inc_frame.var.get())

        # loop through comboboxes and entry fields from AR options frame
        for i in range(0, len(self.ar_frame.user_input_list)):
        
            # if type and/or value are inputted, perform validity checks
            if (self.ar_frame.user_input_list[i][0].get() != '' or # type
                self.ar_frame.user_input_list[i][1].get() != ''): # value

                # get AR type
                self.user_ar_type = self.ar_frame.user_input_list[i][0].get()

                # if AR type is not filled out (invalid)
                if self.user_ar_type == '':
                    
                    # display error message
                    # configure AR border frame colour
                    # mark user input as invalid
                    self.ar_error(
                        i+1,
                        'Both AR type and value must be filled in')

                    # configure the combobox that corresponds to the
                    # invalid AR option
                    self.ar_error_combo(i+1)

                # if AR type is filled, check value
                else:
                    try:
                        # get AR value
                        self.user_ar_value = float(self.ar_frame.user_input_list[i][1].get())
                        
                        # xmod value must be between 0.001 and 4 (inclusive)
                        if (self.user_ar_type == 'x' and
                            (self.user_ar_value < self.XMOD_LOWER or
                            self.user_ar_value > self.XMOD_UPPER)):

                            # display error message
                            # configure AR border frame colour
                            # mark user input as invalid
                            self.ar_error(
                                i+1,
                                'xmod value must be between ' \
                                '{} and {} ' \
                                '(inclusive)'.format(self.XMOD_LOWER, self.XMOD_UPPER))
                        
                            # configure entry that corresponds to the
                            # invalid AR option
                            self.ar_error_entry(i+1)

                        # cmod value must be between 120 and 500 (inclusive)
                        # for all rates (lowercase c scales with rates)
                        elif (self.user_ar_type == 'c' and
                            (self.user_min * self.user_ar_value < self.CMOD_LOWER or
                            self.user_max * self.user_ar_value > self.CMOD_UPPER)):

                            # display error message
                            # configure AR border frame colour
                            # mark user input as invalid
                            self.ar_error(
                                i+1,
                                'cmod value must be between ' \
                                '{} and {} ' \
                                '(inclusive) for all rates'.format(self.CMOD_LOWER, self.CMOD_UPPER))

                            # configure entry that corresponds to the
                            # invalid AR option
                            self.ar_error_entry(i+1)

                        # Cmod value must be between 120 and 500
                        elif (self.user_ar_type == 'C' and
                            (self.user_ar_value < self.CMOD_LOWER or
                            self.user_ar_value > self.CMOD_UPPER)):

                            # display error message
                            # configure AR border frame colour
                            # mark user input as invalid
                            self.ar_error(
                                i+1,
                                'Cmod value must be between ' \
                                '{} and {} (inclusive)'.format(self.CMOD_LOWER, self.CMOD_UPPER))

                            # configure entry that corresponds to the
                            # invalid AR option
                            self.ar_error_entry(i+1)

                        # if value passed all validity checks
                        else:

                            # append AR option to list
                            self.user_ar_options.append(
                                [self.user_ar_type,
                                 self.user_ar_value]
                                )

                    # if value is not valid number (invalid)
                    except ValueError:

                        # if value is completely empty
                        if self.ar_frame.user_input_list[i][1].get() == '':

                            # display error message
                            # configure AR border frame colour
                            # mark user input as invalid
                            self.ar_error(
                                i+1,
                                'Both AR type and value must be filled in')

                            # configure entry that corresponds to the
                            # invalid AR option
                            self.ar_error_entry(i+1)

                        # if value is not empty,
                        # but still an invalid number
                        else:

                            # display error message
                            # configure AR border frame colour
                            # mark user input as invalid
                            self.ar_error(
                                i+1,
                                'AR value must be a valid number')

                            # configure entry that corresponds to the
                            # invalid AR option
                            self.ar_error_entry(i+1)

                    # TypeError occurs when cmod is selected
                    # and rates aren't filled out

                    # rates have validity check anyway,
                    # so no action needed
                    except TypeError:
                        pass

        # display error messagebox if Cytoid level is invalid
        if self.level_validity == False:
            messagebox.showerror(
                'Error',
                'Please select a valid Cytoid level file'
                )

        # call function to work with necessary files if both
        # user input and Cytoid level file are valid and
        # unexpected_files and output_num_check functions return True
        elif (self.level_validity == True
              and self.user_validity == True
              and self.unexpected_files() == True
              and self.output_num_check() == True):
            self.work_with_files()

    def output_num_check(self):
        '''This function calculates the total number of Cytoid levels
        that will be created according to the user input, and warns
        the user if more than 20 levels will be created.
        '''

        # calculate total number of rates that are looped through
        total_rates = (self.user_max - self.user_min) / self.user_rate_inc + 1

        # round to eliminate round-off errors from working with floats
        # then round down to nearest integer
        total_rates = math.floor(round(total_rates, 8))

        # calculate total levels
        total_levels = total_rates * len(self.user_diffs)

        # set default confirmation value if messagebox does not appear
        # (i.e. number of levels created will be 20 or fewer)
        confirm = True

        # if more than 20 levels will be created
        if total_levels > self.OUTPUT_NUM_UPPER:

            # display messagebox to confirm to the user if they want
            # to continue
            confirm = messagebox.askyesno(
                title='Warning',
                message='You are about to create ' \
                        '{} new Cytoid level files. ' \
                        'Do you wish to continue?'.format(total_levels))

        return confirm


    def diffs_error(self, message):
        '''Updates styles of difficulties frame (border and
        "required" label), displays error message in text widget,
        and marks user input as invalid.'''
        
        # allow text inside error widget to be edited
        self.diffs_frame.error_text.configure(state='normal')

        # clear any text inside error widget
        self.diffs_frame.error_text.delete('1.0', tk.END)

        # insert error message (line 1, character 0)
        self.diffs_frame.error_text.insert(
            '1.0', message)

        # prevent text from being edited
        self.diffs_frame.error_text.configure(state='disabled')

        # configure styles
        self.style.configure(
            'Diffs.NormalBorder.TFrame',
            background='#ee9f9f')

        self.style.configure(
            'Diffs.Required.TLabel',
            foreground='#ee9f9f',
            font=('Tahoma', 8, 'bold'))

        # indicate that user input is invalid
        self.user_validity = False


    def rates_error(self, message):
        '''Updates styles of rates frame (border and
        "required" label), displays error message in text widget,
        and marks user input as invalid.'''

        # allow text inside error widget to be edited
        self.rates_frame.error_text.configure(state='normal')

        # clear any text inside error widget
        self.rates_frame.error_text.delete('1.0', tk.END)

        # insert error message (line 1, character 0)
        self.rates_frame.error_text.insert(
            '1.0', message)

        # prevent text from being edited
        self.rates_frame.error_text.configure(state='disabled')

        # configure styles
        self.style.configure(
            'Rates.NormalBorder.TFrame',
            background='#ee9f9f',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'Rates.Required.TLabel',
            foreground='#ee9f9f',
            font=('Tahoma', 8, 'bold'))

        # indicated that user input is invalid
        self.user_validity = False


    def rate_inc_error(self, message):
        '''Updates styles of rate increment frame,
        displays error message in text widget,
        and marks user input as invalid.'''
        
        # allow text inside error widget to be edited
        self.rate_inc_frame.error_text.configure(state='normal')

        # clear any text inside error widget
        self.rate_inc_frame.error_text.delete('1.0', tk.END)

        # insert error message (line 1, character 0)
        self.rate_inc_frame.error_text.insert(
            '1.0', message)

        # prevent text from being edited
        self.rate_inc_frame.error_text.configure(state='disabled')

        # configure styles
        self.style.configure(
            'RateInc.NormalBorder.TFrame',
            background='#ee9f9f',
            font=('Tahoma', 8, 'bold'))

        # indicate that user input is invalid
        self.user_validity = False
        

    def ar_error(self, index, message):
        '''Updates border colour of AR options frame,
        displays error message for an AR option in the first
        available text widget, and marks user input as invalid.'''
        
        # configure styles
        self.style.configure(
            'AR.NormalBorder.TFrame',
            background='#ee9f9f')

        # display error message in first text widget if it is empty
        if self.ar_frame.error_text1.get('1.0', 'end-1c') == '':

            # allow text inside error widget to be edited
            self.ar_frame.error_text1.configure(state='normal')

            # clear any text inside error widget
            self.ar_frame.error_text1.delete('1.0', tk.END)

            # insert error message
            self.ar_frame.error_text1.insert(
                '1.0',
                'AR Option #{}: {}'.format(index, message))

            # prevent text from being edited
            self.ar_frame.error_text1.configure(state='disabled')

        # if first text widget is already filled,
        # display errors in second text widget if it is empty
        elif self.ar_frame.error_text2.get('1.0', 'end-1c') == '':

            # allow text inside error widget to be edited
            self.ar_frame.error_text2.configure(state='normal')

            # clear any text inside error widget
            self.ar_frame.error_text2.delete('1.0', tk.END)

            # insert error message
            self.ar_frame.error_text2.insert(
                '1.0',
                'AR Option #{}: {}'.format(index, message))

            # prevent text from being edited
            self.ar_frame.error_text2.configure(state='disabled')

        # if both the first and second text widgets are filled,
        # display error messages in the third text widget
        else:
            
            # allow text inside error widget to be edited
            self.ar_frame.error_text3.configure(state='normal')

            # clear any text inside error widget
            self.ar_frame.error_text3.delete('1.0', tk.END)

            # insert error message
            self.ar_frame.error_text3.insert(
                '1.0',
                'AR Option #{}: {}'.format(index, message))

            # prevent text from being edited
            self.ar_frame.error_text3.configure(state='disabled')

        # indicate that user input is invalid
        self.user_validity = False
            

    def ar_error_combo(self, index):
        '''Updates style of combobox borders if user inputs
        invalid data.'''

        if index == 1:
            self.style.configure(
                'ARCombo1.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')

        elif index == 2:
            self.style.configure(
                'ARCombo2.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')

        else:
            self.style.configure(
                'ARCombo3.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')

    def ar_error_entry(self, index):
        '''Updates style of entry field borders if user inputs
        invalid data.'''

        if index == 1:
            self.style.configure(
                'AREntry1.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')

        elif index == 2:
            self.style.configure(
                'AREntry2.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')

        else:
            self.style.configure(
                'AREntry3.WidgetBorder.TFrame',
                background='#ee9f9f',
                relief='flat')
            

    def work_with_files(self):
        '''This function starts working with files and creating
        new levels once the Cytoid level file and user input have
        been marked as valid.'''

        # create list of files to delete after all new levels have
        # been created
        self.files_to_delete = []

        # extract level.json file from Cytoid level file
        with ZipFile(self.user_level_path, 'r') as level:
            level.extract('level.json')

        # delete beta.level.json if it exists
        try:
            os.remove('beta.level.json')

        except FileNotFoundError:
            pass

        # rename level.json file
        os.rename('level.json', 'beta.level.json')

        # add beta.level.json to list of files to delete
        self.files_to_delete.append('beta.level.json')

        # open beta.level.json to get paths of other needed files
        self.user_json = json.load(open(
            'beta.level.json',
            'r',
            encoding='utf-8')
            )

        try:
            
            # try to extract music file
            with ZipFile(self.user_level_path, 'r') as level:
                level.extract(self.user_json['music']['path'])

            # store path of file
            self.music_path = self.user_json['music']['path']

            # add file path to list of files to delete
            self.files_to_delete.append(self.user_json['music']['path'])

        # if no key in level.json or file doesn't exist,
        # skip this step and extract music_override instead
        except KeyError:
            self.music_path = None

        try:
            
            # try to extract music preview file
            with ZipFile(self.user_level_path, 'r') as level:
                level.extract(self.user_json['music_preview']['path'])

            # store path of file
            self.preview_path = self.user_json['music_preview']['path']

            # add file path to list of files to delete
            self.files_to_delete.append(self.user_json['music_preview']['path'])

        # if no key in level.json or file doesn't exist,
        # skip this step
        except KeyError:
            self.preview_path = None

        try:

            # try to extract background file
            with ZipFile(self.user_level_path, 'r') as level:
                level.extract(self.user_json['background']['path'])

            # store path of file
            self.background_path = self.user_json['background']['path']

            # add file path to list of files to delete
            self.files_to_delete.append(self.user_json['background']['path'])

        # if no key in level.json or file doesn't exist,
        # skip this step
        except KeyError:
            self.background_path = None

        # loop through each difficulty selected by the user
        for diff in self.user_diffs:

            # start at minimum rate chosen by user
            self.current_rate = self.user_min

            # loop through rates between chosen min and max rate
            while self.current_rate <= self.user_max:

                # create list of files to
                # delete after a single new level
                # has been created
                self.output_level_files = []

                # open beta.level.json to work with and update metadata
                self.output_json = json.load(open(
                    'beta.level.json',
                    'r',
                    encoding='utf-8')
                    )

                # add rate to level id, separated by an underscore
                self.output_json['id'] \
                = \
                (self.output_json['id']
                 + '_'
                 + diff
                 + '_'
                 + str(self.current_rate)
                 + 'x')

                # add rate to title inside existing square brackets 
                if self.square_brackets(self.output_json['title']) == True:
                    self.output_json['title'] \
                    = \
                    (self.output_json['title'][:-1]
                     + ': '
                     + diff.capitalize()
                     + ' '
                     + str(self.current_rate)
                     + 'x]')

                # add rate to title in new square brackets
                # (if title doesn't have them)
                else:
                    self.output_json['title'] \
                    = \
                    (self.output_json['title']
                     + ' ['
                     + diff.capitalize()
                     + ' '
                     + str(self.current_rate)
                     + 'x]')

                # add rate to title_localized inside existing square brackets
                try: 
                    if self.square_brackets(self.output_json['title_localized']) == True:
                        self.output_json['title_localized'] \
                        = \
                        (self.output_json['title_localized'][:-1]
                         + ': '
                         + diff.capitalize()
                         + ' '
                         + str(self.current_rate)
                         + 'x]')
                        
                    # add rate to title_localized in new square brackets
                    # if title_localized doesn't have them
                    
                    # (skip this step if title_localized
                    # is an empty string)
                    elif self.output_json['title_localized'] != '':
                        self.output_json['title_localized'] \
                         = \
                         (self.output_json['title_localized']
                          + ' ['
                          + diff.capitalize()
                          + ' '
                          + str(self.current_rate)
                          + 'x]')

                # if the chart has no title_localized or
                # title_localized is set to null, skip this step
                except (KeyError, TypeError) as e:
                    pass

                # delete all chart objects in output json file
                # (chart objects will be created with updated metadata
                # after files have been worked with)
                for i in range(0, len(self.output_json['charts'])):
                    del self.output_json['charts'][0]

                # loop through charts in level.json to find and
                # work with chart and music override files for a
                # specific difficulty
                for chart in self.user_json['charts']:

                    if chart['type'] == diff:

                        # extract chart file
                        with ZipFile(self.user_level_path, 'r') as level:
                            level.extract(chart['path'])

                        # store path of file
                        self.chart_path = chart['path']

                        # add chart path to list of files to delete
                        self.files_to_delete.append(chart['path'])

                        # work with chart file
                        icup_chart.create_file(
                            self.chart_path,
                            self.current_rate
                            )

                        # store output name of new chart file
                        # (file is worked with further if user has
                        # selected AR options)
                        self.rate_chart_path = icup_chart.get_output_name(
                            self.chart_path,
                            self.current_rate
                            )

                        # try working with music_override file
                        try:

                            # try to extract music_override file
                            with ZipFile(self.user_level_path, 'r') as level:
                                level.extract(chart['music_override']['path'])

                            # store path of file
                            self.override_path = chart['music_override']['path']

                            # add file path to list of files to delete
                            self.files_to_delete.append(chart['music_override']['path'])

                            # work with music_override file (if it exists)
                            icup_audio_pitch.create_file(
                                self.override_path,
                                self.current_rate
                                )

                            # add the output file to list of files to
                            # delete after level is created
                            self.output_level_files.append(
                                icup_audio_pitch.get_output_name(
                                    self.override_path,
                                    self.current_rate
                                    ))

                            # music key may need to be created
                            # (not required if music_override is valid)
                            self.output_json['music'] = {}
                            
                            # add path of new music_override file
                            # to level.json
                            self.output_json['music']['path'] \
                            = \
                            icup_audio_pitch.get_output_name(
                                    self.override_path,
                                    self.current_rate
                                    )

                        # if no key in level.json or file doesn't exist,
                        # work with music file
                        except (KeyError, FileNotFoundError) as e:
                            
                            # work with music file
                            icup_audio_pitch.create_file(
                                self.music_path,
                                self.current_rate
                                )

                            # add the output file to list of files to
                            # delete after level is created
                            self.output_level_files.append(
                                icup_audio_pitch.get_output_name(
                                    self.music_path,
                                    self.current_rate
                                    ))

                            # add path of new music file
                            # to level.json
                            self.output_json['music']['path'] \
                            = \
                            icup_audio_pitch.get_output_name(
                                    self.music_path,
                                    self.current_rate
                                    )

                        # work with music_preview file if it exists
                        if self.preview_path != None:
                            
                            # try working with music_preview file
                            try:

                                # work with music_preview file
                                icup_audio_pitch.create_file(
                                    self.preview_path,
                                    self.current_rate
                                    )

                                # add the output file to list of files to
                                # delete after level is created
                                self.output_level_files.append(
                                    icup_audio_pitch.get_output_name(
                                        self.preview_path,
                                        self.current_rate
                                        ))

                                # add path of new music file
                                # to level.json
                                self.output_json['music_preview']['path'] \
                                = \
                                icup_audio_pitch.get_output_name(
                                        self.preview_path,
                                        self.current_rate
                                        )

                            # if music_preview file is an invalid
                            # audio file, the key must
                            # be deleted from level.json
                            except (IndexError, pydub.exceptions.CouldntDecodeError) as e:
                                del self.output_json['music_preview']
                        
                # if user has not selected any AR options
                if self.user_ar_options == []:
                    
                    # add the output file to list of files to
                    # delete after level is created
                    self.output_level_files.append(
                        self.rate_chart_path)

                    # (if user has selected AR options,
                    # chart file will be deleted separately to
                    # prevent it from being written to the Cytoid
                    # output file)

                    # add chart object to charts in output level.json
                    self.output_json['charts'].append({
                        'type': 'extreme',
                        'difficulty': 0,
                        'path': self.rate_chart_path
                        })

                # create list of diffs to output the charts to
                # (if AR options have been selected)
                self.output_diffs = []

                # adds diffs to self.output_diffs starting
                # from extreme (extreme is often seen as the 'default'
                # difficulty by players)
                for i in range(0, len(self.user_ar_options)):

                    if i == 0:
                        self.output_diffs.insert(0, 'extreme')
                    
                    if i == 1:
                        self.output_diffs.insert(0, 'hard')
                    
                    if i == 2:
                        self.output_diffs.insert(0, 'easy')

                # loop through AR options chosen by the user
                for i in range(0, len(self.user_ar_options)):

                    # if AR type is xmod
                    if self.user_ar_options[i][0] == 'x':

                        # create AR name for output difficulty
                        self.ar_name \
                        = \
                        ('AR x'
                         + str(self.user_ar_options[i][1])
                         )
                        
                        # work with chart file using xmod module
                        icup_xmod.create_file(
                            self.rate_chart_path,
                            self.user_ar_options[i][1] # ar value
                            )

                        # add the output file to list of files to
                        # delete after level is created
                        self.output_level_files.append(
                            icup_xmod.get_output_name(
                                self.rate_chart_path,
                                self.user_ar_options[i][1]
                            ))

                        # add chart object to charts in output level.json
                        self.output_json['charts'].append({
                            'type': self.output_diffs[i],
                            'name': self.ar_name,
                            'difficulty': 0,
                            'path': icup_xmod.get_output_name(
                                self.rate_chart_path,
                                self.user_ar_options[i][1])
                            })

                    # if AR type is cmod (scales with rates)
                    if self.user_ar_options[i][0] == 'c':

                        # create AR name for output difficulty
                        self.ar_name \
                        = \
                        ('AR C'
                         + str(round((self.user_ar_options[i][1] * self.current_rate), 8))
                         )

                        # work with chart file using xmod module
                        icup_cmod.create_file(
                            self.rate_chart_path,
                            round((self.user_ar_options[i][1] * self.current_rate), 8)
                            )

                        # add the output file to list of files to
                        # delete after level is created
                        self.output_level_files.append(
                            icup_cmod.get_output_name(
                                self.rate_chart_path,
                                round((self.user_ar_options[i][1] * self.current_rate), 8)
                            ))

                        # add chart object to charts in output level.json
                        self.output_json['charts'].append({
                            'type': self.output_diffs[i],
                            'name': self.ar_name,
                            'difficulty': 0,
                            'path': icup_cmod.get_output_name(
                                self.rate_chart_path,
                                round((self.user_ar_options[i][1] * self.current_rate), 8))
                            })

                    # if AR type is Cmod (does not scale with rates)
                    if self.user_ar_options[i][0] == 'C':

                        # create AR name for output difficulty
                        self.ar_name \
                        = \
                        ('AR C'
                         + str(self.user_ar_options[i][1])
                         )

                        # work with chart file using xmod module
                        icup_cmod.create_file(
                            self.rate_chart_path,
                            self.user_ar_options[i][1] # ar value
                            )

                        # add the output file to list of files to
                        # delete after level is created
                        self.output_level_files.append(
                            icup_cmod.get_output_name(
                                self.rate_chart_path,
                                self.user_ar_options[i][1]
                            ))

                        # add chart object to charts in output level.json
                        self.output_json['charts'].append({
                            'type': self.output_diffs[i],
                            'name': self.ar_name,
                            'difficulty': 0,
                            'path': icup_cmod.get_output_name(
                                self.rate_chart_path,
                                self.user_ar_options[i][1])
                            })

                

                # create level.json for output Cytoid level file
                with open('level.json', 'w', encoding='utf-8') as output_file:
                    json.dump(
                        self.output_json,
                        output_file,
                        indent=3,
                        ensure_ascii=False
                        )

                # add level.json to list of files
                # for output Cytoid level file
                self.output_level_files.append('level.json')

                # delete output chart from icup_chart if
                # AR options were selected
                if self.user_ar_options != []:
                    os.remove(self.rate_chart_path)

                # get index of the last dot in
                # filename of Cytoid level file
                self.last_dot = self.user_level_path.rfind('.')

                # create output name by putting the diff and rate
                # in between the filename and the extension
                self.output_name = (self.user_level_path[:self.last_dot]
                       + '_'
                       + diff
                       + '_'
                       + str(self.current_rate)
                       + 'x'
                       + self.user_level_path[self.last_dot:])

                # open the output Cytoid level file
                with ZipFile(self.output_name, 'w') as level:

                    # send background file to the output Cytoid
                    # level file (if it exists)
                    if self.background_path != None:
                        level.write(self.background_path)

                    # after all files have been worked with
                    for path in self.output_level_files:

                        try:

                            # send all necessary files to
                            # the output Cytoid level file
                            level.write(path)
                            
                            # delete files
                            os.remove(path)

                        # if file was already deleted due to
                        # AR options being the same, delete next file
                        except FileNotFoundError:
                            pass

                print(self.output_name)
                
                # increase current rate by chosen rate increment
                self.current_rate += self.user_rate_inc

                # round to eliminate round-off errors from
                # addition of floats
                self.current_rate = round(self.current_rate, 8)

        # once all output Cytoid levels have been created,
        # delete all of the original files extracted from the
        # Cytoid level file opened by the user
        for path in self.files_to_delete:

            try:
                os.remove(path)

            # if file was already deleted, move on to text file
            # (sometimes music and music_override paths are duplicates)
            except FileNotFoundError:
                pass


    def square_brackets(self, string):
        '''The function checks if the title or title_localized fields
        in a level.json file have square brackets. Square brackets are
        a convention used by some charters that include information
        describing the chart(s), and is not considered part of the
        song title. If square brackets are detected in the song title,
        the rate will be inserted inside the square brackets instead
        of being appended at the end of the title.
        '''
        
        if '[' in string and string.endswith(']'):
            return True
        else:
            return False


    def add_ar_chart(self, index):
        '''This function adds a chart object with the path of the
        chart file and the correct type (easy, hard, extreme) to the
        output level.json file.
        '''

class OuterFrame(ttk.Frame):
    '''This class creates invisible frames for the buttons and visible
    frames to be placed in.'''
    
    def __init__(self, container, frame_number):
        super().__init__(container)

        # place frame on grid according to frame_number argument
        self.grid(row=1,
                  column=frame_number,
                  sticky=tk.NS) # stretch to fill up all vertical space


class BorderFrame(ttk.Frame):
    '''This class creates frames to act as borders for widgets.'''

    def __init__(self, container):
        super().__init__(container)


class DifficultiesFrame(ttk.Frame):
    '''Visible "difficulties" frame'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()
        
    def __create_widgets(self):
        '''Create necessary widgets within frame'''

        # makes column 0 fill up available horizontal space
        self.columnconfigure(0, weight=1)

        # labels
        self.heading_label = ttk.Label(
            self,
            text='DIFFICULTIES',
            style='Heading.TLabel')
        self.heading_label.grid(
            row=0,
            column=0,
            padx=(5,0), # left padding
            pady=(5,0), # top padding
            sticky=tk.W)

        self.required_label = ttk.Label(
            self,
            text='*Required',
            style='Diffs.Required.TLabel')
        self.required_label.grid(
            row=1,
            column=0,
            padx=(5,0), # left padding
            pady=(0,5), # bottom padding
            sticky=tk.W)

        # variables to store state of checkboxes
        self.easy_var = tk.IntVar()
        self.hard_var = tk.IntVar()
        self.ex_var = tk.IntVar()

        # set value of checkbox variables to 0 (off)
        self.easy_var.set(0)
        self.hard_var.set(0)
        self.ex_var.set(0)

        # checkboxes
        self.easy_check = tk.Checkbutton(
            self,
            text='Easy',
            variable=self.easy_var)
        self.easy_check.configure(
            font=tk_check_font,
            background=tk_check_bg,
            activebackground=tk_check_activebg,
            foreground=tk_check_fg,
            activeforeground=tk_check_activefg,
            selectcolor=tk_check_selectcolor)
        self.easy_check.grid(
            row=2,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W
            )
                                                  
        self.hard_check = tk.Checkbutton(
            self,
            text='Hard',
            variable=self.hard_var)
        self.hard_check.configure(
            font=tk_check_font,
            background=tk_check_bg,
            activebackground=tk_check_activebg,
            foreground=tk_check_fg,
            activeforeground=tk_check_activefg,
            selectcolor=tk_check_selectcolor)
        self.hard_check.grid(
            row=3,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W
            )

        self.ex_check = tk.Checkbutton(
            self,
            text='Extreme',
            variable=self.ex_var)
        self.ex_check.configure(
            font=tk_check_font,
            background=tk_check_bg,
            activebackground=tk_check_activebg,
            foreground=tk_check_fg,
            activeforeground=tk_check_activefg,
            selectcolor=tk_check_selectcolor)
        self.ex_check.grid(
            row=4,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W
            )

        # text box to display error messages
        self.error_text = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=5,
            width=tk_error_width
            )
        self.error_text.grid(
            row=5,
            column=0,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )

class RatesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):
        '''Create necessary widgets within frame'''

        # makes column 1 fill up available horizontal space
        self.columnconfigure(1, weight=1)

        # labels
        self.heading_label = ttk.Label(
            self,
            text='RATES',
            style='Heading.TLabel')
        self.heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(5,0), # top padding
            sticky=tk.W)

        self.required_label = ttk.Label(
            self,
            text='*Required',
            style='Rates.Required.TLabel')
        self.required_label.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(0,3), # bottom padding
            sticky=tk.W)

        self.min_label = ttk.Label(self, text='Minimum')
        self.min_label.grid(
            row=2,
            column=0,
            padx=(5,0), # left padding
            pady=(1,1), # top/bottom padding
            sticky=tk.W)

        self.max_label = ttk.Label(self, text='Maximum')
        self.max_label.grid(
            row=3,
            column=0,
            padx=(5,0), # left padding
            pady=(1,5), # top/bottom padding
            sticky=tk.W)

        # variables to store text in entry fields
        self.min_var = tk.StringVar()
        self.max_var = tk.StringVar()

        # borders for entry fields
        self.min_border = BorderFrame(self)
        self.min_border.configure(style='WidgetBorder.TFrame')
        self.min_border.grid(
            row=2,
            column=1,
            padx=(0,5), # right padding
            pady=(1,1), # top/bottom padding
            sticky=tk.EW
            )

        self.max_border = BorderFrame(self)
        self.max_border.configure(style='WidgetBorder.TFrame')
        self.max_border.grid(
            row=3,
            column=1,
            padx=(0,5), # right padding
            pady=(1,5), # top/bottom padding
            sticky=tk.EW
            )

        # entry fields
        self.min_entry = tk.Entry(
            self.min_border,
            textvariable=self.min_var)
        self.min_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=1 # width depends on length of rate inc frame (fill=tk.X)
            )
        self.min_entry.pack(padx=1, pady=1, fill=tk.X)

        self.max_entry = tk.Entry(
            self.max_border,
            textvariable=self.max_var)
        self.max_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=1 # width depends on length of rate inc frame (fill=tk.X)
            )
        self.max_entry.pack(padx=1, pady=1, fill=tk.X)

        self.error_text = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=2,
            width=tk_error_width
            )
        self.error_text.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )


class RateIncrementFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):
        '''Create necessary widgets within frame'''

        # labels
        self.heading_label = ttk.Label(
            self,
            text='RATE INCREMENT',
            style='Heading.TLabel')
        self.heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(5,5), # top padding
            sticky=tk.W)

        # variable to store selected rate increment
        self.var = tk.StringVar()

        
        # radio buttons
        self.radio1 = ttk.Radiobutton(
            self,
            text='0.05',
            value=0.05,
            variable=self.var)

        self.radio2 = ttk.Radiobutton(
            self,
            text='0.10',
            value=0.10,
            variable=self.var)

        self.radio3 = ttk.Radiobutton(
            self,
            text='Custom:',
            value='Custom',
            variable=self.var)

        self.radio1.grid(
            row=1,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W)
        self.radio2.grid(
            row=2,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W)
        self.radio3.grid(
            row=3,
            column=0,
            padx=(5,0), # left padding
            sticky=tk.W)

        # set default value of rate increment to 0.05
        self.var.set(0.05)

        # border for custom entry field
        self.entry_border = BorderFrame(self)
        self.entry_border.configure(style='WidgetBorder.TFrame')
        self.entry_border.grid(
            row=3,
            column=1,
            padx=(0,5), # right padding
            pady=(0,5) # bottom padding
            )
        
        # variable to store custom rate increment in entry field
        self.custom_var = tk.StringVar()

        # entry field for custom rate increment
        self.custom_entry = tk.Entry(
            self.entry_border,
            textvariable=self.custom_var)
        self.custom_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_rate_increment_entry_width)
        self.custom_entry.pack(padx=1, pady=1)

        # text box to display error messages
        self.error_text = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=3,
            width=tk_error_width
            )
        self.error_text.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )

class AROptionsFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):
        '''Create necessary widgets within frame'''

        # makes column 3 fill up available horizontal space
        self.columnconfigure(3, weight=1)

        # labels
        self.heading_label = ttk.Label(
            self,
            text='AR OPTIONS',
            style='Heading.TLabel')
        self.heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(5,5), # top/bottom padding
            sticky=tk.W
            )
        
        self.label1 = ttk.Label(self, text='AR Option #1:')
        self.label2 = ttk.Label(self, text='AR Option #2:')
        self.label3 = ttk.Label(self, text='AR Option #3:')

        self.label1.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(1,1), # top/bottom padding
            sticky=tk.W
            )
        
        self.label2.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(1,1), # top/bottom padding
            sticky=tk.W
            )
        
        self.label3.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=(5,0), # left padding
            pady=(1,1), # top/bottom padding
            sticky=tk.W
            )

        # variables to store selected AR type and value
        # for each of the three options
        self.type1 = tk.StringVar()
        self.type2 = tk.StringVar()
        self.type3 = tk.StringVar()

        self.value1 = tk.StringVar()
        self.value2 = tk.StringVar()
        self.value3 = tk.StringVar()

        # borders for comboboxes (dropdown menus)
        self.comboborder1 = BorderFrame(self)
        self.comboborder2 = BorderFrame(self)
        self.comboborder3 = BorderFrame(self)

        self.comboborder1.configure(style='ARCombo1.WidgetBorder.TFrame')
        self.comboborder2.configure(style='ARCombo2.WidgetBorder.TFrame')
        self.comboborder3.configure(style='ARCombo3.WidgetBorder.TFrame')

        self.comboborder1.grid(
            row=1,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )
        
        self.comboborder2.grid(
            row=2,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )
        
        self.comboborder3.grid(
            row=3,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )

        # comboboxes (dropdown menus)
        self.combo1 = ttk.Combobox(
            self.comboborder1,
            textvariable=self.type1,
            width=ttk_ar_options_combo_width)
        self.combo2 = ttk.Combobox(
            self.comboborder2,
            textvariable=self.type2,
            width=ttk_ar_options_combo_width)
        self.combo3 = ttk.Combobox(
            self.comboborder3,
            textvariable=self.type3,
            width=ttk_ar_options_combo_width)

        self.combo1.pack(padx=1, pady=1)
        self.combo2.pack(padx=1, pady=1)
        self.combo3.pack(padx=1, pady=1)

        # define possible values for comboboxes
        self.combo1['values'] = ('', 'x', 'c', 'C')
        self.combo2['values'] = ('', 'x', 'c', 'C')
        self.combo3['values'] = ('', 'x', 'c', 'C')

        # prevent user from entering a custom value in the comboboxes
        self.combo1['state'] = 'readonly'
        self.combo2['state'] = 'readonly'
        self.combo3['state'] = 'readonly'

        # borders for entry fields
        self.entryborder1 = BorderFrame(self)
        self.entryborder2 = BorderFrame(self)
        self.entryborder3 = BorderFrame(self)

        self.entryborder1.configure(style='AREntry1.WidgetBorder.TFrame')
        self.entryborder2.configure(style='AREntry2.WidgetBorder.TFrame')
        self.entryborder3.configure(style='AREntry3.WidgetBorder.TFrame')

        self.entryborder1.grid(
            row=1,
            column=3,
            padx=(2,5), # left/right padding
            pady=(1,1), # top/bottom padding
            sticky=tk.EW
            )
        
        self.entryborder2.grid(
            row=2,
            column=3,
            padx=(2,5), # left/right padding
            pady=(1,1), # top/bottom padding
            sticky=tk.EW
            )
        
        self.entryborder3.grid(
            row=3,
            column=3,
            padx=(2,5), # left/right padding
            pady=(1,1), # top/bottom padding
            sticky=tk.EW
            )

        # entry fields
        self.entry1 = tk.Entry(
            self.entryborder1,
            textvariable=self.value1)
        self.entry2 = tk.Entry(
            self.entryborder2,
            textvariable=self.value2)
        self.entry3 = tk.Entry(
            self.entryborder3,
            textvariable=self.value3)

        self.entry1.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)
        self.entry2.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)
        self.entry3.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)

        self.entry1.pack(padx=1, pady=1, fill=tk.X)
        self.entry2.pack(padx=1, pady=1, fill=tk.X)
        self.entry3.pack(padx=1, pady=1, fill=tk.X)

        # add comboboxes and entries to a list to be looped through
        # when getting user input
        self.user_input_list = [[self.combo1, self.entry1],
                                [self.combo2, self.entry2],
                                [self.combo3, self.entry3]]

        # text boxes to display error messages
        self.error_text1 = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=3,
            width=tk_error_width
            )
        self.error_text2 = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=3,
            width=tk_error_width
            )
        self.error_text3 = tk.Text(
            self,
            font=tk_error_font,
            background=tk_error_bg,
            foreground=tk_error_fg,
            borderwidth=tk_error_borderwidth,
            state='disabled',
            wrap=tk_error_wrap,
            height=3,
            width=tk_error_width
            )

        self.error_text1.grid(
            row=4,
            column=0,
            columnspan=4,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )
        self.error_text2.grid(
            row=5,
            column=0,
            columnspan=4,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )
        self.error_text3.grid(
            row=6,
            column=0,
            columnspan=4,
            padx=(5,5), # left/right padding
            pady=(0,5), # bottom padding
            sticky=tk.EW
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()

