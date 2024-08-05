from flask import Flask, render_template, jsonify # type: ignore
import paho.mqtt.client as mqtt # type: ignore
import json

app = Flask(__name__)

# Thông tin MQTT Broker
broker = "localhost"
port = 1883
topic = "sensor/data"

# Biến toàn cục để lưu trữ dữ liệu sensor
sensor_data = {}

# Hàm callback khi nhận được message từ MQTT Broker
def on_message(client, userdata, message):
    global sensor_data
    payload = message.payload.decode('utf-8')
    sensor_data = json.loads(payload)
    print(f"Received: {sensor_data}")

# Kết nối đến MQTT Broker
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(topic)
client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data')
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
