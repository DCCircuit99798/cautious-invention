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
    '''This class creates the main window of the program.'''

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Idiot Caleb's Uprating Project")
        self.geometry('800x400')
        self.configure(bg='#1e2129')

        # call method to configure styles
        self.__configure_styles()

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):
        '''Adds labels, buttons, and frames to create the layout of
        the program.'''
        
        # add label for program title
        title_label = ttk.Label(self,
                                text="Idiot Caleb's Uprating Project",
                                style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3)

        # create instances of OuterFrame for other widgets to be placed in
        frame0 = OuterFrame(self, 0)
        frame1 = OuterFrame(self, 1)
        frame2 = OuterFrame(self, 2)

        # create border frames to contain widgets and visible frames
        choose_file_border = BorderFrame(frame0)
        choose_file_border.configure(style='ButtonBorder.TFrame')
        choose_file_border.pack()

        difficulties_border = BorderFrame(frame0)
        difficulties_border.configure(style='NormalBorder.TFrame')
        difficulties_border.pack()

        rates_border = BorderFrame(frame1)
        rates_border.configure(style='NormalBorder.TFrame')
        rates_border.pack()

        rate_increment_border = BorderFrame(frame1)
        rate_increment_border.configure(style='NormalBorder.TFrame')
        rate_increment_border.pack()

        ar_options_border = BorderFrame(frame2)
        ar_options_border.configure(style='NormalBorder.TFrame')
        ar_options_border.pack()

        other_border = BorderFrame(frame2)
        other_border.configure(style='NormalBorder.TFrame')
        other_border.pack()

        start_border = BorderFrame(frame2)
        start_border.configure(style='ButtonBorder.TFrame')
        start_border.pack()

        # create buttons and frames for layout of program
        choose_file_button = tk.Button(
            choose_file_border,
            text='Choose File')

        choose_file_button.configure(
            font=tk_button_font,
            background=tk_button_bg,
            activebackground=tk_button_activebg,
            foreground=tk_button_fg,
            activeforeground=tk_button_activefg,
            borderwidth=tk_button_borderwidth)
        
        choose_file_button.pack(padx=1, pady=1)
        
        difficulties_frame = DifficultiesFrame(difficulties_border)
        difficulties_frame.configure(style='Normal.TFrame')
        difficulties_frame.pack(padx=1, pady=1)

        rates_frame = RatesFrame(rates_border)
        rates_frame.configure(style='Normal.TFrame')
        rates_frame.pack(padx=1, pady=1)

        rate_increment_frame = RateIncrementFrame(rate_increment_border)
        rate_increment_frame.configure(style='Normal.TFrame')
        rate_increment_frame.pack(padx=1, pady=1)

        ar_options_frame = AROptionsFrame(ar_options_border)
        ar_options_frame.configure(style='Normal.TFrame')
        ar_options_frame.pack(padx=1, pady=1)

        other_frame = OtherFrame(other_border)
        other_frame.configure(style='Normal.TFrame')
        other_frame.pack(padx=1, pady=1)

        start_button = tk.Button(start_border, text='Start!')
        start_button.configure(
            font=tk_button_font,
            background=tk_button_bg,
            activebackground=tk_button_activebg,
            foreground=tk_button_fg,
            activeforeground=tk_button_activefg,
            borderwidth=tk_button_borderwidth)
        start_button.pack(padx=1, pady=1)

    def __configure_styles(self):
        '''Configures the styles of all the widgets in the program.'''
        
        # create style object for the program
        self.style = ttk.Style(self)

        # change font of all text in the program
        self.style.configure('.', font=('Tahoma', 12))

        # change background colour of all labels to
        # same colour as outer frames
        self.style.configure('TLabel',
                             background='#2d2d39',
                             foreground='#ffffff')

        # title ttk label
        self.style.configure('Title.TLabel',
                             font=('Tahoma', 24),
                             background='#1e2129')

        # heading ttk labels
        self.style.configure('Heading.TLabel', font=('Tahoma', 8, 'bold'))

        # "required" ttk labels
        self.style.configure('Required.Heading.TLabel',
                             foreground='#aeb9ef')

        # tk buttons
        global tk_button_font, tk_button_bg, tk_button_activebg, \
        tk_button_fg, tk_button_activefg, tk_button_borderwidth
        
        tk_button_font = ('Tahoma', 12)

        tk_button_bg = '#536cde'
        tk_button_activebg = '#6c81d9'

        tk_button_fg = '#ffffff'
        tk_button_activefg = '#ffffff'
        
        tk_button_borderwidth = 0

        # tk checkbuttons
        global tk_checkbutton_font, tk_checkbutton_bg, \
        tk_checkbutton_activebg, tk_checkbutton_fg, tk_checkbutton_activefg, \
        tk_checkbutton_selectcolor, tk_checkbutton_relief
        
        tk_checkbutton_font = ('Tahoma', 12)
        
        tk_checkbutton_bg = '#2d2d39'
        tk_checkbutton_activebg = '#2d2d39'

        tk_checkbutton_fg = '#ffffff'
        tk_checkbutton_activefg = '#ffffff'

        tk_checkbutton_selectcolor = '#2d2d39'
        tk_checkbutton_relief = 'flat'

        # tk entry fields
        global tk_entry_font

        tk_entry_font = ('Tahoma', 12)

        # border frames
        self.style.configure('ButtonBorder.TFrame',
                             background='#ffffff',
                             relief='flat')

        self.style.configure('NormalBorder.TFrame',
                             background='#aeb9ef')

        # visible frames (that contain widgets)
        self.style.configure('Normal.TFrame',
                             background='#2d2d39')

        # outer invisible frames
        self.style.configure('TFrame',
                             background='#1e2129')


