import serial
import time
import paho.mqtt.client as paho
import configuration as config
broker=config.mqttBroker
port=int(config.mqttPort)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    print(response)
    

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
 
s = serial.Serial('/dev/ttyACM0', 9600) 
s.isOpen()
time.sleep(5)


try:
    while True:
        response = s.readline()
        if (b"Proximity/1" in response):
            response = s.readline()
            ret= client1.publish("Proximity/1",response)
        elif (b"Proximity/2" in response):
            response = s.readline()
            ret= client1.publish("Proximity/2",response)
        else:
            ret= client1.publish("Proximity/Error","Unexpected response")
                
                
except KeyboardInterrupt:
    s.close()