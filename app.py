from flask import Flask, render_template, request, jsonify, send_from_directory
import ast
import sys
import json
import os
from io import StringIO
from datetime import datetime
import re

# OpenAI API integration (optional)
try:
    import openai
    OPENAI_AVAILABLE = True
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
except ImportError:
    OPENAI_AVAILABLE = False
    OPENAI_API_KEY = ''

app = Flask(__name__)

# Create networks directory if it doesn't exist
NETWORKS_DIR = "saved_networks"
if not os.path.exists(NETWORKS_DIR):
    os.makedirs(NETWORKS_DIR)

# Create trace files directory if it doesn't exist
TRACE_DIR = "trace_files"
if not os.path.exists(TRACE_DIR):
    os.makedirs(TRACE_DIR)

# ---------- IOT CLASSES FOR PYTHON SCRIPTS ----------
class IoTNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.states = {}
    
    def add_node(self, node_obj):
        self.nodes[node_obj.id] = node_obj.type
        if hasattr(node_obj, 'state'):
            self.states[node_obj.id] = node_obj.state
    
    def connect_nodes(self, source_obj, target_obj):
        if source_obj.id not in self.nodes:
            raise ValueError(f"Source node '{source_obj.id}' does not exist")
        if target_obj.id not in self.nodes:
            raise ValueError(f"Target node '{target_obj.id}' does not exist")
        self.edges.append((source_obj.id, target_obj.id))

# Base IoT Device Class
class IoTDevice:
    def __init__(self, device_id, device_type, network_ref=None):
        self.id = device_id
        self.type = device_type
        self.state = "off"
        # Use provided network or global network
        if network_ref:
            self.network = network_ref
        else:
            # Don't use global network here - it might not exist yet
            self.network = None
    
    def turn_on(self):
        self.state = "on"
        # Update network state if network exists
        if self.network:
            self.network.states[self.id] = "on"
    
    def turn_off(self):
        self.state = "off"
        # Update network state if network exists
        if self.network:
            self.network.states[self.id] = "off"
    
    def connect(self, other_device):
        if self.network:
            self.network.connect_nodes(self, other_device)
        else:
            raise ValueError("No network available for connection")
    
    def get_data(self):
        """Simulate data retrieval from device"""
        if self.type == "Sensor":
            return {"sensor_id": self.id, "value": 25.5, "unit": "C"}
        elif self.type == "Camera":
            return {"camera_id": self.id, "status": "recording"}
        else:
            return {"device_id": self.id, "status": self.state}
    
    def send_data(self, data):
        """Simulate sending data from device"""
        return {"device_id": self.id, "data": data, "sent": True}

