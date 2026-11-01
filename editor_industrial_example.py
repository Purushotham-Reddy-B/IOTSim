# Industrial IoT Network - Editor Compatible Version
# Use this script in the web editor

# Create industrial devices
temp_sensor = Sensor("industrial_temp")
pressure_sensor = Sensor("industrial_pressure")
vibration_sensor = Sensor("vibration_monitor")
plc = Arduino("plc_controller")
gateway = Gateway("industrial_gateway")
server = Server("edge_server")

# Connect devices with industrial protocols
temp_sensor.connect(plc)
pressure_sensor.connect(plc)
vibration_sensor.connect(plc)
plc.connect(gateway)
gateway.connect(server)

# Power on industrial network
temp_sensor.turn_on()
pressure_sensor.turn_on()
vibration_sensor.turn_on()
plc.turn_on()
gateway.turn_on()
server.turn_on()

# Simulate industrial data flow
print("Industrial IoT Network Active")
print("CAN Bus: Sensor to PLC communication")
print("Modbus: PLC to Gateway communication")
print("WiFi/MQTT: Gateway to Edge Server")

# Data transmission simulation
temp_sensor.get_data()
pressure_sensor.get_data()
vibration_sensor.get_data()
server.send_data("Industrial status: Normal")
