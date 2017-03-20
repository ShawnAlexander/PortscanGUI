from tkinter import ttk

class DetailedFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master, relief='sunken')