class OuterFrame(ttk.Frame):
    '''This class creates invisible frames for the buttons and visible
    frames to be placed in.'''
    
    def __init__(self, container, frame_number):
        super().__init__(container)

        # place frame on grid according to frame_number argument
        self.grid(row=1, column=frame_number)


class BorderFrame(ttk.Frame):
    '''This class creates frames to act as borders for widgets.'''

    def __init__(self, container):
        super().__init__(container)


class DifficultiesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()
        
    def __create_widgets(self):

        # labels
        difficulties_heading_label = ttk.Label(self,
                                               text='DIFFICULTIES',
                                               style='Heading.TLabel')
        difficulties_heading_label.grid(row=0, column=0)

        difficulties_required_label = ttk.Label(self,
                                                text='*Required',
                                                style='Required.Heading.TLabel')
        difficulties_required_label.grid(row=1, column=0)

        # variables to store state of checkboxes
        self.easy_var = tk.StringVar()
        self.hard_var = tk.StringVar()
        self.ex_var = tk.StringVar()

        # set value of checkbox variables to 0 (off)
        self.easy_var.set(0)
        self.hard_var.set(0)
        self.ex_var.set(0)

        # checkboxes
        difficulties_easy_checkbox = tk.Checkbutton(self,
                                                    text='Easy',
                                                    variable=self.easy_var)
        difficulties_easy_checkbox.configure(
            font=tk_checkbutton_font,
            background=tk_checkbutton_bg,
            activebackground=tk_checkbutton_activebg,
            foreground=tk_checkbutton_fg,
            activeforeground=tk_checkbutton_activefg,
            selectcolor=tk_checkbutton_selectcolor,
            relief=tk_checkbutton_relief)
        difficulties_easy_checkbox.grid(row=2, column=0)
                                                  
        difficulties_hard_checkbox = tk.Checkbutton(self,
                                                  text='Hard',
                                                  variable=self.hard_var)
        difficulties_hard_checkbox.configure(
            font=tk_checkbutton_font,
            background=tk_checkbutton_bg,
            activebackground=tk_checkbutton_activebg,
            foreground=tk_checkbutton_fg,
            activeforeground=tk_checkbutton_activefg,
            selectcolor=tk_checkbutton_selectcolor,
            relief=tk_checkbutton_relief)
        difficulties_hard_checkbox.grid(row=3, column=0)

        difficulties_ex_checkbox = tk.Checkbutton(self,
                                                  text='Extreme',
                                                  variable=self.ex_var)
        difficulties_ex_checkbox.configure(
            font=tk_checkbutton_font,
            background=tk_checkbutton_bg,
            activebackground=tk_checkbutton_activebg,
            foreground=tk_checkbutton_fg,
            activeforeground=tk_checkbutton_activefg,
            selectcolor=tk_checkbutton_selectcolor,
            relief=tk_checkbutton_relief)
        difficulties_ex_checkbox.grid(row=4, column=0)


class RatesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        rates_heading_label = ttk.Label(self,
                                        text='RATES',
                                        style='Heading.TLabel')
        rates_heading_label.grid(row=0, column=0, columnspan=2)

        rates_required_label = ttk.Label(self,
                                         text='*Required',
                                         style='Required.Heading.TLabel')
        rates_required_label.grid(row=1, column=0, columnspan=2)

        rates_minimum_label = ttk.Label(self, text='Minimum')
        rates_minimum_label.grid(row=2, column=0)

        rates_maximum_label = ttk.Label(self, text='Maximum')
        rates_maximum_label.grid(row=3, column=0)

        # variables to store text in entry fields
        self.minimum_var = tk.StringVar()
        self.maximum_var = tk.StringVar()

        # entry fields
        rates_minimum_entry = tk.Entry(self, textvariable=self.minimum_var)
        rates_minimum_entry.configure(
            font=tk_entry_font)
        rates_minimum_entry.grid(row=2, column=1)

        rates_maximum_entry = ttk.Entry(self, textvariable=self.maximum_var)
        rates_maximum_entry.grid(row=3, column=1)


class RateIncrementFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        rate_increment_heading_label = ttk.Label(self,
                                                 text='RATE INCREMENT',
                                                 style='Heading.TLabel')
        rate_increment_heading_label.grid(row=0, column=0, columnspan=2)

        # variable to store selected rate increment
        self.increment_var = tk.StringVar()

        # variable to store custom rate increment in entry field
        self.increment_custom_var = tk.StringVar()

        # entry field for custom rate increment
        rate_increment_entry = ttk.Entry(self,
                                         textvariable=self.increment_custom_var)
        rate_increment_entry.grid(row=3, column=1)

        # radio buttons
        rate_increment_radio1 = ttk.Radiobutton(self,
                                                text='0.05',
                                                value=0.05,
                                                variable=self.increment_var)

        rate_increment_radio2 = ttk.Radiobutton(self,
                                                text='0.10',
                                                value=0.10,
                                                variable=self.increment_var)

        rate_increment_radio3 = ttk.Radiobutton(self,
                                        text='Custom:',
                                        value=self.increment_custom_var.get(),
                                        variable=self.increment_var)

        rate_increment_radio1.grid(row=1, column=0)
        rate_increment_radio2.grid(row=2, column=0)
        rate_increment_radio3.grid(row=3, column=0)

        # set default value of rate increment to 0.05
        self.increment_var.set(0.05)


class AROptionsFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        ar_options_heading_label = ttk.Label(self,
                                             text='AR OPTIONS',
                                             style='Heading.TLabel')
        ar_options_heading_label.grid(row=0, column=0, columnspan=2)
        
        ar_options_label1 = ttk.Label(self, text='AR Option #1:')
        ar_options_label2 = ttk.Label(self, text='AR Option #2:')
        ar_options_label3 = ttk.Label(self, text='AR Option #3:')

        ar_options_label1.grid(row=1, column=0, columnspan=2)
        ar_options_label2.grid(row=2, column=0, columnspan=2)
        ar_options_label3.grid(row=3, column=0, columnspan=2)

        # variables to store selected AR type and value
        # for each of the three options
        self.ar_options_type1 = tk.StringVar()
        self.ar_options_type2 = tk.StringVar()
        self.ar_options_type3 = tk.StringVar()

        self.ar_options_value1 = tk.StringVar()
        self.ar_options_value2 = tk.StringVar()
        self.ar_options_value3 = tk.StringVar()

        # comboboxes (dropdown menus)
        ar_options_combobox1 = ttk.Combobox(self,
                                            textvariable=self.ar_options_type1)
        ar_options_combobox2 = ttk.Combobox(self,
                                            textvariable=self.ar_options_type2)
        ar_options_combobox3 = ttk.Combobox(self,
                                            textvariable=self.ar_options_type3)

        ar_options_combobox1.grid(row=1, column=2)
        ar_options_combobox2.grid(row=2, column=2)
        ar_options_combobox3.grid(row=3, column=2)

        # define possible values for comboboxes
        ar_options_combobox1['values'] = ('x', 'c', 'C')
        ar_options_combobox2['values'] = ('x', 'c', 'C')
        ar_options_combobox3['values'] = ('x', 'c', 'C')

        # prevent user from entering a custom value in the comboboxes
        ar_options_combobox1['state'] = 'readonly'
        ar_options_combobox2['state'] = 'readonly'
        ar_options_combobox3['state'] = 'readonly'

        # entry fields
        ar_options_entry1 = ttk.Entry(self,
                                      textvariable=self.ar_options_value1)
        ar_options_entry2 = ttk.Entry(self,
                                      textvariable=self.ar_options_value2)
        ar_options_entry3 = ttk.Entry(self,
                                      textvariable=self.ar_options_value3)

        ar_options_entry1.grid(row=1, column=3)
        ar_options_entry2.grid(row=2, column=3)
        ar_options_entry3.grid(row=3, column=3)


class OtherFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # label
        other_heading_label = ttk.Label(self,
                                        text='OTHER',
                                        style='Heading.TLabel')
        other_heading_label.grid(row=0, column=0)

        # create variables to store state of "pitch rates" checkbox
        self.pitch_rates_var = tk.StringVar()

        # set default value of pitch rates variable to 1 (on)
        self.pitch_rates_var.set(1)
        
        # checkbox
        other_checkbox = tk.Checkbutton(self,
                                         text='Change pitch of audio files with rate',
                                         variable=self.pitch_rates_var)
        other_checkbox.configure(
            font=tk_checkbutton_font,
            background=tk_checkbutton_bg,
            activebackground=tk_checkbutton_activebg,
            foreground=tk_checkbutton_fg,
            activeforeground=tk_checkbutton_activefg,
            selectcolor=tk_checkbutton_selectcolor,
            relief=tk_checkbutton_relief)
        other_checkbox.grid(row=2, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()

