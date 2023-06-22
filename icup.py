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
        self.geometry('300x200')
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
        choose_file_button.grid(row=0, column=0)
        
        difficulties_frame = DifficultiesFrame(frame0)
        difficulties_frame.grid(row=1, column=0)

        rates_frame = RatesFrame(frame1)
        rates_frame.grid(row=0, column=0)

        rate_increment_frame = RateIncrementFrame(frame1)
        rate_increment_frame.grid(row=1, column=0)

        ar_options_frame = AROptionsFrame(frame2)
        ar_options_frame.grid(row=0, column=0)

        other_frame = OtherFrame(frame2)
        other_frame.grid(row=1, column=0)

        start_button = ttk.Button(frame2, text='Start!')
        start_button.grid(row=2, column=0)

        

        

        


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


class RatesFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)


class RateIncrementFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)


class AROptionsFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)


class OtherFrame(ttk.Frame):
    '''Visible frame for difficulty selection checkboxes
    to be displayed.'''

    def __init__(self, container):
        super().__init__(container)

        # configure height and width
        # NOTE: this is temporary, just to make the frames visible
        self.configure(height=100, width=50)


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
# create main window
root = tk.Tk()

# configure window
root.title("Idiot Caleb's Uprating Project")
root.geometry('300x200')
root.configure(bg='#1e2129')

# create buttons and frames (forms the visual layout of the program)
# grid layout is used to separate widgets into columns
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)

choose_file_button = ttk.Button(frame1, text='Choose File')
choose_file_button.pack()

difficulties_frame = ttk.Frame(frame1, height=100, width=50)
difficulties_frame.pack()

frame2 = ttk.Frame(root)
frame2.grid(row=0, column=1)

rates_frame = ttk.Frame(frame2, height=100, width=50)
rates_frame.pack()

rate_increment_frame = ttk.Frame(frame2, height=100, width=50)
rate_increment_frame.pack()

frame3 = ttk.Frame(root)
frame3.grid(row=0, column=2)

ar_options_frame = ttk.Frame(frame3, height=100, width=50)
ar_options_frame.pack()

other_frame = ttk.Frame(frame3, height=100, width=50)
other_frame.pack()

start_button = ttk.Button(frame3, text='Start!')
start_button.pack()

style = ttk.Style(root)
style.configure('TFrame',
                background='#2d2d39',
                relief='groove',
                borderwidth=2)

root.mainloop()
"""
