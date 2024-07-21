import random
import time
import paho.mqtt.client as mqtt # type: ignore
import ssl
import logging

#MQTT Broker 
broker = 'localhost' #local Mosquitto broker
port = 1883

#topics
humidity_topic = 'home/humidity'
temperature_topic = 'home/temperature'

#ham kiem tra ket noi den broker
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

        #HUMIDITY
        random_humidity_data = random.uniform(0, 100)
        humidity_result = client.publish(humidity_topic, random_humidity_data)

        #kiem tra neu publish data thanh cong
        humidity_status = humidity_result[0]
        if humidity_status == 0:
            print(f"Send '{random_humidity_data}' to topic '{humidity_topic}'")
        else:
            print("Failed!")



        #TEMPERATURE
        random_temperature_data = random.uniform(20, 45)
        temperature_result = client.publish(temperature_topic, random_temperature_data)

        #kiem tra neu publish data thanh cong
        temperature_status = temperature_result[0]
        if temperature_status == 0:
            print(f"Send '{random_temperature_data}' to topic '{temperature_topic}'")
        else:
            print("Failed!")



        print("-------------------------------")
        #gui sau bao nhieu giay
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting...")

#stop va disconnect
client.loop_stop()
client.disconnect()