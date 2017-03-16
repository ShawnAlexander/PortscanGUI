#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from .listview import ListView
from .detailed_view import DetailedFrame

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Portscanner - Shawn Johnson")
        self.container = ttk.Frame(self)
        self.container.grid(column=0, row=0)
        self.outputFrame = ttk.Frame(self.container)
        self.outputFrame.grid(row = 0, column = 0)
        self.inputFrame = ttk.Frame(self.container)
        self.inputFrame.grid(row = 0, column = 1)
        self.container.columnconfigure(0, weight=3)
        self.container.columnconfigure(1, weight=1)
        self.lbox = ListView(self.outputFrame)
        self.lbox.grid(row=0, column=0)
        self.dView = DetailedFrame(self.outputFrame)
        self.dView.grid(row=1, column=0)
