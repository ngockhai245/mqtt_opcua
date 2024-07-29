import paho.mqtt.client as mqtt # type: ignore
import time

#mosquiito broker
broker = 'localhost'
port = 1883

topics = ['home/temperature', 'home/humidity']

# topics_count = 0

#check connect to broker
def on_connect(client, userdata, flags, rc):#rc: reason_code
    if rc == 0:
        print("Connect to broker")
        #subscribe all topics
        for topic in topics:
            client.subscribe(topic)
    else:
        print("Connection failed")

#
def on_message(client, userdata, msg):
    global topics_count

    #decode message
    message = msg.payload.decode()

    print(f"Received '{message}' from topic '{msg.topic}'")

#create client instance
client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect(broker, port)

client.loop_forever()