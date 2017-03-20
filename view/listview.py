from tkinter import ttk
from tkinter import StringVar

TESTDATA = [{'IP Version': '4', '#0': '192.168.1.1', 'Port Range': '0-65000', 'Timeout': '5'}, {'IP Version': '4', '#0': '192.168.0.1', 'Port Range': '22-80', 'Timeout': '5'}]

class ListView(ttk.Frame):
    COLUMNS = ('ver', 'port', 'time')
    HEADINGS = ('IP Version', 'Port Range', 'Timeout')
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master=master)
        self.tBox = ttk.Treeview(master=self, height=30, columns=ListView.COLUMNS)
        self.scroll = ttk.Scrollbar(master=self, orient="vertical", command=self.tBox.yview)
        self.tBox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row = 0, column = 1, sticky='nse')
        self.tBox.grid(row = 0, column = 0)
        self.doHeadings()
        self.addTestData()

    def append(self, listOfDictionary):
        for d in listOfDictionary:
            self.tBox.insert('', index='end', values=[value for key, value in d.items()])
    def doColumns(self):
        self.tBox.column('#0', minwidth=15, width=30)
        for col in ListView.COLUMNS:
            self.tBox.column(col, minwidth=20, width=30)

    def doHeadings(self):
        self.tBox.heading('#0', text='IP Address')
        for i, j in zip(ListView.COLUMNS, ListView.HEADINGS):
            self.tBox.heading(i, text=j)

    def addTestData(self):
        self.append(TESTDATA)
