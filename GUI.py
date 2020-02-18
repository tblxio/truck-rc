from kivy.clock import Clock
from kivy.app import App
from kivy.garden.joystick import Joystick
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os
from mqttClient import MqttClient
import controllerMessages as messages
import sys
import json
import webbrowser
from config import configuration as config

print("GUI.py launched")
x = 0
y = 0
magnitude = 0

webbrowser.open(config.mqttBroker + ":8000")

sys.path.append('..')


# Connect to the client and subscribe to the necessary topics
drive_topic = "sbrick/01/sp/drive"
my_client = MqttClient()
my_client.setup_client()

clear = lambda: os.system('clear')

class DemoApp(App):

    def build(self):
        self.root = BoxLayout()
        self.root.padding = 25
        joystick = Joystick()
        joystick.bind(pad=self.update_coordinates)
        self.root.add_widget(joystick)
        self.label = Label()

    def update_coordinates(self, joystick, pad):
        global x
        global y
        global magnitude
        x = str(pad[0])[0:5]
        y = str(pad[1])[0:5]
        radians = str(joystick.radians)[0:5]
        magnitude = str(joystick.magnitude)[0:5]
        angle = str(joystick.angle)[0:5]
        text = "x: {}\ny: {}\nradians: {}\nmagnitude: {}\nangle: {}"
        self.label.text = text.format(x, y, radians, magnitude, angle)
        #clear()
        #print(text.format(x, y, radians, magnitude, angle))

    def my_callback(dt):
        global y
        global x
        global magnitude
        my_client.publish(drive_topic, json.dumps(messages.getMsgDrive(float(y), float(magnitude)), sort_keys=True))
        my_client.publish(drive_topic, json.dumps(messages.getMsgSteer(float(x)), sort_keys=True))

    event = Clock.schedule_interval(my_callback, 1 / 10)

DemoApp().run()
