# Truck-RC
    This is a set of little applications to control a Lego-Truck and extract data from on board sensors such as
    - Raspberry Pi CAM
    - Two HC SR/04 Proximity Sensors
    - SBrick
    The Data is gathered and streamed by a Arduino/Raspberry-Symbiosis over MQTT and can be accessed from
    anywhere in the network. The code for the Raspberry and for the Arduino are also included in this repository.
    The information for all Lego engines is transmitted by the SBrick. The SBrick is connected via Bluetooth to the
    MQTT-Broker. A simple message to a certain topic can execute drive and steer commands.

# Requirements
    a variety of different libraries is used to receive, save, process, transmit and visualize the data.
    The used libraries will be listed here. You can install dem on your own for Python3 or just execute the
    install.py script.
        - paho mqtt
        - kivy
        - kivy garden
        - kivy garden joystick (https://github.com/kivy-garden/garden.joystick)
        - tkinter
    all other libraries should be installed by default.

# How to use
    - set up the sensors, the sbrick and the raspberry
    - make sure the proximity script (Truck-RC-Arduino) is running on the arduino
      and it is connected to the RP via the serial port
    - if not already done, install all necessary libraries on the RP
        - the SBrick Framework (https://github.com/BensonHsu/SBrick-Framework)
        - tkinter
        - paho mqtt
        - mosquitto mqtt (https://mosquitto.org/)
        - io
        - picamera
        - logging
        - socketserver
        - http
    - make sure the mosquitto mqtt broker is set up and running
    - place the Truck-RC-RasPi folder on the RP at a location of your choice and execute the main.py in the
      mentioned folder -> find the ip-address of your mqtt broker -> everything should be running, nice!
    - Place the whole repository on your machine. execute the main.py in the top directory

-> DONE

# Documentation
    For further Documentation about the individual scrips look into the "Documentation" folder