#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from .listview import ListView
from .detailed_view import DetailedFrame

class App(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master.title("GUI Port Scanner - Shawn Johnson")
        self.grid(column=0, row=0)
        self.outputFrame = ttk.Frame(master=self)
        self.outputFrame.grid(row = 0, column = 0)
        self.inputFrame = ttk.Frame(master=self)
        self.inputFrame.grid(row = 0, column = 1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.lbox = ListView(master=self.outputFrame)
        self.lbox.grid(row=0, column=0)
        self.dView = DetailedFrame(master=self.outputFrame)
        self.dView.grid(row=1, column=0)
