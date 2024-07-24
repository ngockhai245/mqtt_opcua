import random
import time
import paho.mqtt.client as mqtt # type: ignore
import ssl
import logging

#local Mosquitto broker
broker = 'localhost'
port = 1883

#topics
humidity_topic = 'home/humidity'
temperature_topic = 'home/temperature'

#function check connect to broker
def on_connect(client, userdata, flags, rc):
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

        #TEMPERATURE
        random_temperature_data = random.randint(10, 60)
        temperature_result = client.publish(temperature_topic, random_temperature_data)

        #check if publish success
        temperature_status = temperature_result[0]
        if temperature_status == 0:
            print(f"Send '{random_temperature_data}' to topic '{temperature_topic}'")
        else:
            print("Failed!")



        #HUMIDITY
        random_humidity_data = random.randint(0, 100)
        humidity_result = client.publish(humidity_topic, random_humidity_data)

        #check if publish success
        humidity_status = humidity_result[0]
        if humidity_status == 0:
            print(f"Send '{random_humidity_data}' to topic '{humidity_topic}'")
        else:
            print("Failed!")



        # print("-------------------------------")
        #interval between sends
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")

#stop and disconnect
client.loop_stop()
client.disconnect()