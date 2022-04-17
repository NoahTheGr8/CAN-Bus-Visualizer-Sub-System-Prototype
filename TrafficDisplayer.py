import tkinter
from tkinter import *
from tkinter import ttk
import can
import signal
import sys
import os
import copy
from PacketManager import PacketManager

class GUI(object):
    def __init__(self, title, size, can_bus, p1, p2):
        '''
        For soft 2 - relocate these attributes to another class. This is only here for making prototype work within deadline

        :param can_bus: - the bus object
        :param p1: - the speedometer UI process
        :param p2: - the controller UI process
        :param function: - the function that recieves packets
        '''
        self.temp_traffic_storage = [] #This holds all messages for the session
        self.can_bus = can_bus #this is the can bus that has been passed from Controller.py
        self.p1 = p1 #this is the proccess thats displaying the speedometer
        self.p2 = p2 #this is the process thats displaying the controller

        # Create window
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(size)

        # Create menu
        self.menu = Menu(self.window, tearoff=False)
        self.menu.add_command(label='Save Packet')
        self.menu.add_command(label='Edit Packet', command=lambda: self.openEditWindow(title='Edit Packet', size='500x115'))
        self.menu.add_command(label='Replay Packet', command=lambda: self.replayPacket(self.table.index(self.table.selection())))
        self.menu.add_command(label='Annotate Packet')
        self.menu.add_command(label='Delete Packet')
        self.menu.add_separator()
        self.menu.add_command(label='Show Packet Edits', command=lambda: self.openVersionWindow(title='Packet Modifications', size='1100x400'))

        # Bind right click to menu
        self.window.bind('<Button-3>', self.openMenu)

        # Create frame
        self.frame = Frame(self.window)
        self.frame.pack(padx=15,
                        pady=15,
                        side=TOP,
                        expand=True,
                        fill=BOTH)

        # Create table
        self.table = ttk.Treeview(master=self.frame,
                                  columns=('Timestamp', 'ID', 'DL', 'DATA', 'Channel'),
                                  show='headings'
                                  )
        self.table.pack(side=LEFT, expand=True, fill=BOTH)

        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(master=self.frame,
                                       orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure table to scroll vertically with scrollbar
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.table.yview)

        # Create columns
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', anchor=CENTER)
        self.table.column('#2', anchor=CENTER)
        self.table.column('#3', anchor=CENTER)
        self.table.column('#4', anchor=CENTER)
        self.table.column('#5', anchor=CENTER)

        # Create headings
        self.table.heading('#0', text='')
        self.table.heading('#1', text='Timestamp', anchor=CENTER)
        self.table.heading('#2', text='ID', anchor=CENTER)
        self.table.heading('#3', text='DL', anchor=CENTER)
        self.table.heading('#4', text='Data', anchor=CENTER)
        self.table.heading('#5', text='Channel', anchor=CENTER)

        #added a button to stop session - Closes main UI
        self.stop_button = Button(master=self.window, text='Stop Sesssion', command=lambda: self.stopSession())
        self.stop_button.pack(side=BOTTOM, pady=15)

    #packet_index is the index of the packet in reference to the table on the Traffic View.
    def replayPacket(self, packet_index):
        #Get tree selected index
        poi = self.temp_traffic_storage[packet_index].message #this is the packet of interest they right clicked on
        self.can_bus.send(poi) #transmit the packet back to the CAN Bus
        self.add(poi) #add the packet to the traffic view
        self.temp_traffic_storage.append(self.temp_traffic_storage[packet_index]) #add the packet to the traffic temporary file

    #stops the session and closes the UI
    def stopSession(self):
        os.killpg(os.getpgid(self.p1.pid), signal.SIGTERM) #close the speedometer UI
        os.killpg(os.getpgid(self.p2.pid), signal.SIGTERM) #close the controlller UI
        sys.exit(0) #close the traffic view

    def add(self, msg: can.Message):
        packet = PacketManager(msg)
        self.temp_traffic_storage.append(packet)
        data = '0x'
        for index in range(0, min(msg.dlc, len(msg.data))):
            data += f"{msg.data[index]:02x}"
        self.table.insert(parent='',
                          index='end',
                          values=(msg.timestamp, msg.arbitration_id, msg.dlc, data, msg.channel))

        #time.sleep(0.9) #to contol the flow of the packets

    def start(self):
        self.window.mainloop()

    def messageCallback(self, ms, function):
        msg: can.Message = function()
        if msg is not None:
            self.temp_traffic_storage.append(PacketManager(msg))
            self.add(msg)
            # self.table.yview_moveto(1)  # Allows autoscroll

        #The 1000 below specifies that 1000 milliseconds = 1 sec will pass until the next invocation of callback which also means 1s until next packet is read
        if len(self.temp_traffic_storage) < 25: #for sake of demo - we will only show x packets
            self.window.after(ms, self.messageCallback, 1000, function)

    def openMenu(self, e):
        self.menu.tk_popup(e.x_root, e.y_root)

    def openVersionWindow(self, title, size):
        # Get tree selected index
        index = self.table.focus()
        items = self.table.item(index)

        if len(items['values']) < 1:
            print('A packet was not selected')
            pass

        # Create Top Window
        self.top_window = Toplevel(self.window)
        self.top_window.title(title)
        self.top_window.geometry(size)

        # Create frame
        self.top_window.frame = Frame(self.top_window)
        self.top_window.frame.pack(padx=15,
                        pady=15,
                        side=TOP,
                        expand=True,
                        fill=BOTH)

        # Create table
        self.top_window.table = ttk.Treeview(master=self.top_window.frame,
                                  columns=('Timestamp', 'ID', 'DL', 'DATA', 'Channel'),
                                  show='headings'
                                  )
        self.top_window.table.pack(side=LEFT, expand=True, fill=BOTH)

        # Create scrollbar
        self.top_window.scrollbar = ttk.Scrollbar(master=self.top_window.frame,
                                       orient=VERTICAL)
        self.top_window.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure table to scroll vertically with scrollbar
        self.top_window.table.configure(yscrollcommand=self.top_window.scrollbar.set)
        self.top_window.scrollbar.configure(command=self.top_window.table.yview)

        # Create columns
        self.top_window.table.column('#0', width=0, stretch=NO)
        self.top_window.table.column('#1', anchor=CENTER)
        self.top_window.table.column('#2', anchor=CENTER)
        self.top_window.table.column('#3', anchor=CENTER)
        self.top_window.table.column('#4', anchor=CENTER)
        self.top_window.table.column('#5', anchor=CENTER)

        # Create headings
        self.top_window.table.heading('#0', text='')
        self.top_window.table.heading('#1', text='Timestamp', anchor=CENTER)
        self.top_window.table.heading('#2', text='ID', anchor=CENTER)
        self.top_window.table.heading('#3', text='DL', anchor=CENTER)
        self.top_window.table.heading('#4', text='Data', anchor=CENTER)
        self.top_window.table.heading('#5', text='Channel', anchor=CENTER)

        index = self.table.index(self.table.selection())
        packet = self.temp_traffic_storage[index]
        for msg in packet.get():
            data = '0x'
            for index in range(0, min(msg.dlc, len(msg.data))):
                data += f"{msg.data[index]:02x}"
            self.top_window.table.insert(parent='',
                              index='end',
                              values=(msg.timestamp, msg.arbitration_id, msg.dlc, data, msg.channel))

    def openEditWindow(self, title, size):
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
        index = self.table.index(self.table.selection())
        packet = self.temp_traffic_storage[index]
        data = str(text.get(1.0, 'end-1c'))
        data = bytearray(bytes.fromhex(data[2:]))
        msg = copy.copy(packet.message)
        msg.data = data
        packet.add(msg)
        if window is not None:
            window.destroy()


class TrafficDisplayer(object):
    def __init__(self, canbus=None, size='1150x400', ms=None, function=None, p1=None, p2=None):
        self.gui = GUI('CAN Bus Visualizer', size, canbus, p1, p2)
        if function is not None:
            self.gui.messageCallback(ms, function) #pass the can bus as well
        self.gui.start()


if __name__ == '__main__':
    disp = TrafficDisplayer()
