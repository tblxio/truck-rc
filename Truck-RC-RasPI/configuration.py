#!/usr/bin/env python
import os
# Root topic
rootTopic = "truck1"
dirname=os.path.dirname(__file__)
# Broker configuration
mqttPort = "1883"

mqttUser = "techhub"
mqttPasswd = "dtbhub2019"

IP= open(dirname+'/ip.txt','r')
mqttBroker = str(IP.readlinas8+)
mqttBroker = mqttBroker.replace("'","")
mqttBroker = mqttBroker.replace("[","")
mqttBroker = mqttBroker.replace("]","")

# Components configuration
componentDic = {
    "imuClass": "Imu",
    "proximityClass": "ProximitySensor",
    "motorClass": "Motor",
    "cameraClass": "Camera"}
# Has to be float
componentsSamplingIntevalInSeconds = {
    "imuClass": 0.1,
    "proximityClass": 0.4,
    "motorClass": 10,
    "cameraClass": 100.0}
