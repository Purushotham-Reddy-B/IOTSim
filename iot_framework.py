"""
IoT Framework - Python Scripting Engine for IoT Simulation
Original IoT-Native Simulation Methodology
"""

class IoTDevice:
    """Resource-constrained IoT device with realistic constraints"""
    def __init__(self, device_id, device_type, memory_kb, cpu_mhz, power_v):
        self.device_id = device_id
        self.device_type = device_type
        self.memory_kb = memory_kb
        self.cpu_mhz = cpu_mhz
        self.power_v = power_v
        self.energy_consumption = 0.0
        self.active = False
        self.connections = []
        
    def configure_data_generation(self, interval, data_range, noise_level):
        """Configure sensor data generation parameters"""
        self.data_interval = interval
        self.data_range = data_range
        self.noise_level = noise_level
        
    def turn_on(self):
        """Activate device with energy consumption"""
        self.active = True
        self.energy_consumption += 0.1  # Base power consumption
        
    def turn_off(self):
        """Deactivate device"""
        self.active = False
        
    def get_energy_consumption(self):
        """Return current energy consumption in mJ"""
        return self.energy_consumption


class IoTProtocol:
    """IoT-specific protocol with timing and energy characteristics"""
    def __init__(self, protocol_type, **params):
        self.protocol_type = protocol_type
        self.params = params
        self.clock_speed = params.get('clock_speed', 'unknown')
        self.bandwidth = params.get('bandwidth', 'unknown')
        self.power_consumption = params.get('power_consumption', 0.0)
        
    def calculate_latency(self, data_size):
        """Calculate protocol-specific latency based on data size"""
        # Original latency calculation methodology
        base_latency = 0.001  # 1ms base latency
        protocol_factor = {
            'I2C': 0.01,
            'SPI': 0.005,
            'UART': 0.02,
            'WiFi': 0.05,
            'BLE': 0.03,
            'LoRa': 0.1,
            'MQTT': 0.08
        }.get(self.protocol_type, 0.05)
        
        return base_latency + (data_size * protocol_factor)
    
    def calculate_energy(self, data_size, distance):
        """Calculate energy consumption for data transmission"""
        # Original energy calculation methodology
        base_energy = self.power_consumption
        distance_factor = distance * 0.01
        size_factor = data_size * 0.001
        
        return base_energy + distance_factor + size_factor


class IoTNetwork:
    """IoT network with resource-aware simulation"""
    def __init__(self, network_name):
        self.network_name = network_name
        self.devices = {}
        self.protocols = {}
        self.connections = []
        self.trace_log = []
        self.simulation_time = 0.0
        
    def add_device(self, device):
        """Add device to network with resource tracking"""
        self.devices[device.device_id] = device
        return device
        
    def add_protocol(self, protocol):
        """Add protocol to network"""
        self.protocols[protocol.protocol_type] = protocol
        return protocol
        
    def connect_devices(self, device1_id, device2_id, protocol_type):
        """Connect devices using specified protocol"""
        if device1_id in self.devices and device2_id in self.devices:
            connection = {
                'source': device1_id,
                'target': device2_id,
                'protocol': protocol_type,
                'distance': 10.0  # Default distance in meters
            }
            self.connections.append(connection)
            return connection
        return None
        
    def simulate_data_transmission(self, source_id, target_id, protocol_type, data_size):
        """Simulate data transmission with energy and latency tracking"""
        if protocol_type not in self.protocols:
            return None
            
        protocol = self.protocols[protocol_type]
        connection = next((c for c in self.connections 
                          if c['source'] == source_id and c['target'] == target_id), None)
        
        if not connection:
            return None
            
        # Calculate transmission metrics
        latency = protocol.calculate_latency(data_size)
        energy = protocol.calculate_energy(data_size, connection['distance'])
        
        # Update device energy consumption
        if source_id in self.devices:
            self.devices[source_id].energy_consumption += energy
            
        # Log transmission
        trace_entry = {
            'timestamp': self.simulation_time,
            'source': source_id,
            'target': target_id,
            'event': 'transmit',
            'protocol': protocol_type,
            'data_size': data_size,
            'energy_consumption': energy,
            'latency_ms': latency * 1000,
            'packet_id': f"pkt_{len(self.trace_log):06d}"
        }
        self.trace_log.append(trace_entry)
        
        # Update simulation time
        self.simulation_time += latency
        
        return trace_entry
        
    def generate_trace_file(self, filename):
        """Generate single-line trace file format"""
        with open(filename, 'w') as f:
            # Header
            f.write("# IoT Simulation Trace File\n")
            f.write("# Format: timestamp|device_id|event|protocol|data_size|energy_consumption|latency_ms|packet_id\n")
            f.write(f"# Network: {self.network_name}\n")
            f.write(f"# Total Events: {len(self.trace_log)}\n\n")
            
            # Trace entries
            for entry in self.trace_log:
                line = f"{entry['timestamp']:.3f}|{entry['source']}|{entry['event']}|{entry['protocol']}|{entry['data_size']}|{entry['energy_consumption']:.4f}|{entry['latency_ms']:.2f}|{entry['packet_id']}\n"
                f.write(line)
                
    def get_network_statistics(self):
        """Calculate network performance statistics"""
        total_energy = sum(d.energy_consumption for d in self.devices.values())
        avg_latency = sum(e['latency_ms'] for e in self.trace_log) / len(self.trace_log) if self.trace_log else 0
        total_packets = len(self.trace_log)
        
        return {
            'total_energy_consumption': total_energy,
            'average_latency_ms': avg_latency,
            'total_packets_transmitted': total_packets,
            'active_devices': sum(1 for d in self.devices.values() if d.active),
            'total_devices': len(self.devices)
        }
