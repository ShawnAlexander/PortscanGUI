from tkinter import ttk

class InputView(ttk.Frame):
    TIMEOUTS = []
    def __init__(self, master):
        super().__init__(master, padx=5, pady=5)
        self.hostRangeIPV4 = ttk.Labelframe(self, text="Host Range")
        self.hostRangeIPV4.grid(row=0, column=0)
        self.portRange = ttk.Labelframe(self, text="Port Range")
        self.portRange.grid(row=1, column=0)
        self.timeoutFrame = ttk.Labelframe(self, text="Timeout")
        self.timeout = ttk.Combobox(self.timeoutFrame)
        self.timeout.grid(row = 2, column = 0)
        self.fire = ttk.Button(self, text="Fire")
        self.fire.grid(row=3, column=0)

        self.periodLabel = ttk.Label(self.hostRangeIPV4, text=".")

        self.ipv4_1 = ttk.Entry(self.hostRangeIPV4, width=3)
        self.ipv4_1.grid(row=0, column=0)
        self.periodLabel.grid(row=0, column=1)
        self.ipv4_2 = ttk.Entry(self.hostRangeIPV4, width=3)
        self.ipv4_2.grid(row=0, column=2)
        self.periodLabel.grid(row=0, column=3)
        self.ipv4_3 = ttk.Entry(self.hostRangeIPV4, width=3)
        self.ipv4_3.grid(row=0, column=4)
        self.periodLabel.grid(row=0, column=5)
        self.ipv4_4 = ttk.Entry(self.hostRangeIPV4, width=3)
        self.ipv4_4.grid(row=0, column=6)





