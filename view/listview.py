from tkinter import ttk
from tkinter import StringVar

TESTDATA = [{'IP Version': '4', 'IP Address': '192.168.1.1', 'Port Range': '0-65000', 'Timeout': '5'}, {'IP Version': '4', 'IP Address': '192.168.0.1', 'Port Range': '0-65000', 'Timeout': '5'}]

class ListView(ttk.Frame):
    COLUMNS = ('ver', 'ip', 'port', 'time')
    HEADINGS = ('IP Version', 'IP Address', 'Port Range', 'Timeout')
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master=master, width=300)
        self.grid(row=0, column=0)
        self.tBox = ttk.Treeview(master=self, height=30, columns=ListView.COLUMNS)
        self.scroll = ttk.Scrollbar(master=self, orient="vertical", command=self.tBox.yview)
        self.tBox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row = 0, column = 1)
        self.tBox.grid(row = 0, column = 0)
        self.doHeadings()
        self.addTestData()

    def append(self, listOfDictionary):
        for l in listOfDictionary:
            self.tBox.insert('', index='end')
    def doHeadings(self):
        for col in ListView.COLUMNS:
            
    def addTestData(self):
        self.append(TESTDATA)
