# import required modules
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from pathlib import Path
import sys

# get path of modules that aren't built-in

# append path to system

# import required modules

class App(tk.Tk):
    '''Create the main window of the program'''

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Idiot Caleb's Uprating Project")
        self.geometry('520x260')
        self.configure(bg='#1e2129')
        #self.resizable(False, False)

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
        self.choose_file_border.configure(style='WidgetBorder.TFrame')
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
        self.ar_border.configure(style='NormalBorder.TFrame')
        self.ar_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.BOTH,
            expand=True) # take up rest of vert and horz space

        self.other_border = BorderFrame(self.frame2)
        self.other_border.configure(style='NormalBorder.TFrame')
        self.other_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.X) # take up all horz space

        self.start_border = BorderFrame(self.frame2)
        self.start_border.configure(style='WidgetBorder.TFrame')
        self.start_border.pack(
            padx=(4,0), # left padding
            pady=(0,4), # bottom padding
            fill=tk.X) # take up all horz space

        # create buttons and frames for layout of program
        self.choose_file_button = ttk.Button(
            self.choose_file_border,
            text='Choose File')
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

        self.other_frame = OtherFrame(self.other_border)
        self.other_frame.configure(style='Normal.TFrame')
        self.other_frame.pack(
            padx=1,
            pady=1,
            fill=tk.X) # take up all horz space

        self.start_button = ttk.Button(
            self.start_border,
            text='Start!',
            command=self.start)
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

        # "required" ttk labels
        self.style.configure(
            'Diffs.Required.TLabel', # difficulties
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'Rates.Required.TLabel', # rates
            foreground='#aeb9ef',
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
        
        '''
        # ttk checkbuttons
        self.style.configure(
            'TCheckbutton',
            background='#2d2d39',
            indicatorbackground='#2d2d39',
            indicatorforeground='#ffffff',
            borderwidth=0)
        self.style.map(
            'TCheckbutton',
            background = [('pressed', '#2d2d39'),
                         ('active', '#2d2d39')],
            foreground = [('pressed', '#ffffff'),
                         ('active', '#ffffff')],
            indicatorbackground = [('pressed', '#2d2d39'),
                                  ('active', '#2d2d39')],
            indicatorforeground = [('pressed', '#ffffff'),
                                  ('active', '#ffffff')]
            )
        '''
        

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

        tk_error_height = 5
        tk_error_width = 1 # width controlled by sticky=tk.EW within frame


        # border frames
        self.style.configure(
            'WidgetBorder.TFrame',
            background='#ffffff',
            relief='flat')

        self.style.configure(
            'NormalBorder.TFrame',
            background='#aeb9ef')

        self.style.configure(
            'Diffs.NormalBorder.TFrame', # difficulties
            background='#aeb9ef')

        self.style.configure(
            'Rates.NormalBorder.TFrame', # rates
            background='#aeb9ef')

        self.style.configure(
            'RateInc.NormalBorder.TFrame', # rate increment
            background='#aeb9ef')

        # visible frames (that contain widgets)
        self.style.configure(
            'Normal.TFrame',
            background='#2d2d39')

        # outer invisible frames
        self.style.configure(
            'TFrame',
            background='#1e2129')


    def start(self):
        '''Start working with files and creating new levels.
           NOTE: Only prints information in terminal as of now.'''

        # create variables to keep track of user info
        self.user_diffs = []
        self.user_min = None
        self.user_max = None
        self.user_rate_inc = None
        self.user_ar_option1 = []
        self.user_ar_option2 = []
        self.user_ar_option3 = []
        self.user_pitch_rates = 1

        # variable to keep track of validity of user input
        self.user_validity = True

        # reset styles to default
        self.style.configure(
            'Diffs.NormalBorder.TFrame', # difficulties
            background='#aeb9ef')

        self.style.configure(
            'Diffs.Required.TLabel', # difficulties
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'Rates.NormalBorder.TFrame', # rates
            background='#aeb9ef')

        self.style.configure(
            'Rates.Required.TLabel', # rates
            foreground='#aeb9ef',
            font=('Tahoma', 8, 'bold'))

        self.style.configure(
            'RateInc.NormalBorder.TFrame', # rate increment
            background='#aeb9ef')
        
        # check status of difficulty checkboxes and add
        # difficulties to the list if they are selected
        if self.diffs_frame.easy_var.get() == 1:
            self.user_diffs.append('easy')

        if self.diffs_frame.hard_var.get() == 1:
            self.user_diffs.append('hard')

        if self.diffs_frame.ex_var.get() == 1:
            self.user_diffs.append('extreme')

        # if no difficulties are selected
        if self.user_diffs == []:
            
            # allow text inside error widget to be edited
            self.diffs_frame.error_text.configure(state='normal')

            # clear any text inside error widget
            self.diffs_frame.error_text.delete('1.0', tk.END)

            # insert error message (line 1, character 0)
            self.diffs_frame.error_text.insert(
                '1.0',
                'At least one difficulty must be selected')

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

        # if at least one difficulty is selected
        else:

            # allow text to be edited
            self.diffs_frame.error_text.configure(state='normal')
            
            # clear error message in text widget
            self.diffs_frame.error_text.delete('1.0', tk.END)

            # prevent text from being edited
            self.diffs_frame.error_text.configure(state='disabled')

        # get value of minimum and maximum rates
        try:
            self.user_min = float(self.rates_frame.min_var.get())
            self.user_max = float(self.rates_frame.max_var.get())

            # if minimum rate is zero or negative
            if self.user_min <= 0:

                
                print('Rates cannot be zero or negative')
                self.user_validity = False

            # maximum rate cannot be less than minimum rate
            elif self.user_max < self.user_min:
                print('Maximum rate cannot be less than minimum')
                self.user_validity = False

        # if entry fields are empty,
        # except error and print error message
        except ValueError:
            print('Minimum and maximum rates must be valid numbers')
            self.user_validity = False

        

        # if custom increment is selected, get value from entry field
        if self.rate_inc_frame.var.get() == 'Custom':
            try:
                self.user_rate_inc = float(self.rate_inc_frame.custom_var.get())

                # rate increment cannot be zero or negative
                if self.user_rate_inc <= 0:
                    print('Rate increment cannot be zero or negative')
                    self.user_validity = False
            
            except ValueError:
                print('Custom rate increment must be a valid number')
                self.user_validity = False

        # otherwise get rate increment from radio buttons
        else:
            self.user_rate_inc = self.rate_inc_frame.var.get()


        # AR Option #1:
        # get AR type
        self.user_ar_type1 = self.ar_frame.type1.get()

        # if type is chosen, get AR value
        if self.user_ar_type1 != None:
            
            try:
                # get AR value
                self.user_ar_value1 = float(self.ar_frame.value1.get())

                # append type and value to list if value is valid
                self.user_ar_option1.append(self.user_ar_type1)
                self.user_ar_option1.append(self.user_ar_value1)

            # otherwise, check next AR option
            except ValueError:
                pass
                
        # AR Option #2:
        # get AR type
        self.user_ar_type2 = self.ar_frame.type2.get()

        # if type is chosen, get AR value
        if self.user_ar_type2 != None:
            
            try:
                # get AR value
                self.user_ar_value2 = float(self.ar_frame.value2.get())

                # append type and value to list if value is valid
                self.user_ar_option2.append(self.user_ar_type2)
                self.user_ar_option2.append(self.user_ar_value2)

            # otherwise, check next AR option
            except ValueError:
                pass

        # AR Option #3:
        # get AR type
        self.user_ar_type3 = self.ar_frame.type3.get()

        # if type is chosen, get AR value
        if self.user_ar_type3 != None:
            
            try:
                # get AR value
                self.user_ar_value3 = float(self.ar_frame.value3.get())

                # append type and value to list if value is valid
                self.user_ar_option3.append(self.user_ar_type3)
                self.user_ar_option3.append(self.user_ar_value3)

            # otherwise, check next AR option
            except ValueError:
                pass


        # get status of "pitch rates"
        self.user_pitch_rates = self.other_frame.pitch_rates_var.get()

        # print collected user info
        # NOTE: only for debugging purposes, remove in final program
        print(self.user_diffs)
        print(self.user_min)
        print(self.user_max)
        print(self.user_rate_inc)
        print(self.user_ar_option1)
        print(self.user_ar_option2)
        print(self.user_ar_option3)
        print(self.user_pitch_rates)

        # print self.user_validity
        # NOTE: only for debugging purpose, remove in final program
        print()
        print(self.user_validity)

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
            height=tk_error_height,
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
            height=tk_error_height,
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

        # variable to store custom rate increment in entry field
        self.custom_var = tk.StringVar()

        # border for custom entry field
        self.entry_border = BorderFrame(self)
        self.entry_border.configure(style='WidgetBorder.TFrame')
        self.entry_border.grid(
            row=3,
            column=1,
            padx=(0,5), # right padding
            pady=(0,5) # bottom padding
            )

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
        self.checkborder1 = BorderFrame(self)
        self.checkborder2 = BorderFrame(self)
        self.checkborder3 = BorderFrame(self)

        self.checkborder1.configure(style='WidgetBorder.TFrame')
        self.checkborder2.configure(style='WidgetBorder.TFrame')
        self.checkborder3.configure(style='WidgetBorder.TFrame')

        self.checkborder1.grid(
            row=1,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )
        
        self.checkborder2.grid(
            row=2,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )
        
        self.checkborder3.grid(
            row=3,
            column=2,
            padx=(2,0), # left padding
            pady=(1,1), # top/bottom padding
            )

        # comboboxes (dropdown menus)
        self.combo1 = ttk.Combobox(
            self.checkborder1,
            textvariable=self.type1,
            width=ttk_ar_options_combo_width)
        self.combo2 = ttk.Combobox(
            self.checkborder2,
            textvariable=self.type2,
            width=ttk_ar_options_combo_width)
        self.combo3 = ttk.Combobox(
            self.checkborder3,
            textvariable=self.type3,
            width=ttk_ar_options_combo_width)

        self.combo1.pack(padx=1, pady=1)
        self.combo2.pack(padx=1, pady=1)
        self.combo3.pack(padx=1, pady=1)

        # define possible values for comboboxes
        self.combo1['values'] = ('x', 'c', 'C')
        self.combo2['values'] = ('x', 'c', 'C')
        self.combo3['values'] = ('x', 'c', 'C')

        # prevent user from entering a custom value in the comboboxes
        self.combo1['state'] = 'readonly'
        self.combo2['state'] = 'readonly'
        self.combo3['state'] = 'readonly'

        # borders for entry fields
        self.entryborder1 = BorderFrame(self)
        self.entryborder2 = BorderFrame(self)
        self.entryborder3 = BorderFrame(self)

        self.entryborder1.configure(style='WidgetBorder.TFrame')
        self.entryborder2.configure(style='WidgetBorder.TFrame')
        self.entryborder3.configure(style='WidgetBorder.TFrame')

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


class OtherFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):
        '''Create necessary widgets within frame'''

        # label
        self.heading_label = ttk.Label(
            self,
            text='OTHER',
            style='Heading.TLabel')
        self.heading_label.grid(
            row=0,
            column=0,
            padx=(5,0), # left padding
            pady=(5,0), # top padding
            sticky=tk.W
            )

        # create variables to store state of "pitch rates" checkbox
        self.pitch_rates_var = tk.StringVar()

        # set default value of pitch rates variable to 1 (on)
        self.pitch_rates_var.set(1)
        
        # checkbox
        self.check = tk.Checkbutton(
            self,
            text='Change audio pitch with rate',
            variable=self.pitch_rates_var)
        self.check.configure(
            font=tk_check_font,
            background=tk_check_bg,
            activebackground=tk_check_activebg,
            foreground=tk_check_fg,
            activeforeground=tk_check_activefg,
            selectcolor=tk_check_selectcolor)
        self.check.grid(
            row=2,
            column=0,
            padx=(5,5), # left/right padding
            )

if __name__ == "__main__":
    app = App()
    app.mainloop()

