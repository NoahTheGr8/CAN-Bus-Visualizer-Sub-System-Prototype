import can
from tkinter import *
from tkinter import ttk

file = open("data.txt", 'w')

#socketcan allow us to run read can-utils messages
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=30000)
msg = can.Message(arbitration_id=0x01, data=[0,25, 0, 1, 3, 1, 4, 1], is_extended_id=False)

#bus.send(msg)

#Add data to a text file
for i in range(25):
    message = bus.recv()
    temp = str(message)     #convert data to string
    temp2 = temp.split()    #tokenize string
    time_stamp_var = temp2[1]
    canv0 = temp2[-1]
    info = temp2[3]
    returned_text = time_stamp_var + " " + canv0 + " " + info
    file.write(returned_text)
    file.write('\n')

file.close()

file2 = open('data.txt', 'r')
f = file2.readlines()

# Create lists
time_stamp = []
can0 = []
packet = []

for line in f:
    dump = line.split()
    time_stamp.append(dump[0])      # append the time stamp
    can0.append(dump[1])            # append can0
    packet.append(dump[2])          # append packets

# Gui
root = Tk()
root.title('CAN Bus Visualizer')
root.geometry("1000x200")

# Create table
table = ttk.Treeview(columns=('nodeID', 'CANName', 'nodeData'))
table.pack()

# Create names in columns
table.heading('#0', text="Time Stamp")
table.heading('#1', text="CAN Name")
table.heading('#2', text="Node Data")

# Insert dictionary into table

# todo print data vertically
for i in range(len(time_stamp)):
    table.insert("", "end", values=(time_stamp[i], can0[i], packet[i]))

root.mainloop()

file2.close()
