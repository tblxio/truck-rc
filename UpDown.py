from mqttClient import MqttClient
import controllerMessages as messages
import tkinter as tk
import json

drive_topic = "sbrick/01/sp/drive"
my_client = MqttClient()
my_client.setup_client()

def UpCallBack():
    my_client.publish(drive_topic, json.dumps(messages.getMsgUp(), sort_keys=True))


def DownCallBack():
    my_client.publish(drive_topic, json.dumps(messages.getMsgDown(), sort_keys=True))

top = tk.Tk()
top.title("TrailerControl")
frame = tk.Frame(top)
frame.pack()
top.geometry("200x135")

BtnUp = tk.Button(top, text="     Up      ", font="Helvetica 50 bold", command=UpCallBack)
BtnUp.pack()
BtnDown = tk.Button(top, text=" Down ", font="Helvetica 60 bold", command=DownCallBack)
BtnDown.pack()

top.mainloop()

