import os
import tkinter as tk

print("IPselect.py launched")

dirname = os.path.dirname(__file__)
IP = open(dirname + '/config/ip.txt', 'r')
oldIP = str(IP.readlines())  # 192.168.13.106
oldIP = oldIP.replace("'", "")
oldIP = oldIP.replace("[", "")
oldIP = oldIP.replace("]", "")
IP.close()

def NewCB(self):
    os.remove(dirname + '/config/ip.txt')
    NewIP = open(dirname + '/config/ip.txt', 'w')
    NewIP.write(Entry.get())
    NewIP.close()
    IPselect.destroy()

def OldCB():
    IPselect.destroy()

IPselect = tk.Tk()
frame = tk.Frame(IPselect)
frame.pack()

BtnNew = tk.Button(IPselect, text="Enter new IP:", font="Helvetica 40 bold", command=NewCB, height=1, width=15)
BtnOld = tk.Button(IPselect, text="Keep old IP:", font="Helvetica 40 bold", command=OldCB, height=1, width=15)
Entry = tk.Entry(IPselect, width=15)
Entry.bind('<Return>', NewCB)
LableIP = tk.Label(IPselect, text=oldIP, font="Helvetica 25 bold", height=1, width=20)

BtnNew.pack()
Entry.pack()
BtnOld.pack()
LableIP.pack()

IPselect.mainloop()
