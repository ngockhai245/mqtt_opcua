import paho.mqtt.client as mqtt # type: ignore
import json
import time
import random

# Thông tin MQTT Broker
broker = 'localhost'
port = 1883
data_topic = 'sensor/data'

# Tạo dữ liệu ngẫu nhiên từ các sensor
def get_random_sensor_data():
    sensor_data = {
        'temperature': round(random.uniform(20, 40), 2),
        'humidity': round(random.uniform(30, 70), 2),
        'light': random.randint(0, 100),
        'motion': random.choice(['Yes', 'No'])
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
    
    # Gửi dữ liệu lên topic
    client.publish(data_topic, payload)
    
    # In ra màn hình để kiểm tra
    print(f'Sent: {payload}')
    
    # Đợi x giây trước khi gửi dữ liệu lần tiếp theo
    time.sleep(10)

