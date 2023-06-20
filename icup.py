# import tkinter and required submodules
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

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
