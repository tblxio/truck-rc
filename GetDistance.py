import pickle
import paho.mqtt.client as mqtt
import statistics
import os
from config import configuration as config

clear = lambda: os.system('clear')

print("GetDistance.py launched")

# define variables
Proximity_1_values = ["150", "150", "150", "150", "150", "150", "150", "150", "150", "150"]
Proximity_1_value = 0
Proximity_1_idx = 0
Proximity_1_dist = 0
Proximity_1_150count = 0

Proximity_2_values = ["150", "150", "150", "150", "150", "150", "150", "150", "150", "150"]
Proximity_2_value = 0
Proximity_2_idx = 0
Proximity_2_dist = 0
Proximity_2_150count = 0

db = {}


def resetValues(Sens):
    idx = 0
    global Proximity_1_values
    global Proximity_2_values
    if (Sens == 1):
        while (idx < 10):
            Proximity_1_values[idx] = 150
            idx = idx + 1

    if (Sens == 2):
        while (idx < 10):
            Proximity_2_values[idx] = 150
            idx = idx + 1


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe([("Proximity/2", 1), ("Proximity/1", 0)])


def on_message(client, userdata, msg):

    if (msg.topic == "Proximity/1"):
        global Proximity_1_idx
        global Proximity_1_values
        global Proximity_1_value
        global Proximity_1_150count
        global Proximity_1_dist
        Proximity_1_value = int(msg.payload.decode())

        if (Proximity_1_value <= 150):
            Proximity_1_values[Proximity_1_idx] = Proximity_1_value
            Proximity_1_idx = Proximity_1_idx + 1
            Proximity_1_dist = statistics.median(map(float, Proximity_1_values))
            Proximity_1_150count = 0

        else:
            Proximity_1_150count = Proximity_1_150count + 1
            if (Proximity_1_150count > 10):
                Proximity_1_150count = 0
                resetValues(1)
                Proximity_1_dist = statistics.median(map(float, Proximity_1_values))
                clear()

        if (Proximity_1_idx == 10): Proximity_1_idx = 0

    if (msg.topic == "Proximity/2"):
        global Proximity_2_idx
        global Proximity_2_values
        global Proximity_2_value
        global Proximity_2_150count
        global Proximity_2_dist
        Proximity_2_value = int(msg.payload.decode())

        if (Proximity_2_value <= 150):
            Proximity_2_values[Proximity_2_idx] = Proximity_2_value
            Proximity_2_idx = Proximity_2_idx + 1
            Proximity_2_dist = statistics.median(map(float, Proximity_2_values))
            Proximity_2_150count = 0

        else:
            Proximity_2_150count = Proximity_2_150count + 1
            if (Proximity_2_150count > 10):
                Proximity_2_150count = 0
                resetValues(2)
                Proximity_2_dist = statistics.median(map(float, Proximity_2_values))
                clear()

        if (Proximity_2_idx == 10): Proximity_2_idx = 0

    db['Proximity1'] = Proximity_1_dist
    db['Proximity2'] = Proximity_2_dist
    pickle.dump(Proximity_1_dist, open("Proximity1.p", "wb"))
    pickle.dump(Proximity_2_dist, open("Proximity2.p", "wb"))
    open("Proximity1.p", 'a').close()
    open("Proximity2.p", 'a').close()
    #clear()
    #print(Proximity_1_values)
    #print(Proximity_2_values)


client = mqtt.Client()
client.connect(config.mqttBroker, 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
