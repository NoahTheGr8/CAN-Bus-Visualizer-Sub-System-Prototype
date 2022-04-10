from tkinter import *
from tkinter import ttk

import can


class GUI(object):
    def __init__(self, title, size):
        # Create window
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(size)

        # Create table and columns
        self.table = ttk.Treeview(columns=('Timestamp', 'ID', 'DL', 'Channel'))
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', anchor=NW)
        self.table.column('#2', anchor=NW)
        self.table.column('#3', anchor=NW)
        self.table.column('#4', anchor=NW)

        # Create headings
        self.table.heading('#0', text='')
        self.table.heading('#1', text='Timestamp', anchor=CENTER)
        self.table.heading('#2', text='ID', anchor=CENTER)
        self.table.heading('#3', text='DL', anchor=CENTER)
        self.table.heading('#4', text='Channel', anchor=CENTER)

        self.table.pack()

    def add(self, msg: can.Message):
        self.table.insert(parent='', index='end', values=(msg.timestamp, msg.arbitration_id, msg.dlc, msg.channel))

    def start(self):
        self.window.mainloop()

    def messageCallback(self, ms, function):
        msg: can.Message = function()
        if msg is not None:
            self.add(msg)

        self.window.after(ms, self.messageCallback, ms, function)


class TrafficDisplayer(object):
    def __init__(self, ms=None, function=None):
        self.gui = GUI('CAN Bus Visualizer', '1000x200')
        if function is not None:
            self.gui.messageCallback(ms, function)
        self.gui.start()


if __name__ == '__main__':
    disp = TrafficDisplayer()