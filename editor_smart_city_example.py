# Smart City Network - Editor Compatible Version
# Use this script in the web editor

# Create smart city devices
traffic_camera = Camera("traffic_cam_01")
air_sensor = Sensor("air_quality_01")
street_light = LED("smart_light_01")
parking_sensor = Sensor("parking_01")
gateway = Gateway("city_gateway")
cloud = Cloud("city_cloud")

# Connect devices with appropriate protocols
traffic_camera.connect(gateway)
air_sensor.connect(gateway)
street_light.connect(gateway)
parking_sensor.connect(gateway)
gateway.connect(cloud)

# Power on smart city network
traffic_camera.turn_on()
air_sensor.turn_on()
street_light.turn_on()
parking_sensor.turn_on()
gateway.turn_on()
cloud.turn_on()

# Simulate smart city operations
print("Smart City Network Active")
print("WiFi: Traffic camera monitoring")
print("LoRa: Environmental sensors")
print("Zigbee: Smart lighting control")
print("MQTT: Cloud data aggregation")

# Smart city data flow
traffic_camera.get_data()
air_sensor.get_data()
parking_sensor.get_data()
street_light.turn_on()
street_light.turn_off()
cloud.send_data("City status: All systems normal")
