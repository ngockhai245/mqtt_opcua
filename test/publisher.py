import paho.mqtt.client as mqtt # type: ignore
import json
import time
import random

# Thông tin MQTT Broker
broker = "localhost"
port = 1883
topic = "sensor/data"

# Tạo dữ liệu ngẫu nhiên từ các sensor
def get_random_sensor_data():
    sensor_data = {
        "temperature": round(random.uniform(20.0, 30.0), 2), 
        "humidity": random.randint(30, 70), 
        "light": random.randint(0, 1000), 
        "motion": random.choice(['Yes', 'No']) 
    }
    return sensor_data

# Kết nối MQTT Client
client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    # Lấy dữ liệu ngẫu nhiên từ các sensor
    data = get_random_sensor_data()
    # Chuyển dữ liệu thành JSON
    payload = json.dumps(data)

    client.publish(topic, payload)

    print(f"Sent: {payload}")
    
    time.sleep(10)
