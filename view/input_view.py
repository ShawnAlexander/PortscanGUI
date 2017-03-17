from tkinter import ttk

class InputView(ttk.Frame):
    TIMEOUTS = []
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master)
        self.hostRangeIPV4 = ttk.Labelframe(master=self, text="Host Range")
        self.hostRangeIPV4.grid(row=0, column=0)
        self.portRange = ttk.Labelframe(master=self, text="Port Range")
        self.portRange.grid(row=1, column=0)
        self.timeoutFrame = ttk.Labelframe(master=self, text="Timeout")
        self.timeout = ttk.Combobox(master=self.timeoutFrame)
        self.timeout.grid(row = 2, column = 0)
        self.fire = ttk.Button(master=self, text="Fire")
        self.fire.grid(row=3, column=0)
        self.periodLabel = []
        for i in range(3):
            self.periodLabel.append(ttk.Label(master=self.hostRangeIPV4, text='.'))

        self.ipv4_1 = ttk.Entry(master=self.hostRangeIPV4, width=3)
        self.ipv4_1.grid(row=0, column=0)
        self.periodLabel[0].grid(row=0, column=1)
        self.ipv4_2 = ttk.Entry(master=self.hostRangeIPV4, width=3)
        self.ipv4_2.grid(row=0, column=2)
        self.periodLabel[1].grid(row=0, column=3)
        self.ipv4_3 = ttk.Entry(master=self.hostRangeIPV4, width=3)
        self.ipv4_3.grid(row=0, column=4)
        self.periodLabel[2].grid(row=0, column=5)
        self.ipv4_4 = ttk.Entry(master=self.hostRangeIPV4, width=3)
        self.ipv4_4.grid(row=0, column=6)





