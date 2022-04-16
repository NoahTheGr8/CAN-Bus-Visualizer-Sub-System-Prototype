import tkinter
from tkinter import *
from tkinter import ttk
import can
import time

class GUI(object):
    def __init__(self, title, size):
        # Create window
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(size)

        # Create frame
        self.frame = Frame(self.window)
        self.frame.pack(#padx=14, #padx and pady set the distance between borders
                        #pady=14,
                        side=TOP) # dysplayed on the center

        # Create table
        self.table = ttk.Treeview(master=self.frame,
                                  columns=('Timestamp', 'ID', 'DL', 'DATA', 'Channel'),
                                  show='headings',
                                  height=15,  #heigth to set the number of columns
                                  )
        self.table.pack(side=LEFT)

        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(master=self.frame,
                                       orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.table.yview)

        # Create columns
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', anchor=CENTER, stretch=NO, width=150)
        self.table.column('#2', anchor=CENTER, stretch=NO, width=50)
        self.table.column('#3', anchor=CENTER, stretch=NO, width=50)
        self.table.column('#4', anchor=CENTER, stretch=NO, width=155)
        self.table.column('#5', anchor=CENTER, stretch=NO, width=90)

        # Create headings
        self.table.heading('#0', text='')
        self.table.heading('#1', text='Timestamp', anchor=CENTER)
        self.table.heading('#2', text='ID', anchor=CENTER)
        self.table.heading('#3', text='DL', anchor=CENTER)
        self.table.heading('#4', text='Data', anchor=CENTER)
        self.table.heading('#5', text='Channel', anchor=CENTER)

    def selected_item(self):
        current_item = self.table.focus()
        if current_item is None:
            return 0
        else:
            return 1

    def add(self, msg: can.Message):
        data = '0x'
        for index in range(0, min(msg.dlc, len(msg.data))):
            data += (f"{msg.data[index]:02x}")
        self.table.insert(parent='',
                          index='end',
                          values=(msg.timestamp, msg.arbitration_id, msg.dlc, data, msg.channel))
        #time.sleep(0.5) #to contol the flow of the packets

    def start(self):
        self.window.mainloop()

    def messageCallback(self, ms, function):
        msg: can.Message = function()
        if msg is not None:
            self.add(msg)
            self.table.yview_moveto(1)  # Allows autoscroll



        self.window.after(ms, self.messageCallback, ms, function)

class TrafficDisplayer(object):
    def __init__(self, size='750x400', ms=None, function=None):
        self.gui = GUI('CAN Bus Visualizer', size)
        if function is not None:
            self.gui.messageCallback(ms, function)
        self.gui.start()

if __name__ == '__main__':
    disp = TrafficDisplayer()
