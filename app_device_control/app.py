from flask import Flask, render_template, jsonify # type: ignore
from flask_socketio import SocketIO, emit # type: ignore
import paho.mqtt.client as mqtt # type: ignore
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Thông tin MQTT Broker
broker = "localhost"
port = 1883
control_topic = "device/control"
data_topic = "sensor/data"

# Kết nối đến MQTT Broker
client = mqtt.Client()

# Biến toàn cục để lưu trữ dữ liệu sensor
sensor_data = {}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with the result code: {rc}")
    client.subscribe(data_topic)

def on_message(client, userdata, message):
    global sensor_data
    payload = message.payload.decode('utf-8')
    sensor_data = json.loads(payload)
    print(f"Received: {sensor_data}")
    # socketio.emit('sensor_data', sensor_data)

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data')
def get_sensor_data():
    return jsonify(sensor_data)

@socketio.on('control_device')
def handle_control_device(data):
    # Dữ liệu từ client chứa 'board_id', 'device_id' và 'state'
    board_id = data['board_id']
    device_id = data['device_id']
    state = data['state']
    payload = json.dumps({'board_id': board_id, 'device_id': device_id, 'state': state})
    client.publish(control_topic, payload)
    print(f"Sent control command: {payload}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
