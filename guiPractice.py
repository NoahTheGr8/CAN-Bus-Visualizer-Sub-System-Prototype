import tkinter as tk
from tkinter import ttk


class Gui:
    def __init__(self, master):
        style = ttk.Style()
        print(style.theme_names())
        style.theme_use("classic")

        col = ('column2', 'column3', 'column...')
        self.treeview = ttk.Treeview(master, columns=col, height=20)
        self.treeview.pack(padx=5, pady=5)

        self.treeview.heading('#0', text="Time Stamp")
        self.treeview.heading('column2', text="CAN Bus")
        self.treeview.heading('column3', text="Raw Packet")
        self.treeview.heading('column...', text="Column...")

        self.read_data()

    def read_data(self):
        file = open("small_sample.txt", 'r')

        for index, line in enumerate(file):
            values = line.rstrip().split(' ')
            self.treeview.insert('', tk.END, iid=index, text=values[0], values=values[1:])
        # Create lists
        # time_stamp = []
        # can0 = []
        # packet = []
        #
        # # Save text file into lists
        # for line in file:
        #     dump = line.split()
        #     aa = dump[0]
        #     bb = dump[1]
        #     cc = dump[2]
        #     time_stamp.append(aa)
        #     can0.append(bb)
        #     packet.append(cc)
        #
        #
        # # Create dictionary with lists
        # for i in range(len(time_stamp)):
        #     self.treeview.insert("", "end", values=(time_stamp[i], can0[i], packet[i], ))


root = tk.Tk()
window = Gui(root)
root.mainloop()
