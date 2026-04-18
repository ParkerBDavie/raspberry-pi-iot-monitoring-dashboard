import time
import os
import adafruit_dht
import board
import paho.mqtt.client as mqtt
import json

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT,60)
client.loop_start()
print("Connected to MQTT broker")

dht_sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temp_c = dht_sensor.temperature
        temp_f = temp_c * (9/5) + 32
        humidity = dht_sensor.humidity

        payload = {"temperature": round(temp_f, 1), "humidity": round(humidity, 1)}
        client.publish("sensor/dht22", json.dumps(payload))
        
        print(f"Published: {payload}")
        
    except RuntimeError as err:
        print(err.args[0])
    time.sleep(30)
