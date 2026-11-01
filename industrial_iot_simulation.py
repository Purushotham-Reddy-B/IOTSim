"""
IoT Simulation Example - Industrial IoT Network
Demonstrates industrial automation with multiple protocols
"""

from iot_framework import IoTDevice, IoTNetwork
from iot_protocols import ProtocolLibrary

# Initialize industrial IoT network
industrial_network = IoTNetwork("Industrial_Automation_Network")

# Initialize protocol library
protocol_lib = ProtocolLibrary()

# Create industrial IoT devices
temperature_sensor = IoTDevice(
    device_id="temp_sensor_01",
    device_type="Industrial_Temperature",
    memory_kb=4,
    cpu_mhz=16,
    power_v=24.0
)

pressure_sensor = IoTDevice(
    device_id="pressure_sensor_01",
    device_type="Industrial_Pressure",
    memory_kb=4,
    cpu_mhz=16,
    power_v=24.0
)

vibration_sensor = IoTDevice(
    device_id="vibration_sensor_01",
    device_type="Vibration_Sensor",
    memory_kb=8,
    cpu_mhz=32,
    power_v=24.0
)

plc_controller = IoTDevice(
    device_id="plc_controller",
    device_type="PLC_Controller",
    memory_kb=64,
    cpu_mhz=200,
    power_v=24.0
)

industrial_gateway = IoTDevice(
    device_id="industrial_gateway",
    device_type="Industrial_Gateway",
    memory_kb=512,
    cpu_mhz=800,
    power_v=24.0
)

edge_server = IoTDevice(
    device_id="edge_server",
    device_type="Edge_Server",
    memory_kb=4096,
    cpu_mhz=2400,
    power_v=24.0
)

# Add devices to network
industrial_network.add_device(temperature_sensor)
industrial_network.add_device(pressure_sensor)
industrial_network.add_device(vibration_sensor)
industrial_network.add_device(plc_controller)
industrial_network.add_device(industrial_gateway)
industrial_network.add_device(edge_server)

# Configure industrial protocols
can_protocol = protocol_lib.get_protocol('CAN', baud_rate='500kbps')
modbus_protocol = protocol_lib.get_protocol('UART', baud_rate=115200)  # Modbus over UART
ethernet_protocol = protocol_lib.get_protocol('WiFi', standard='802.11n', power='20dBm')
mqtt_protocol = protocol_lib.get_protocol('MQTT', qos=2)

industrial_network.add_protocol(can_protocol)
industrial_network.add_protocol(modbus_protocol)
industrial_network.add_protocol(ethernet_protocol)
industrial_network.add_protocol(mqtt_protocol)

# Connect devices with industrial protocols
industrial_network.connect_devices("temp_sensor_01", "plc_controller", "CAN")
industrial_network.connect_devices("pressure_sensor_01", "plc_controller", "CAN")
industrial_network.connect_devices("vibration_sensor_01", "plc_controller", "CAN")
industrial_network.connect_devices("plc_controller", "industrial_gateway", "UART")
industrial_network.connect_devices("industrial_gateway", "edge_server", "WiFi")
industrial_network.connect_devices("industrial_gateway", "edge_server", "MQTT")

# Activate devices
temperature_sensor.turn_on()
pressure_sensor.turn_on()
vibration_sensor.turn_on()
plc_controller.turn_on()
industrial_gateway.turn_on()
edge_server.turn_on()

# Simulate industrial data transmission
print("Starting Industrial IoT Simulation...")
print("=" * 60)

# Sensor data collection via CAN bus
print("\n[Sensor Data Collection]")
industrial_network.simulate_data_transmission("temp_sensor_01", "plc_controller", "CAN", 16)
industrial_network.simulate_data_transmission("pressure_sensor_01", "plc_controller", "CAN", 16)
industrial_network.simulate_data_transmission("vibration_sensor_01", "plc_controller", "CAN", 32)

# PLC processing and gateway communication
print("\n[PLC Processing and Gateway Communication]")
industrial_network.simulate_data_transmission("plc_controller", "industrial_gateway", "UART", 64)

# Edge server communication via multiple protocols
print("\n[Edge Server Communication]")
industrial_network.simulate_data_transmission("industrial_gateway", "edge_server", "WiFi", 256)
industrial_network.simulate_data_transmission("industrial_gateway", "edge_server", "MQTT", 512)

# Generate trace file
industrial_network.generate_trace_file("industrial_iot_trace.tr")
print("Trace file generated: industrial_iot_trace.tr")

# Get network statistics
stats = industrial_network.get_network_statistics()
print("\nIndustrial Network Statistics:")
print("=" * 60)
print(f"Total Energy Consumption: {stats['total_energy_consumption']:.4f} mJ")
print(f"Average Latency: {stats['average_latency_ms']:.2f} ms")
print(f"Total Packets Transmitted: {stats['total_packets_transmitted']}")
print(f"Active Devices: {stats['active_devices']}/{stats['total_devices']}")

print("\nIndustrial IoT simulation completed successfully!")
print("Features demonstrated:")
print("- CAN bus protocol for sensor communication")
print("- UART/Modbus for PLC communication")
print("- WiFi and MQTT for gateway-to-edge communication")
print("- Industrial device resource modeling")
