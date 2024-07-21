import paho.mqtt.client as mqtt # type: ignore
import time

#mosquiito broker
broker = 'localhost'
port = 1883

topics = ['home/humidity', 'home/temperature']

topics_count = 0

#kiem tra ket noi voi broker
def on_connect(client, userdata, flags, rc):#rc: reason_code
    if rc == 0:
        print("Connect to broker")
        #subscribe topics
        for topic in topics:
            client.subscribe(topic)
    else:
        print("Connection failed")

#
def on_message(client, userdata, msg):
    global topics_count

    #giai ma noi dung tin nhan
    message = msg.payload.decode()
    #in 
    print(f"Received '{message}' from topic '{msg.topic}'")

    topics_count += 1

    if topics_count == len(topics):
        print("-------------------------------")
        topics_count = 0



client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect(broker, port)

client.loop_forever()