import paho.mqtt.client as mqtt # type: ignore

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("home/temperature")

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}, Message: {msg.payload.decode()}")
    action = msg.payload.decode()
    if action == "ON":
        print("Turning on the fan.")

    elif action == "OFF":
        print("Turning off the fan.")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)
client.loop_forever()
