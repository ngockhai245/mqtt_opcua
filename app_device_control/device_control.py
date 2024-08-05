import paho.mqtt.client as mqtt # type: ignore
import json

# Thông tin MQTT Broker
broker = "localhost"
port = 1883
control_topic = "device/control"

def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    data = json.loads(payload)
    board_id = data['board_id']
    device_id = data['device_id']
    state = data['state']
    if board_id == 1:
        print(f"Board 1, Device {device_id} received command: {state}")

    if board_id == 2:
        print(f"Board 2, Device {device_id} received command: {state}")

        
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(control_topic)
client.loop_forever()
