# raspberry-pi-iot-monitoring-dashboard

### Overview
IoT monitoring system built using a Raspberry Pi 5 and DHT22 sensor. The system collects environmental data, processes it through an MQTT-based pipeline with Node-RED, stores it in an InfluxDB time-series database, and visualizes it in a live Grafana dashboard.

### Pipeline diagram
DHT22 -> Raspberry Pi -> MQTT -> Node-RED -> InfluxDB -> Grafana

### Hardware
- Raspberry Pi 5
- DHT22 sensor

### Software
- Python
- Mosquitto
- Node-RED
- InfluxDB v1
- Grafana
