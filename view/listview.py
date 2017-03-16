from tkinter import Listbox
from tkinter import ttk
from tkinter import StringVar

class ListView(ttk.Frame):
    def __int__(self, master, **kw):
        super().__init__(master)
        self.lbox = Listbox(self, height=30, selectmode=SINGLE)
        self.scroll = ttk.Scrollbar(self, orient=VERTICAL, command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row = 0, column = 1)
        self.lbox.grid(row = 0, column = 0)

    def append(self, lofl):
        for i in lofl:
            j = StringVar(i)
            self.lbox.insert(END, j)
