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

# frame
label1 = ttk.Label(root, text="Label 1")
label1.pack()

label2 = ttk.Label(root, text="Label 2")
label2.pack()

label3 = ttk.Label(root, text="Label 3")
label3.pack()

root.mainloop()
