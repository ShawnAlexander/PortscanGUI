from tkinter import ttk
from tkinter import StringVar

class ListView(ttk.Frame):
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master=master)
        self.grid(row=0, column=0)
        self.tBox = ttk.Treeview(master=self, height=30)
        self.scroll = ttk.Scrollbar(master=self, orient="vertical", command=self.tBox.yview)
        self.tBox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row = 0, column = 1)
        self.tBox.grid(row = 0, column = 0)

    def append(self, lofl):
        for i in lofl:
            j = StringVar(i)
            self.tBox.insert(END, j)
