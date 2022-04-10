import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

# Open and read CAN bus data dump .txt format
file = open('data.txt', 'r')
f = file.readlines()

# Create lists
time_stamp = []
can0 = []
packet = []

# Save text file into lists
for line in f:
    dump = line.split()
    time_stamp.append(dump[0]) #append the time stamp
    can0.append(dump[1]) #append can0
    packet.append(dump[2]) #append packets

# Gui
root = Tk()
root.title('CAN Bus Visualizer')
root.geometry("1000x2000")

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


# I tried to use a internal database.

# # Crate Database
# conn = sqlite3.connect('CAN_Bus_DB.db')
#
# # Create cursor
# c = conn.cursor()
#
# c.execute("""CREATE TABLE traffic (
#          node_name text,
#          node_ID text,
#          node_information text
#          )""")
#
# # Commit changes
# conn.commit()
# # Close connection
# conn.close()
#
# root.mainloop()