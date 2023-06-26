# import tkinter and required submodules
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class App(tk.Tk):
    '''This class creates the main window of the program.'''

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Idiot Caleb's Uprating Project")
        self.geometry('600x400')
        self.configure(bg='#1e2129')

        # call method to create widgets
        self.__create_widgets()

        # configure styles
        self.style = ttk.Style(self)
        self.style.configure('TFrame',
                        background='#2d2d39',
                        relief='groove',
                        borderwidth=2)

    def __create_widgets(self):
        '''Adds labels, buttons, and frames to create the layout of
        the program.'''
        
        # add label for program title
        title_label = ttk.Label(self, text="Idiot Caleb's Uprating Project")
        title_label.grid(row=0, column=0, columnspan=3)

        # create instances of OuterFrame for other widgets to be placed in
        frame0 = OuterFrame(self, 0)
        frame1 = OuterFrame(self, 1)
        frame2 = OuterFrame(self, 2)

        # create buttons and frames for layout of program
        choose_file_button = ttk.Button(frame0, text='Choose File')
        choose_file_button.pack()
        
        difficulties_frame = DifficultiesFrame(frame0)
        difficulties_frame.pack()

        rates_frame = RatesFrame(frame1)
        rates_frame.pack()

        rate_increment_frame = RateIncrementFrame(frame1)
        rate_increment_frame.pack()

        ar_options_frame = AROptionsFrame(frame2)
        ar_options_frame.pack()

        other_frame = OtherFrame(frame2)
        other_frame.pack()

        start_button = ttk.Button(frame2, text='Start!')
        start_button.pack()


class OuterFrame(ttk.Frame):
    '''This class creates invisible frames for the buttons and visible
    frames to be placed in.'''
    
    def __init__(self, container, frame_number):
        super().__init__(container)

        # place frame on grid according to frame_number argument
        self.grid(row=1, column=frame_number)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=200, width=100)


class DifficultiesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        difficulties_heading_label = ttk.Label(self, text='Difficulties')
        difficulties_heading_label.grid(row=0, column=0)

        difficulties_required_label = ttk.Label(self, text='*Required')
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
        difficulties_easy_checkbox = ttk.Checkbutton(self,
                                                  text='Easy',
                                                  variable=self.easy_var)
        difficulties_easy_checkbox.grid(row=2, column=0)
                                                  
        difficulties_hard_checkbox = ttk.Checkbutton(self,
                                                  text='Hard',
                                                  variable=self.hard_var)
        difficulties_hard_checkbox.grid(row=3, column=0)

        difficulties_ex_checkbox = ttk.Checkbutton(self,
                                                  text='Extreme',
                                                  variable=self.ex_var)
        difficulties_ex_checkbox.grid(row=4, column=0)

class RatesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        rates_heading_label = ttk.Label(self, text='Rates')
        rates_heading_label.grid(row=0, column=0, columnspan=2)

        rates_required_label = ttk.Label(self, text='*Required')
        rates_required_label.grid(row=1, column=0, columnspan=2)

        rates_minimum_label = ttk.Label(self, text='Minimum')
        rates_minimum_label.grid(row=2, column=0)

        rates_maximum_label = ttk.Label(self, text='Maximum')
        rates_maximum_label.grid(row=3, column=0)

        # variables to store text in entry fields
        self.minimum_var = tk.StringVar()
        self.maximum_var = tk.StringVar()

        # entry fields
        rates_minimum_entry = ttk.Entry(self, textvariable=self.minimum_var)
        rates_minimum_entry.grid(row=2, column=1)

        rates_maximum_entry = ttk.Entry(self, textvariable=self.maximum_var)
        rates_maximum_entry.grid(row=3, column=1)


class RateIncrementFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        rate_increment_heading_label = ttk.Label(self, text='Rate Increment')
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

        # the custom value is selected by default from the .get() method,
        # so deselect the radio button
        self.increment_var.set(None)


class AROptionsFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # labels
        ar_options_heading_label = ttk.Label(self, text='AR Options')
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

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)

        # call method to create widgets
        self.__create_widgets()

    def __create_widgets(self):

        # label
        other_heading_label = ttk.Label(self, text='Other')
        other_heading_label.grid(row=0, column=0)

        # create variables to store state of "pitch rates" checkbox
        self.pitch_rates_var = tk.StringVar()

        # set default value of pitch rates variable to 1 (on)
        self.pitch_rates_var.set(0)
        
        # checkbox
        other_checkbox = ttk.Checkbutton(self,
                                         text='Change pitch of audio files with rate',
                                         variable=self.pitch_rates_var)
        other_checkbox.grid(row=2, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()

