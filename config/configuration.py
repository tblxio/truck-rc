#!/usr/bin/env python
import os
dirname = os.path.dirname(__file__)

# Root topic
rootTopic = "truck1"

# Broker configuration

mqttPort = "1883"

mqttUser = "techhub"
mqttPasswd = ""

IP = open(dirname+'/ip.txt','r')
mqttBroker = str(IP.readlines())  # 192.168.13.106
mqttBroker = mqttBroker.replace("'", "")
mqttBroker = mqttBroker.replace("[", "")
mqttBroker = mqttBroker.replace("]", "")
