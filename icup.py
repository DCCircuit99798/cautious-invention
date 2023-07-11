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
        choose_file_border.configure(style='WidgetBorder.TFrame')
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
        start_border.configure(style='WidgetBorder.TFrame')
        start_border.pack()

        # create buttons and frames for layout of program
        choose_file_button = ttk.Button(
            choose_file_border,
            text='Choose File')
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

        start_button = ttk.Button(start_border, text='Start!')
        start_button.pack(padx=1, pady=1)

    def __configure_styles(self):
        '''Configures the styles of all the widgets in the program.'''
        
        # create style object for the program
        self.style = ttk.Style(self)

        # use ttk theme that allows widget background colours
        # to be changed
        self.style.theme_use('alt')

        # configure all text in the program
        self.style.configure('.',
                             font=('Tahoma', 12),
                             foreground='#ffffff')

        # change background colour of all labels to
        # same colour as outer frames
        self.style.configure('TLabel',
                             background='#2d2d39')

        # title ttk label
        self.style.configure('Title.TLabel',
                             font=('Tahoma', 24),
                             background='#1e2129')

        # heading ttk labels
        self.style.configure('Heading.TLabel', font=('Tahoma', 8, 'bold'))

        # "required" ttk labels
        self.style.configure('Required.Heading.TLabel',
                             foreground='#aeb9ef')

        # ttk buttons
        self.style.configure('TButton',
                             background='#536cde',
                             borderwidth=0)
        self.style.map('TButton',
                       background = [('pressed', '#536cde'),
                                     ('active', '#6c81d9')],
                       foreground = [('pressed', '#ffffff'),
                                     ('active', '#ffffff')]
                       )

        '''
        # ttk checkbuttons
        self.style.configure('TCheckbutton',
                             background='#2d2d39',
                             indicatorbackground='#2d2d39',
                             indicatorforeground='#ffffff',
                             borderwidth=0)
        self.style.map('TCheckbutton',
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
        self.style.configure('TRadiobutton',
                             background='#2d2d39',
                             indicatorcolor='#2d2d39')
        self.style.map('TRadiobutton',
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
        self.style.map('TCombobox',
                       fieldbackground = [('pressed', '#2d2d39'),
                                          ('active', '#2d2d39')],
                       selectbackground = [('pressed', '#2d2d39'),
                                           ('active', '#2d2d39')],
                       selectforeground = [('pressed', '#ffffff'),
                                           ('active', '#ffffff')],
                       background = [('pressed', '#d5dbf2'),
                                     ('active', '#bac5f5')]
                       )

        global ttk_ar_options_combobox_width
        ttk_ar_options_combobox_width = 2

        # tk checkbuttons
        global tk_checkbutton_font, tk_checkbutton_bg, \
        tk_checkbutton_activebg, tk_checkbutton_fg, tk_checkbutton_activefg, \
        tk_checkbutton_selectcolor

        tk_checkbutton_font = ('Tahoma', 12)

        tk_checkbutton_bg = '#2d2d39'
        tk_checkbutton_activebg = '#2d2d39'

        tk_checkbutton_fg = '#ffffff'
        tk_checkbutton_activefg = '#ffffff'

        tk_checkbutton_selectcolor = '#2d2d39'
        
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

        tk_rates_entry_width = 5
        tk_rate_increment_entry_width = 5
        tk_ar_options_entry_width = 5

        # border frames
        self.style.configure('WidgetBorder.TFrame',
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
            selectcolor=tk_checkbutton_selectcolor)
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
            selectcolor=tk_checkbutton_selectcolor)
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
            selectcolor=tk_checkbutton_selectcolor)
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

        # borders for entry fields
        rates_minimum_border = BorderFrame(self)
        rates_minimum_border.configure(style='WidgetBorder.TFrame')
        rates_minimum_border.grid(row=2, column=1)

        rates_maximum_border = BorderFrame(self)
        rates_maximum_border.configure(style='WidgetBorder.TFrame')
        rates_maximum_border.grid(row=3, column=1)

        # entry fields
        rates_minimum_entry = tk.Entry(rates_minimum_border,
                                       textvariable=self.minimum_var)
        rates_minimum_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_rates_entry_width)
        rates_minimum_entry.pack(padx=1, pady=1)

        rates_maximum_entry = tk.Entry(rates_maximum_border,
                                        textvariable=self.maximum_var)
        rates_maximum_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_rates_entry_width)
        rates_maximum_entry.pack(padx=1, pady=1)


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

        # border for custom entry field
        rate_increment_entry_border = BorderFrame(self)
        rate_increment_entry_border.configure(style='WidgetBorder.TFrame')
        rate_increment_entry_border.grid(row=3, column=1)

        # entry field for custom rate increment
        rate_increment_entry = tk.Entry(
            rate_increment_entry_border,
            textvariable=self.increment_custom_var)
        rate_increment_entry.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_rate_increment_entry_width)
        rate_increment_entry.pack(padx=1, pady=1)

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

        # borders for comboboxes (dropdown menus)
        ar_options_cbborder1 = BorderFrame(self)
        ar_options_cbborder2 = BorderFrame(self)
        ar_options_cbborder3 = BorderFrame(self)

        ar_options_cbborder1.configure(style='WidgetBorder.TFrame')
        ar_options_cbborder2.configure(style='WidgetBorder.TFrame')
        ar_options_cbborder3.configure(style='WidgetBorder.TFrame')

        ar_options_cbborder1.grid(row=1, column=2)
        ar_options_cbborder2.grid(row=2, column=2)
        ar_options_cbborder3.grid(row=3, column=2)

        # comboboxes (dropdown menus)
        ar_options_combobox1 = ttk.Combobox(
            ar_options_cbborder1,
            textvariable=self.ar_options_type1,
            width=ttk_ar_options_combobox_width)
        ar_options_combobox2 = ttk.Combobox(
            ar_options_cbborder2,
            textvariable=self.ar_options_type2,
            width=ttk_ar_options_combobox_width)
        ar_options_combobox3 = ttk.Combobox(
            ar_options_cbborder3,
            textvariable=self.ar_options_type3,
            width=ttk_ar_options_combobox_width)

        ar_options_combobox1.pack(padx=1, pady=1)
        ar_options_combobox2.pack(padx=1, pady=1)
        ar_options_combobox3.pack(padx=1, pady=1)

        # define possible values for comboboxes
        ar_options_combobox1['values'] = ('x', 'c', 'C')
        ar_options_combobox2['values'] = ('x', 'c', 'C')
        ar_options_combobox3['values'] = ('x', 'c', 'C')

        # prevent user from entering a custom value in the comboboxes
        ar_options_combobox1['state'] = 'readonly'
        ar_options_combobox2['state'] = 'readonly'
        ar_options_combobox3['state'] = 'readonly'

        # borders for entry fields
        ar_options_eborder1 = BorderFrame(self)
        ar_options_eborder2 = BorderFrame(self)
        ar_options_eborder3 = BorderFrame(self)

        ar_options_eborder1.configure(style='WidgetBorder.TFrame')
        ar_options_eborder2.configure(style='WidgetBorder.TFrame')
        ar_options_eborder3.configure(style='WidgetBorder.TFrame')

        ar_options_eborder1.grid(row=1, column=3)
        ar_options_eborder2.grid(row=2, column=3)
        ar_options_eborder3.grid(row=3, column=3)

        # entry fields
        ar_options_entry1 = tk.Entry(ar_options_eborder1,
                                     textvariable=self.ar_options_value1)
        ar_options_entry2 = tk.Entry(ar_options_eborder2,
                                     textvariable=self.ar_options_value2)
        ar_options_entry3 = tk.Entry(ar_options_eborder3,
                                     textvariable=self.ar_options_value3)

        ar_options_entry1.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)
        ar_options_entry2.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)
        ar_options_entry3.configure(
            font=tk_entry_font,
            background=tk_entry_bg,
            foreground=tk_entry_fg,
            borderwidth=tk_entry_borderwidth,
            insertbackground=tk_entry_insertbackground,
            width=tk_ar_options_entry_width)

        ar_options_entry1.pack(padx=1, pady=1)
        ar_options_entry2.pack(padx=1, pady=1)
        ar_options_entry3.pack(padx=1, pady=1)


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
            selectcolor=tk_checkbutton_selectcolor)
        other_checkbox.grid(row=2, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()

