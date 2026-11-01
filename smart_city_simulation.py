"""
IoT Simulation Example - Smart City Network
Demonstrates smart city infrastructure with diverse protocols
"""

from iot_framework import IoTDevice, IoTNetwork
from iot_protocols import ProtocolLibrary

# Initialize smart city network
smart_city = IoTNetwork("Smart_City_Network")

# Initialize protocol library
protocol_lib = ProtocolLibrary()

# Create smart city IoT devices
traffic_sensor = IoTDevice(
    device_id="traffic_sensor_01",
    device_type="Traffic_Camera",
    memory_kb=16,
    cpu_mhz=100,
    power_v=12.0
)

air_quality_sensor = IoTDevice(
    device_id="air_quality_01",
    device_type="Air_Quality_Sensor",
    memory_kb=8,
    cpu_mhz=32,
    power_v=5.0
)

street_light = IoTDevice(
    device_id="street_light_01",
    device_type="Smart_Street_Light",
    memory_kb=4,
    cpu_mhz=16,
    power_v=24.0
)

parking_sensor = IoTDevice(
    device_id="parking_sensor_01",
    device_type="Parking_Sensor",
    memory_kb=2,
    cpu_mhz=8,
    power_v=3.3
)

city_gateway = IoTDevice(
    device_id="city_gateway",
    device_type="City_Gateway",
    memory_kb=1024,
    cpu_mhz=1200,
    power_v=24.0
)

cloud_server = IoTDevice(
    device_id="city_cloud",
    device_type="City_Cloud",
    memory_kb=16384,
    cpu_mhz=3200,
    power_v=24.0
)

# Add devices to network
smart_city.add_device(traffic_sensor)
smart_city.add_device(air_quality_sensor)
smart_city.add_device(street_light)
smart_city.add_device(parking_sensor)
smart_city.add_device(city_gateway)
smart_city.add_device(cloud_server)

# Configure smart city protocols
loRa_protocol = protocol_lib.get_protocol('LoRa', band='868MHz', spreading_factor=9)
zigbee_protocol = protocol_lib.get_protocol('Zigbee', channel=15, data_rate='250kbps')
wifi_protocol = protocol_lib.get_protocol('WiFi', standard='802.11n', power='20dBm')
mqtt_protocol = protocol_lib.get_protocol('MQTT', qos=1)

smart_city.add_protocol(loRa_protocol)
smart_city.add_protocol(zigbee_protocol)
smart_city.add_protocol(wifi_protocol)
smart_city.add_protocol(mqtt_protocol)

# Connect devices with appropriate protocols
smart_city.connect_devices("traffic_sensor_01", "city_gateway", "WiFi")
smart_city.connect_devices("air_quality_01", "city_gateway", "LoRa")
smart_city.connect_devices("street_light_01", "city_gateway", "Zigbee")
smart_city.connect_devices("parking_sensor_01", "city_gateway", "LoRa")
smart_city.connect_devices("city_gateway", "city_cloud", "WiFi")
smart_city.connect_devices("city_gateway", "city_cloud", "MQTT")

# Activate devices
traffic_sensor.turn_on()
air_quality_sensor.turn_on()
street_light.turn_on()
parking_sensor.turn_on()
city_gateway.turn_on()
cloud_server.turn_on()

# Simulate smart city data transmission
print("Starting Smart City IoT Simulation...")
print("=" * 60)

# Traffic monitoring via WiFi
print("\n[Traffic Monitoring]")
smart_city.simulate_data_transmission("traffic_sensor_01", "city_gateway", "WiFi", 512)

# Environmental monitoring via LoRa
print("\n[Environmental Monitoring]")
smart_city.simulate_data_transmission("air_quality_01", "city_gateway", "LoRa", 32)
smart_city.simulate_data_transmission("parking_sensor_01", "city_gateway", "LoRa", 16)

# Smart lighting via Zigbee
print("\n[Smart Lighting Control]")
smart_city.simulate_data_transmission("street_light_01", "city_gateway", "Zigbee", 8)

# Cloud aggregation via multiple protocols
print("\n[Cloud Data Aggregation]")
smart_city.simulate_data_transmission("city_gateway", "city_cloud", "WiFi", 1024)
smart_city.simulate_data_transmission("city_gateway", "city_cloud", "MQTT", 2048)

# Generate trace file
smart_city.generate_trace_file("smart_city_trace.tr")
print("Trace file generated: smart_city_trace.tr")

# Get network statistics
stats = smart_city.get_network_statistics()
print("\nSmart City Network Statistics:")
print("=" * 60)
print(f"Total Energy Consumption: {stats['total_energy_consumption']:.4f} mJ")
print(f"Average Latency: {stats['average_latency_ms']:.2f} ms")
print(f"Total Packets Transmitted: {stats['total_packets_transmitted']}")
print(f"Active Devices: {stats['active_devices']}/{stats['total_devices']}")

print("\nSmart City simulation completed successfully!")
print("Features demonstrated:")
print("- LoRa for long-range environmental sensors")
print("- Zigbee for smart lighting mesh network")
print("- WiFi for high-bandwidth traffic cameras")
print("- MQTT for cloud messaging")
print("- Multi-protocol smart city infrastructure")
