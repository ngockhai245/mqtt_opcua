from flask import Flask, render_template, request  # type: ignore
import paho.mqtt.client as mqtt # type: ignore

app = Flask(__name__)

# Kết nối đến Mosquitto broker
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    mqtt_client.publish("home/temperature", action)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
