from tkinter import ttk

class InputView(ttk.Frame):
    TIMEOUTS = []
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master)
        self.hostRangeIPV4 = ttk.Labelframe(master=self, text="Host Range")
        self.hostRangeIPV4.grid(row=0, column=0, sticky='ew')

        self.portRange = ttk.Labelframe(master=self, text="Port Range")
        self.portRange.grid(row=1, column=0)
        self.portStartFrame = ttk.Labelframe(master=self.portRange, text='Start Port')
        self.portEndFrame = ttk.Labelframe(master=self.portRange, text='End Port')
        self.portStartFrame.grid(row=0, column=0)
        self.portEndFrame.grid(row =1, column=0)
        self.portStart = ttk.Entry(master=self.portStartFrame, width=6)
        self.portEnd = ttk.Entry(master=self.portEndFrame, width = 6)
        self.portStart.grid(row=0, column=0)
        self.portEnd.grid(row=0, column=0)

        for i in range(1, 21):
            InputView.TIMEOUTS.append(i)

        self.timeoutFrame = ttk.Labelframe(master=self, text="Timeout")
        self.timeoutFrame.grid(row=2, column=0)
        self.timeout = ttk.Combobox(master=self.timeoutFrame, values=InputView.TIMEOUTS)
        self.timeout.grid(row = 2, column = 0)



        self.fire = ttk.Button(master=self, text="Fire!")
        self.fire.grid(row=3, column=0)

        self.ipv4StartFrame = ttk.Labelframe(self.hostRangeIPV4, text='Start')
        self.ipv4EndFrame = ttk.Labelframe(self.hostRangeIPV4, text='End')
        self.ipv4StartFrame.grid(row=0, column = 0)
        self.ipv4EndFrame.grid(row = 1, column=0)

        self.periodLabel = []
        for i in range(3):
            self.periodLabel.append(ttk.Label(master=self.ipv4StartFrame, text='.'))
        for i in range(3):
            self.periodLabel.append(ttk.Label(master=self.ipv4EndFrame, text='.'))

        self.ipv4Start = []
        self.ipv4End = []
        for i in range(4):
            self.ipv4Start.append(ttk.Entry(master=self.ipv4StartFrame, width=3))
        for i in range(4):
            self.ipv4End.append(ttk.Entry(master=self.ipv4EndFrame, width=3))

        self.ipv4Start[0].grid(row=0, column=0)
        self.periodLabel[0].grid(row=0, column=1)
        self.ipv4Start[1].grid(row=0, column=2)
        self.periodLabel[1].grid(row=0, column=3)
        self.ipv4Start[2].grid(row=0, column=4)
        self.periodLabel[2].grid(row=0, column=5)
        self.ipv4Start[3].grid(row=0, column=6)


        self.ipv4End[0].grid(row=2, column=0)
        self.periodLabel[3].grid(row=2, column=1)
        self.ipv4End[1].grid(row=2, column=2)
        self.periodLabel[4].grid(row=2, column=3)
        self.ipv4End[2].grid(row=2, column=4)
        self.periodLabel[5].grid(row=2, column=5)
        self.ipv4End[3].grid(row=2, column=6)





