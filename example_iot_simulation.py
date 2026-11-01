"""
IoT Simulation Example - Smart Home Network
Demonstrates Python scripting with IoT-native syntax
"""

from iot_framework import IoTDevice, IoTNetwork
from iot_protocols import ProtocolLibrary

# Initialize IoT network
smart_home = IoTNetwork("Smart_Home_Network")

# Initialize protocol library
protocol_lib = ProtocolLibrary()

# Create IoT devices with resource constraints
temperature_sensor = IoTDevice(
    device_id="temp_sensor_01",
    device_type="DHT22",
    memory_kb=2,
    cpu_mhz=8,
    power_v=3.3
)

humidity_sensor = IoTDevice(
    device_id="hum_sensor_01", 
    device_type="DHT22",
    memory_kb=2,
    cpu_mhz=8,
    power_v=3.3
)

arduino_controller = IoTDevice(
    device_id="arduino_gateway",
    device_type="Arduino",
    memory_kb=2,
    cpu_mhz=16,
    power_v=5.0
)

raspberry_pi = IoTDevice(
    device_id="rpi_gateway",
    device_type="RaspberryPi",
    memory_kb=1024,
    cpu_mhz=1200,
    power_v=5.0
)

cloud_server = IoTDevice(
    device_id="aws_cloud",
    device_type="Cloud",
    memory_kb=8192,
    cpu_mhz=2400,
    power_v=12.0
)

# Add devices to network
smart_home.add_device(temperature_sensor)
smart_home.add_device(humidity_sensor)
smart_home.add_device(arduino_controller)
smart_home.add_device(raspberry_pi)
smart_home.add_device(cloud_server)

# Configure protocols
i2c_protocol = protocol_lib.get_protocol('I2C', clock_speed='400kHz')
wifi_protocol = protocol_lib.get_protocol('WiFi', standard='802.11n', power='20dBm')
mqtt_protocol = protocol_lib.get_protocol('MQTT', qos=1)

smart_home.add_protocol(i2c_protocol)
smart_home.add_protocol(wifi_protocol)
smart_home.add_protocol(mqtt_protocol)

# Connect devices with protocols
smart_home.connect_devices("temp_sensor_01", "arduino_gateway", "I2C")
smart_home.connect_devices("hum_sensor_01", "arduino_gateway", "I2C")
smart_home.connect_devices("arduino_gateway", "rpi_gateway", "UART")
smart_home.connect_devices("rpi_gateway", "aws_cloud", "WiFi")

# Activate devices
temperature_sensor.turn_on()
humidity_sensor.turn_on()
arduino_controller.turn_on()
raspberry_pi.turn_on()
cloud_server.turn_on()

# Simulate data transmission
print("Starting IoT Simulation...")
print("=" * 50)

# Sensor data transmission
smart_home.simulate_data_transmission("temp_sensor_01", "arduino_gateway", "I2C", 32)
smart_home.simulate_data_transmission("hum_sensor_01", "arduino_gateway", "I2C", 32)

# Gateway processing
smart_home.simulate_data_transmission("arduino_gateway", "rpi_gateway", "UART", 64)

# Cloud upload
smart_home.simulate_data_transmission("rpi_gateway", "aws_cloud", "WiFi", 128)
smart_home.simulate_data_transmission("rpi_gateway", "aws_cloud", "MQTT", 256)

# Generate trace file
smart_home.generate_trace_file("smart_home_trace.tr")
print("Trace file generated: smart_home_trace.tr")

# Get network statistics
stats = smart_home.get_network_statistics()
print("\nNetwork Statistics:")
print("=" * 50)
print(f"Total Energy Consumption: {stats['total_energy_consumption']:.4f} mJ")
print(f"Average Latency: {stats['average_latency_ms']:.2f} ms")
print(f"Total Packets Transmitted: {stats['total_packets_transmitted']}")
print(f"Active Devices: {stats['active_devices']}/{stats['total_devices']}")

print("\nSimulation completed successfully!")
