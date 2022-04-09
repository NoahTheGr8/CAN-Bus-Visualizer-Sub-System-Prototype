import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

# Open and read CAN bus data dump .txt format
file = open('small_sample.txt', 'r')
f = file.readlines()

# Create lists
one = []
two = []
three = []

# Save text file into lists
for line in f:
    dump = line.split()
    aa = dump[0]
    bb = dump[1]
    cc = dump[2]

    one.append(aa)
    two.append(bb)
    three.append(cc)
# Create dictionary with lists
CANBusData = {'nodeID': one, 'CANName': two, 'nodeData': three}

# dataList.append(line.strip())
# print(CANBusData)

# Gui
root = Tk()
root.title('CAN Bus Visualizer')
root.geometry("1000x200")

# Create table
table = ttk.Treeview(columns=('nodeID', 'CANName', 'nodeData'))
table.pack()

# Create names in columns
table.heading('#0', text="Node ID")
table.heading('#1', text="CAN Name")
table.heading('#2', text="Node Data")

# Insert dictionary into table

# todo print data vertically

table.insert("", 'end', values=(CANBusData['nodeID'], CANBusData['CANName'], CANBusData['nodeData']))
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
