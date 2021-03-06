# Truck-RC
    This is a set of little applications to control a Lego-Truck and extract data from on board sensors 
    such as:
    - Raspberry Pi CAM
    - Two HC SR/04 Proximity Sensors
    - SBrick
    The Data is gathered and streamed by a Arduino/Raspberry-Symbiosis over MQTT and can be accessed 
    from anywhere in the network. The code for the Raspberry and for the Arduino are also included in 
    this repository. The information for all Lego engines is transmitted by the SBrick. The SBrick is 
    connected via Bluetooth to the MQTT-Broker. A simple message to a certain topic can execute drive 
    and steer commands.
    
# Plug&Play Guide for tb.lx'ers
![Flowchart](/Img/FlowChart.jpg)

    If the camera does not open because of permission issues, just open in a new browser tab 
    '192.168.13.106:8000'
    Or the same with a different IP outside of woods.

# Requirements
    a variety of different libraries is used to receive, save, process, transmit and visualise the data.
    The used libraries will be listed here.
        - paho mqtt
        - kivy
        - kivy garden
        - kivy garden joystick (https://github.com/kivy-garden/garden.joystick) + 'garden install joystick'
        - tkinter
    all other libraries should be installed by default.

# How to use
    1. Raspberry:
        1a) For a new truck, arduino and RP you first have to perform the following steps in order to set 
        up the hardware the way you prefer. If everything is already set up, you can go directly to 
        the next section (1b):
            - set up the sensors, the sbrick and the raspberry
            - The easiest way to access the RP is by connecting a Keyboard, a mouse and a Screen (via HDMI)
            - make sure the proximity script (Truck-RC-Arduino) is running on the arduino
            and it is connected to the RP via the serial port
            - if not already done, install all necessary libraries on the RP
                - the SBrick Framework (https://github.com/BensonHsu/SBrick-Framework)
                - paho mqtt
                - mosquitto mqtt (https://mosquitto.org/)
                - io
                - picamera
                - logging
                - socketserver
                - http
            - make sure the mosquitto mqtt broker is set up and running
            - place the Truck-RC-RasPi folder on the RP in a directory of your choice and execute the 
            main.py in the mentioned folder
            -> everything should be running, nice!
            (If you want, you can call the main.py at startup with your method of choice (e.g. corntab).)
            (a connection via VNC/Viewer will also be helpful if you want to work on the PR in a 
            comfortable way)
        
        1b) For a already set up RP performe the following steps:
            - Turn on the Sbrick (by turning on the power of the lego modules)
            - Turn on the RP
            -> Done
            (in a new Network you will have to connect the RP to a Screen in order to establish the 
            necessary network connection in the usual way.)
            
    2. On your machine:
        - if the RP, Arduino and the Sbrick are set up and running, furthermore all necessary libraries 
        are installed you can now execute the applications
        - Clone the whole repository to your machine in a directory of your choice. 
        - Execute the main.py in the top directory
    
    -> DONE
