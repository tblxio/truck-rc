import os
import configuration as config

dirname = os.path.dirname(__file__)
IP=config.mqttBroker

os.system(f'sudo python3 {dirname}/SBrick-Framework/sbrick_server.py --connect --broker-ip {IP} --broker-port 1883 --log-level debug --sbrick-id 88:6B:0F:80:29:D1')