# Specific IoT Device Classes
class Sensor(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Sensor", network_ref)

class Gateway(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Gateway", network_ref)

class Actuator(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Actuator", network_ref)

class Camera(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Camera", network_ref)

class Switch(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Switch", network_ref)

class Router(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Router", network_ref)

class Server(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Server", network_ref)

class Cloud(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Cloud", network_ref)

class Mobile(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Mobile", network_ref)

class LED(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "LED", network_ref)

class Motor(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Motor", network_ref)

class Display(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Display", network_ref)

# ---------- NEW IOT HARDWARE DEVICES ----------
# Microcontrollers
class Arduino(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Arduino", network_ref)

class ESP32(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "ESP32", network_ref)

class STM32(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "STM32", network_ref)

class PIC(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "PIC", network_ref)

# Single Board Computers
class RaspberryPi(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "RaspberryPi", network_ref)

class BeagleBone(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "BeagleBone", network_ref)

class JetsonNano(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "JetsonNano", network_ref)

# Communication Modules
class WiFi(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "WiFi", network_ref)

class Bluetooth(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Bluetooth", network_ref)

class LoRa(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "LoRa", network_ref)

class Zigbee(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Zigbee", network_ref)

# Power Management
class Battery(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "Battery", network_ref)

class PowerSupply(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "PowerSupply", network_ref)

class SolarPanel(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "SolarPanel", network_ref)

# Storage Devices
class SDCard(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "SDCard", network_ref)

class EEPROM(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "EEPROM", network_ref)

class FlashMemory(IoTDevice):
    def __init__(self, device_id, network_ref=None):
        super().__init__(device_id, "FlashMemory", network_ref)

# Global network instance - created AFTER all classes
network = IoTNetwork()

# ---------- VALIDATION ----------
def validate_python_script(script: str):
    try:
        # Check if it's valid Python syntax
        ast.parse(script)
        
        # Execute in restricted environment
        test_network = IoTNetwork()
        
        # Create device classes that automatically register with test_network
        def make_device_class(device_type):
            class TestDevice(IoTDevice):
                def __init__(self, device_id):
                    super().__init__(device_id, device_type, test_network)
                    # Manually register with network
                    test_network.add_node(self)
            return TestDevice
        
        # Create restricted globals with test-specific device classes
        restricted_globals = {
            '__builtins__': {
                '__import__': __import__,
                'print': print,
                'len': len,
                'str': str,
                'int': int,
                'float': float,
                'bool': bool,
                'list': list,
                'dict': dict,
                'range': range,
                'enumerate': enumerate,
                'zip': zip,
            },
            'IoTNetwork': IoTNetwork,
            'IoTDevice': IoTDevice,
            # Original devices
            'Sensor': make_device_class('Sensor'),
            'Gateway': make_device_class('Gateway'),
            'Actuator': make_device_class('Actuator'),
            'Camera': make_device_class('Camera'),
            'Switch': make_device_class('Switch'),
            'Router': make_device_class('Router'),
            'Server': make_device_class('Server'),
            'Cloud': make_device_class('Cloud'),
            'Mobile': make_device_class('Mobile'),
            'LED': make_device_class('LED'),
            'Motor': make_device_class('Motor'),
            'Display': make_device_class('Display'),
            # Microcontrollers
            'Arduino': make_device_class('Arduino'),
            'ESP32': make_device_class('ESP32'),
            'STM32': make_device_class('STM32'),
            'PIC': make_device_class('PIC'),
            # Single Board Computers
            'RaspberryPi': make_device_class('RaspberryPi'),
            'BeagleBone': make_device_class('BeagleBone'),
            'JetsonNano': make_device_class('JetsonNano'),
            # Communication Modules
            'WiFi': make_device_class('WiFi'),
            'Bluetooth': make_device_class('Bluetooth'),
            'LoRa': make_device_class('LoRa'),
            'Zigbee': make_device_class('Zigbee'),
            # Power Management
            'Battery': make_device_class('Battery'),
            'PowerSupply': make_device_class('PowerSupply'),
            'SolarPanel': make_device_class('SolarPanel'),
            # Storage Devices
            'SDCard': make_device_class('SDCard'),
            'EEPROM': make_device_class('EEPROM'),
            'FlashMemory': make_device_class('FlashMemory'),
            'network': test_network
        }
        
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            exec(script, restricted_globals)
        finally:
            sys.stdout = old_stdout
        
        # Check if test_network has nodes
        if not test_network.nodes:
            return False, "No devices created in script"
        
        return True, "Valid Python script"
        
    except SyntaxError as e:
        return False, f"Syntax error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

# ---------- SIMULATOR ----------
@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json or {}
    script = data.get("script", "")

    ok, msg = validate_python_script(script)
    if not ok:
        return jsonify({"error": msg}), 400

    # Execute script to get network data
    network = IoTNetwork()
    
    # Create device classes that automatically register with network
    def make_device_class(device_type):
        class NetworkDevice(IoTDevice):
            def __init__(self, device_id):
                super().__init__(device_id, device_type, network)
                # Manually register with network
                network.add_node(self)
        return NetworkDevice
    
    restricted_globals = {
        '__builtins__': {
            '__import__': __import__,
            'print': print,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'bool': bool,
            'list': list,
            'dict': dict,
            'range': range,
            'enumerate': enumerate,
            'zip': zip,
        },
        'IoTNetwork': IoTNetwork,
        'IoTDevice': IoTDevice,
        # Original devices
        'Sensor': make_device_class('Sensor'),
        'Gateway': make_device_class('Gateway'),
        'Actuator': make_device_class('Actuator'),
        'Camera': make_device_class('Camera'),
        'Switch': make_device_class('Switch'),
        'Router': make_device_class('Router'),
        'Server': make_device_class('Server'),
        'Cloud': make_device_class('Cloud'),
        'Mobile': make_device_class('Mobile'),
        'LED': make_device_class('LED'),
        'Motor': make_device_class('Motor'),
        'Display': make_device_class('Display'),
        # Microcontrollers
        'Arduino': make_device_class('Arduino'),
        'ESP32': make_device_class('ESP32'),
        'STM32': make_device_class('STM32'),
        'PIC': make_device_class('PIC'),
        # Single Board Computers
        'RaspberryPi': make_device_class('RaspberryPi'),
        'BeagleBone': make_device_class('BeagleBone'),
        'JetsonNano': make_device_class('JetsonNano'),
        # Communication Modules
        'WiFi': make_device_class('WiFi'),
        'Bluetooth': make_device_class('Bluetooth'),
        'LoRa': make_device_class('LoRa'),
        'Zigbee': make_device_class('Zigbee'),
        # Power Management
        'Battery': make_device_class('Battery'),
        'PowerSupply': make_device_class('PowerSupply'),
        'SolarPanel': make_device_class('SolarPanel'),
        # Storage Devices
        'SDCard': make_device_class('SDCard'),
        'EEPROM': make_device_class('EEPROM'),
        'FlashMemory': make_device_class('FlashMemory'),
        'network': network
    }
    
    try:
        exec(script, restricted_globals)
    except Exception as e:
        return jsonify({"error": f"Execution error: {e}"}), 400

    # Build cytoscape elements
    elements = []

    # nodes
    for nid, ntype in network.nodes.items():
        elements.append({
            "data": {
                "id": nid,
                "label": f"{ntype} ({nid})",
                "type": ntype
            }
        })

    # edges (only if both ends exist)
    for s, t in network.edges:
        if s in network.nodes and t in network.nodes:
            elements.append({
                "data": {
                    "source": s,
                    "target": t
                }
            })

    return jsonify({
        "elements": elements,
        "states": network.states,
        "script": script  # Add script data to response
    })

# ---------- SAVE/LOAD NETWORK FUNCTIONALITY ----------
@app.route("/save_network", methods=["POST"])
def save_network():
    try:
        data = request.json or {}
        script = data.get("script", "")
        name = data.get("name", "unnetwork")
        
        if not script.strip():
            return jsonify({"error": "No script to save"}), 400
        
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.json"
        filepath = os.path.join(NETWORKS_DIR, filename)
        
        # Save network data
        network_data = {
            "name": name,
            "script": script,
            "timestamp": timestamp,
            "created_at": datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(network_data, f, indent=2)
        
        return jsonify({
            "message": "Network saved successfully",
            "filename": filename
        })
        
    except Exception as e:
        return jsonify({"error": f"Save failed: {e}"}), 500

@app.route("/load_network", methods=["POST"])
def load_network():
    try:
        data = request.json or {}
        filename = data.get("filename", "")
        
        if not filename:
            return jsonify({"error": "No filename provided"}), 400
        
        filepath = os.path.join(NETWORKS_DIR, filename)
        
        if not os.path.exists(filepath):
            return jsonify({"error": "Network file not found"}), 404
        
        with open(filepath, 'r') as f:
            network_data = json.load(f)
        
        return jsonify(network_data)
        
    except Exception as e:
        return jsonify({"error": f"Load failed: {e}"}), 500

@app.route("/list_networks", methods=["GET"])
def list_networks():
    try:
        networks = []
        
        for filename in os.listdir(NETWORKS_DIR):
            if filename.endswith('.json'):
                filepath = os.path.join(NETWORKS_DIR, filename)
                
                with open(filepath, 'r') as f:
                    network_data = json.load(f)
                
                networks.append({
                    "filename": filename,
                    "name": network_data.get("name", "Unnamed"),
                    "created_at": network_data.get("created_at", "Unknown"),
                    "timestamp": network_data.get("timestamp", "")
                })
        
        # Sort by timestamp (newest first)
        networks.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        return jsonify({"networks": networks})
        
    except Exception as e:
        return jsonify({"error": f"List failed: {e}"}), 500

@app.route("/delete_network", methods=["POST"])
def delete_network():
    try:
        data = request.json or {}
        filename = data.get("filename", "")
        
        if not filename:
            return jsonify({"error": "No filename provided"}), 400
        
        filepath = os.path.join(NETWORKS_DIR, filename)
        
        if not os.path.exists(filepath):
            return jsonify({"error": "Network file not found"}), 404
        
        os.remove(filepath)
        
        return jsonify({"message": "Network deleted successfully"})
        
    except Exception as e:
        return jsonify({"error": f"Delete failed: {e}"}), 500


# ---------- TRACE FILE FUNCTIONALITY ----------
@app.route("/create_trace_file", methods=["POST"])
def create_trace_file():
    """Create a new trace file for a script"""
    try:
        data = request.json or {}
        script = data.get("script", "")
        script_name = data.get("script_name", "unnamed_script")
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{script_name}_{timestamp}.tr"
        filepath = os.path.join(TRACE_DIR, filename)
        
        # Create trace file with header
        trace_content = f"""# IoT Simulator Trace File
# Script: {script_name}
# Created: {datetime.now().isoformat()}
# Format: time event source target packetType description
# Event Types: s=send, r=receive, d=drop, f=forward

# Script Content:
{script}

# Trace Events:
"""
        
        with open(filepath, 'w') as f:
            f.write(trace_content)
        
        return jsonify({
            "success": True,
            "trace_file": filename,
            "filepath": filepath,
            "message": f"Trace file created: {filename}"
        })
        
    except Exception as e:
        return jsonify({"error": f"Failed to create trace file: {e}"}), 500

@app.route("/append_trace", methods=["POST"])
def append_trace():
    """Append trace events to existing trace file"""
    try:
        data = request.json or {}
        trace_file = data.get("trace_file", "")
        events = data.get("events", [])
        
        if not trace_file or not events:
            return jsonify({"error": "Missing trace file or events"}), 400
        
        filepath = os.path.join(TRACE_DIR, trace_file)
        
        # Append events to trace file
        with open(filepath, 'a') as f:
            for event in events:
                timestamp = event.get('time', '0.000000')
                event_type = event.get('event', 's')
                source = event.get('source', 'unknown')
                target = event.get('target', 'unknown')
                packet_type = event.get('packetType', 'data')
                description = event.get('description', '')
                
                trace_line = f"{timestamp} {event_type} {source} {target} {packet_type} \"{description}\"\n"
                f.write(trace_line)
        
        return jsonify({
            "success": True,
            "message": f"Appended {len(events)} events to {trace_file}"
        })
        
    except Exception as e:
        return jsonify({"error": f"Failed to append trace: {e}"}), 500

@app.route("/list_trace_files", methods=["GET"])
def list_trace_files():
    """List all trace files"""
    try:
        trace_files = []
        if os.path.exists(TRACE_DIR):
            for filename in os.listdir(TRACE_DIR):
                if filename.endswith('.tr'):
                    filepath = os.path.join(TRACE_DIR, filename)
                    stat = os.stat(filepath)
                    trace_files.append({
                        "filename": filename,
                        "size": stat.st_size,
                        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
        
        # Sort by creation time (newest first)
        trace_files.sort(key=lambda x: x['created'], reverse=True)
        
        return jsonify({"trace_files": trace_files})
        
    except Exception as e:
        return jsonify({"error": f"Failed to list trace files: {e}"}), 500

@app.route("/get_trace_file/<filename>")
def get_trace_file(filename):
    """Download or view a trace file"""
    try:
        return send_from_directory(TRACE_DIR, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"Failed to get trace file: {e}"}), 500

@app.route("/delete_trace_file", methods=["POST"])
def delete_trace_file():
    """Delete a trace file"""
    try:
        data = request.json or {}
        filename = data.get("filename", "")
        
        if not filename:
            return jsonify({"error": "Missing filename"}), 400
        
        filepath = os.path.join(TRACE_DIR, filename)
        
        if not os.path.exists(filepath):
            return jsonify({"error": "Trace file not found"}), 404
        
        os.remove(filepath)
        return jsonify({"message": f"Trace file {filename} deleted successfully"})
        
    except Exception as e:
        return jsonify({"error": f"Failed to delete trace file: {e}"}), 500

# ---------- AI CHATBOT SYSTEM ----------

# System prompt for OpenAI context
IOT_SIMULATOR_SYSTEM_PROMPT = """You are an expert AI assistant for the IoT Network Simulator. Your role is to help users with:

1. **Script Generation**: Create Python scripts for the IoT simulator using available device classes
2. **Technical Support**: Answer questions about simulator features, protocols, and usage
3. **Troubleshooting**: Help debug scripts and resolve errors

**Available Device Classes:**
- Microcontrollers: Arduino, ESP32, STM32, PIC
- I/O Devices: Sensor, Camera, LED, Motor, Display
- Network Devices: Gateway, Router, Server, Cloud

**Device Methods:**
- turn_on() / turn_off() - Power control
- connect(device) - Create connections
- get_data() - Retrieve sensor data
- send_data(data) - Send data to network

**Key Features:**
- Multi-layer visualization (Device, Protocol, Energy, DataFlow)
- Protocol support: I2C, SPI, UART, WiFi, BLE, LoRa, Zigbee, MQTT, CoAP, CAN
- Import support: json, datetime, math, and other standard Python modules
- Export: JSON export with performance metrics
- Trace files: Single-line format with energy and latency data

**Script Guidelines:**
- Use simple, clear variable names
- Include comments explaining device setup
- Always turn on devices before operations
- Connect devices before using them
- Use get_data() for sensors, send_data() for gateways

**Response Style:**
- Be concise and practical
- Provide working code examples
- Explain key concepts briefly
- Focus on simulator-specific features

When generating scripts, always provide complete, runnable code. When answering questions, be specific to the IoT simulator context."""

def call_openai_api(user_query):
    """Call OpenAI API for intelligent responses"""
    if not OPENAI_AVAILABLE or not OPENAI_API_KEY:
        return None, "OpenAI not available"
    
    try:
        openai.api_key = OPENAI_API_KEY
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": IOT_SIMULATOR_SYSTEM_PROMPT},
                {"role": "user", "content": user_query}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content, "openai"
    except Exception as e:
        return None, f"OpenAI API error: {e}"

# Script generation templates
SCRIPT_TEMPLATES = {
    "smart home": """# Smart Home IoT Network
# Temperature sensor and LED control

# Create devices
arduino = Arduino("uno")
temp_sensor = Sensor("temp_sensor")
led = LED("status_led")

# Connect devices
temp_sensor.connect(arduino)
arduino.connect(led)

# Power on system
arduino.turn_on()
temp_sensor.turn_on()
led.turn_on()

# Read sensor data
sensor_data = temp_sensor.get_data()
print(f"Temperature: {sensor_data}")

# Control LED based on temperature
if sensor_data["value"] > 25:
    led.turn_on()
else:
    led.turn_off()
""",

    "industrial": """# Industrial IoT Network
# PLC and sensor monitoring

# Create industrial devices
temp_sensor = Sensor("industrial_temp")
pressure_sensor = Sensor("industrial_pressure")
plc = Arduino("plc_controller")
gateway = Gateway("industrial_gateway")
server = Server("edge_server")

# Connect devices
temp_sensor.connect(plc)
pressure_sensor.connect(plc)
plc.connect(gateway)
gateway.connect(server)

# Power on industrial network
temp_sensor.turn_on()
pressure_sensor.turn_on()
plc.turn_on()
gateway.turn_on()
server.turn_on()

# Monitor sensors
temp_data = temp_sensor.get_data()
pressure_data = pressure_sensor.get_data()
print(f"Temperature: {temp_data}")
print(f"Pressure: {pressure_data}")

# Send data to server
gateway.send_data({"status": "normal", "sensors": 2})
""",

    "smart city": """# Smart City IoT Network
# Traffic and environmental monitoring

# Create smart city devices
traffic_camera = Camera("traffic_cam_01")
air_sensor = Sensor("air_quality_01")
street_light = LED("smart_light_01")
gateway = Gateway("city_gateway")
cloud = Cloud("city_cloud")

# Connect devices
traffic_camera.connect(gateway)
air_sensor.connect(gateway)
street_light.connect(gateway)
gateway.connect(cloud)

# Power on smart city
traffic_camera.turn_on()
air_sensor.turn_on()
street_light.turn_on()
gateway.turn_on()
cloud.turn_on()

# Monitor traffic
traffic_data = traffic_camera.get_data()
print(f"Traffic status: {traffic_data}")

# Monitor air quality
air_data = air_sensor.get_data()
print(f"Air quality: {air_data}")

# Smart lighting control
street_light.turn_on()
""",

    "simple": """# Simple IoT Network
# Basic sensor and actuator setup

# Create devices
sensor = Sensor("sensor_01")
actuator = LED("actuator_01")

# Connect devices
sensor.connect(actuator)

# Power on
sensor.turn_on()
actuator.turn_on()

# Read sensor and control actuator
data = sensor.get_data()
print(f"Sensor data: {data}")
actuator.turn_on()
"""
}

# Knowledge base for Q&A
KNOWLEDGE_BASE = {
    "what is": "The IoT Network Simulator is a Python-based simulation platform for designing, testing, and analyzing IoT networks. It features: 1) Web-based editor for writing IoT scripts, 2) Multi-layer network visualization (Device, Protocol, Energy, DataFlow), 3) Support for 10 IoT protocols (I2C, SPI, UART, WiFi, BLE, LoRa, Zigbee, MQTT, CoAP, CAN), 4) Resource-constrained device modeling, 5) Energy-aware simulation with performance metrics, 6) Single-line trace file generation for analysis, 7) AI-powered chatbot for script generation and Q&A.",
    "simulator": "The IoT Network Simulator is a Python-based simulation platform for designing, testing, and analyzing IoT networks. It features: 1) Web-based editor for writing IoT scripts, 2) Multi-layer network visualization (Device, Protocol, Energy, DataFlow), 3) Support for 10 IoT protocols (I2C, SPI, UART, WiFi, BLE, LoRa, Zigbee, MQTT, CoAP, CAN), 4) Resource-constrained device modeling, 5) Energy-aware simulation with performance metrics, 6) Single-line trace file generation for analysis, 7) AI-powered chatbot for script generation and Q&A.",
    "how to use": "To use the IoT simulator: 1) Write your script in the editor using device classes like Arduino, Sensor, LED. 2) Click 'Run Simulation' to execute. 3) View the network visualization. 4) Use multi-layer view by clicking 'Layer' button.",
    "multi-layer": "Multi-layer visualization shows different aspects: Device layer (device types), Protocol layer (communication protocols), Energy layer (power consumption), DataFlow layer (data intensity). Click 'Layer' button to cycle through them.",
    "export": "To export data: Click 'Export' button to download JSON file with complete simulation data including devices, protocols, and performance metrics.",
    "trace": "Trace files contain single-line format with timestamp, device, event, protocol, data size, energy consumption, and latency. Click 'Download Trace' to get the trace file.",
    "devices": "Available devices: Arduino, ESP32, STM32, PIC (microcontrollers), Sensor, Camera, LED, Motor, Display (I/O devices), Gateway, Router, Server, Cloud (network devices).",
    "protocols": "The simulator supports IoT protocols: I2C, SPI, UART, WiFi, BLE, LoRa, Zigbee, MQTT, CoAP, CAN. Each protocol has specific timing and energy characteristics.",
    "pause": "Pause/Resume button allows you to stop the simulation and continue from the exact same point. It preserves all device states and packet positions.",
    "import": "You can now use Python imports in the editor! Import modules like json, datetime, math, etc. for advanced scripting.",
    "script": "Scripts use simple Python syntax with device classes. Example: arduino = Arduino('uno'); sensor = Sensor('temp'); sensor.connect(arduino); arduino.turn_on()",
    "error": "Common errors: Check device names are unique, ensure devices are connected before use, verify turn_on() is called before operations.",
}

def generate_script(user_query):
    """Generate IoT simulator script based on user query"""
    query_lower = user_query.lower()
    
    # Check for script generation keywords
    script_keywords = {
        "smart home": "smart home",
        "home": "smart home",
        "temperature": "smart home",
        "industrial": "industrial",
        "plc": "industrial",
        "factory": "industrial",
        "smart city": "smart city",
        "traffic": "smart city",
        "city": "smart city",
        "simple": "simple",
        "basic": "simple",
        "beginner": "simple"
    }
    
    for keyword, template_key in script_keywords.items():
        if keyword in query_lower:
            return SCRIPT_TEMPLATES[template_key], "script"
    
    # Default to simple script if no match
    return SCRIPT_TEMPLATES["simple"], "script"

def answer_question(user_query):
    """Answer questions about the IoT simulator"""
    query_lower = user_query.lower()
    
    # Check knowledge base
    for keyword, answer in KNOWLEDGE_BASE.items():
        if keyword in query_lower:
            return answer, "qa"
    
    # Check for common questions
    if "what is" in query_lower or "simulator" in query_lower:
        return KNOWLEDGE_BASE["what is"], "qa"
    elif "how" in query_lower and "use" in query_lower:
        return KNOWLEDGE_BASE["how to use"], "qa"
    elif "layer" in query_lower or "visualization" in query_lower:
        return KNOWLEDGE_BASE["multi-layer"], "qa"
    elif "export" in query_lower or "download" in query_lower:
        return KNOWLEDGE_BASE["export"], "qa"
    elif "trace" in query_lower:
        return KNOWLEDGE_BASE["trace"], "qa"
    elif "device" in query_lower:
        return KNOWLEDGE_BASE["devices"], "qa"
    elif "protocol" in query_lower:
        return KNOWLEDGE_BASE["protocols"], "qa"
    elif "pause" in query_lower or "resume" in query_lower:
        return KNOWLEDGE_BASE["pause"], "qa"
    elif "import" in query_lower:
        return KNOWLEDGE_BASE["import"], "qa"
    elif "script" in query_lower:
        return KNOWLEDGE_BASE["script"], "qa"
    elif "error" in query_lower:
        return KNOWLEDGE_BASE["error"], "qa"
    
    # Default response
    return "I can help you with IoT simulator scripts and answer questions. Try asking about: smart home networks, industrial IoT, smart city, or how to use specific features like multi-layer visualization or export.", "qa"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """AI Chatbot endpoint for script generation and Q&A with OpenAI integration"""
    try:
        data = request.json or {}
        user_query = data.get("query", "").strip()
        
        if not user_query:
            return jsonify({"error": "No query provided"}), 400
        
        # Try OpenAI API first if available
        if OPENAI_AVAILABLE and OPENAI_API_KEY:
            openai_response, openai_status = call_openai_api(user_query)
            if openai_response:
                # Determine response type based on content
                script_keywords = ["arduino", "sensor", "led", "device", "connect", "turn_on", "get_data", "send_data"]
                is_script = any(keyword in openai_response.lower() for keyword in script_keywords)
                response_type = "script" if is_script else "qa"
                
                return jsonify({
                    "response": openai_response,
                    "type": response_type,
                    "source": "openai",
                    "query": user_query
                })
        
        # Fallback to rule-based system
        script_keywords = ["create", "generate", "make", "write", "script", "network", "iot", "setup", "build"]
        is_script_request = any(keyword in user_query.lower() for keyword in script_keywords)
        
        if is_script_request:
            response, response_type = generate_script(user_query)
        else:
            response, response_type = answer_question(user_query)
        
        return jsonify({
            "response": response,
            "type": response_type,
            "source": "rule-based",
            "query": user_query
        })
        
    except Exception as e:
        return jsonify({"error": f"Chatbot error: {e}"}), 500


# ---------- PAGES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/editor")
def editor():
    return render_template("editor.html")

@app.route("/simulation")
def simulation():
    return render_template("simulation.html")


if __name__ == "__main__":
    app.run(debug=True)
