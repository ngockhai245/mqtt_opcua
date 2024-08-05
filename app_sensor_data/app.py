from flask import Flask, render_template # type: ignore
from flask_socketio import SocketIO, emit # type: ignore
import paho.mqtt.client as mqtt # type: ignore
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Thông tin MQTT Broker
broker = "localhost"
port = 1883
data_topic = "sensor/data"

# Hàm callback khi nhận được message từ MQTT Broker
def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    sensor_data = json.loads(payload)
    print(f"Received: {sensor_data}")
    socketio.emit('sensor_data', sensor_data)

# Kết nối đến MQTT Broker
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(data_topic)
client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
