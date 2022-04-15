from tkinter import *
from tkinter import ttk
import can

class GUI(object):
    def __init__(self, title, size):
        # Create window
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(size)

        # Create menu
        self.menu = Menu(self.window, tearoff=False)
        self.menu.add_command(label='Save Packet')
        self.menu.add_command(label='Edit Packet', command=lambda: self.openWindow(title='Edit Packet', size='500x115'))
        self.menu.add_command(label='Replay Packet')
        self.menu.add_command(label='Annotate Packet')
        self.menu.add_command(label='Delete Packet')

        # Bind right click to menu
        self.window.bind('<Button-3>', self.openMenu)

        # Create frame
        self.frame = Frame(master=self.window)
        self.frame.pack(padx=15, pady=15, expand=True, fill=BOTH)

        # Create table
        self.table = ttk.Treeview(master=self.frame, columns=('Timestamp', 'ID', 'DL', 'DATA', 'Channel'), show='headings')
        self.table.pack(side=LEFT, expand=True, fill=BOTH)

        # Create scrollbar
        self.scrollbar = Scrollbar(master=self.frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure table to scroll vertically with scrollbar
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.table.yview)

        # Create columns
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', anchor=NW)
        self.table.column('#2', anchor=NW)
        self.table.column('#3', anchor=NW)
        self.table.column('#4', anchor=NW)
        self.table.column('#5', anchor=NW)

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
        self.table.insert(parent='', index='end', values=(msg.timestamp, msg.arbitration_id, msg.dlc, data, msg.channel))

    def start(self):
        self.window.mainloop()

    def messageCallback(self, ms, function):
        msg: can.Message = function()
        if msg is not None:
            self.add(msg)

        self.window.after(ms, self.messageCallback, ms, function)

    def openMenu(self, e):
        self.menu.tk_popup(e.x_root, e.y_root)

    def openWindow(self, title, size):
        # Get tree selected index
        index = self.table.focus()
        items = self.table.item(index)

        if len(items['values']) > 0:
            # Create Top Window
            self.top_window = Toplevel(self.window)
            self.top_window.title(title)
            self.top_window.geometry(size)

            # Create Frame
            self.top_window.frame = Frame(master=self.top_window)

            # Create Label
            self.top_window.label = Label(master=self.top_window.frame, text='Edit Packet Data: ', justify=LEFT)

            # Create Text Box
            self.top_window.text_box = Text(master=self.top_window.frame, height=1, width=int(size.split('x')[0])//12)

            # Pack All to Top Window
            self.top_window.frame.pack(pady=15)
            self.top_window.label.pack(side=LEFT)
            self.top_window.text_box.pack(side=LEFT)

            # Insert current msg.data into text box
            self.top_window.text_box.insert(INSERT, items['values'][3])

            # Create Button Frame
            self.top_window.button_frame = Frame(master=self.top_window)

            # Create Buttons - Update and Cancel
            self.top_window.update = Button(master=self.top_window.button_frame, text='Update Packet',
                                            command=lambda: self.update(index, self.top_window.text_box, self.top_window))
            self.top_window.replay = Button(master=self.top_window.button_frame, text='Replay Packet')
            self.top_window.cancel = Button(master=self.top_window.button_frame, text='Cancel',
                                            command=self.top_window.destroy)

            # Pack Buttons
            self.top_window.button_frame.pack(side=BOTTOM, padx=15, pady=15)
            self.top_window.update.pack(side=LEFT, anchor=E, padx=15)
            self.top_window.replay.pack(side=LEFT, anchor=E, padx=15)
            self.top_window.cancel.pack(side=LEFT, anchor=E, padx=15)

            # Lock window size
            self.top_window.resizable(False, False)
        else:
            print('A packet was not selected')

    def update(self, index, text: Text, window: Toplevel=None):
        items = self.table.item(index)
        values = items['values']
        self.table.item(index, text='', values=(values[0], values[1], values[2], text.get(1.0, 'end-1c'), values[4]))
        if window is not None:
            window.destroy()


class TrafficDisplayer(object):
    def __init__(self, size='1150x200', ms=None, function=None):
        self.gui = GUI('CAN Bus Visualizer', size)
        if function is not None:
            self.gui.messageCallback(ms, function)
        self.gui.start()


if __name__ == '__main__':
    disp = TrafficDisplayer()
