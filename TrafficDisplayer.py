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
        self.frame.pack(pady=15)

        # Create table
        self.table = ttk.Treeview(master=self.frame, columns=('Timestamp', 'ID', 'DL', 'DATA', 'Channel'), show='headings', height=15)
        self.table.pack(side=LEFT)

        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(master=self.frame, orient=VERTICAL)
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

    def add(self, msg: can.Message):
        data = '0x'
        for index in range(0, min(msg.dlc, len(msg.data))):
            data += (f"{msg.data[index]:02x}")
        # treeview does not support autoscroll so I had to insert the new element at the first row
        self.table.insert(parent='', index=0, values=(msg.timestamp, msg.arbitration_id, msg.dlc, data, msg.channel))
        #
        time.sleep(2)

    def start(self):
        self.window.mainloop()

    def messageCallback(self, ms, function):
        msg: can.Message = function()
        if msg is not None:
            self.add(msg)

        self.window.after(ms, self.messageCallback, ms, function)

class TrafficDisplayer(object):
    def __init__(self, size='1150x200', ms=None, function=None):
        self.gui = GUI('CAN Bus Visualizer', size)
        if function is not None:
            self.gui.messageCallback(ms, function)
        self.gui.start()

if __name__ == '__main__':
    disp = TrafficDisplayer()
