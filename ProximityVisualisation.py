import tkinter as tk
import pickle


def update():
    try:
        Proximity1.set(str(pickle.load(open("Proximity1.p", "rb"))) + " cm")
        open("Proximity1.p", 'a').close()
    except EOFError:
        pass

    try:
        Proximity2.set(str(pickle.load(open("Proximity2.p", "rb"))) + " cm")
        open("Proximity2.p", 'a').close()
    except EOFError:
        pass

    top.after(50, update)


top = tk.Tk()
top.title("Proximity")

Proximity1 = tk.StringVar()
Proximity2 = tk.StringVar()
update()

Proximity1.set(str(pickle.load(open("Proximity1.p", "rb"))) + " cm")
Proximity2.set(str(pickle.load(open("Proximity2.p", "rb"))) + " cm")

frame = tk.Frame(top)
frame.pack()

Sens1 = tk.Label(top, textvariable=Proximity1, font="Helvetica 60 bold", height=1, width=20)
Sens1.pack()
Sens2 = tk.Label(top, textvariable=Proximity2, font="Helvetica 60 bold", height=1, width=20)
Sens2.pack()

top.mainloop()
