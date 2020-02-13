from lib.sbrick_m2mipc import SbrickIpcClient

# MQTT connect
client = SbrickIpcClient(broker_ip='207.154.232.115', broker_port=1883,broker_user="techhub",broker_passwd="dtbhub2019" )
client.connect()

# Get voltage and temperature of a SBrick device
json_response = client.rr_get_adc(sbrick_id='88:6B:0F:80:29:D1', timeout=5)
print(json_response)

# Get information of UUID, sercies and characteristics of a SBrick device
#json_response = client.rr_get_service(sbrick_id='11:22:33:44:55:66', timeout=5)

# Get general information of a SBrick device
#json_response = client.rr_get_general(sbrick_id='11:22:33:44:55:66', timeout=5)

# Stop power functions
#client.publish_stop(sbrick_id='11:22:33:44:55:66', channel_list=['00', '01'])

# Drive a power function
#client.publish_drive(sbrick_id='11:22:33:44:55:66',
#                     channnel='00',
#                     direction='00',
#                    # power='f0',
                     #exec_time=10)
                 
# MQTT disconnect
client.disconnect()
