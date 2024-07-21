import random
import time
import paho.mqtt.client as mqtt # type: ignore

#MQTT Broker details
broker = 'localhost' #local Mosquitto broker
port = 1883
topic = 'test/random_data'

#function to connect to broker
def on_connect(client, user_data, flags, rc):
    if rc == 0:
        print("Connected to Mosquitto broker")
    else:
        print("Connection failed!")

#MQTT client
client = mqtt.Client()

#on_connect callback function
client.on_connect = on_connect

#connect to broker
client.connect(broker, port)

client.loop_start()

try:
    while True:
        random_data = random.randint(20, 45)
        result = client.publish(topic, random_data)

        #check if publish success
        status = result[0]
        if status == 0:
            print(f"Send '{random_data}' to topic '{topic}'")
        else:
            print("Failed!")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

#stop and discnnect
client.loop_stop()
client.disconnect()