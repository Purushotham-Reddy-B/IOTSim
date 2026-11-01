# 🌐 IoT Network Simulator - Complete Script Examples

## 🎯 **IoT Network Simulator Script Repository**

### **🔧 How to Write Scripts**

#### **Basic Script Structure**
```python
# 1. Create devices
arduino = Arduino("uno")
led = LED("status")

# 2. Connect devices
arduino.connect(led)

# 3. Power on devices
arduino.turn_on()
led.turn_on()

# 4. Add control logic
led.turn_on()
led.turn_off()
```

#### **Available Device Types**
- **Sensors**: Sensor, TemperatureSensor, HumiditySensor, LDRSensor, UltrasonicSensor, PressureSensor, MotionSensor
- **Controllers**: Arduino, ESP32, RaspberryPi, STM32, ESP8266
- **Actuators**: LED, Motor, Servo, Buzzer, Display, Relay
- **Communication**: WiFi, Bluetooth, LoRa, GSM, MQTT, Ethernet
- **Power**: Battery, PowerSupply, SolarPanel
- **Components**: Resistor, Capacitor, Button, Switch, Potentiometer

---

## 📋 **Complete Device Inventory**

### **SENSORS**
```python
# Environmental Sensors
temperature_sensor = Sensor("temperature_01")
humidity_sensor = Sensor("humidity_01")
pressure_sensor = Sensor("pressure_01")
light_sensor = Sensor("light_01")
gas_sensor = Sensor("gas_01")

# Distance Sensors
ultrasonic_sensor = Sensor("ultrasonic_01")
infrared_sensor = Sensor("infrared_01")

# Motion Sensors
motion_sensor = Sensor("motion_01")
vibration_sensor = Sensor("vibration_01")

# Specialized Sensors
current_sensor = Sensor("current_01")
voltage_sensor = Sensor("voltage_01")
ph_sensor = Sensor("ph_01")
soil_moisture_sensor = Sensor("soil_01")
```

### **CONTROLLERS**
```python
# Microcontrollers
arduino_uno = Arduino("uno_01")
arduino_mega = Arduino("mega_01")
esp32 = ESP32("esp32_01")
esp8266 = ESP8266("esp8266_01")
stm32 = STM32("stm32_01")

# Single Board Computers
raspberry_pi = RaspberryPi("pi_01")
raspberry_pi_4 = RaspberryPi("pi4_01")
```

### **ACTUATORS**
```python
# Lights
led_red = LED("red_01")
led_green = LED("green_01")
led_blue = LED("blue_01")
led_rgb = LED("rgb_01")

# Motors
motor_dc = Motor("dc_motor_01")
motor_stepper = Motor("stepper_01")
servo_motor = Servo("servo_01")

# Other Actuators
buzzer = Buzzer("buzzer_01")
relay = Relay("relay_01")
solenoid = Solenoid("solenoid_01")
```

### **ELECTRONIC COMPONENTS**
```python
# Passive Components
resistor_220 = Resistor("r220_01")
resistor_1k = Resistor("r1k_01")
resistor_10k = Resistor("r10k_01")
capacitor_100uf = Capacitor("c100_01")

# Input Components
push_button = Button("button_01")
toggle_switch = Switch("switch_01")
potentiometer = Potentiometer("pot_01")
```

---

---

## � **Network Performance Parameters**

### **Available Performance Controls**
```python
# Bandwidth Control
device.set_bandwidth(kbps)        # Set bandwidth in kbps
device.get_bandwidth()            # Get current bandwidth

# Latency Control
device.set_latency(ms)            # Set latency in milliseconds
device.get_latency()              # Get current latency

# Throughput Monitoring
device.get_throughput()           # Get current throughput
device.calculate_throughput()     # Calculate data throughput

# Time Delays
device.set_delay(ms)              # Set processing delay
device.get_delay()                # Get current delay

# Baudrate Configuration (Serial)
device.set_baudrate(rate)         # Set baudrate (9600, 115200, etc.)
device.get_baudrate()             # Get current baudrate

# Protocol Timing
device.set_protocol_timing(protocol, time)  # Set protocol-specific timing
```

### **Performance Monitoring Functions**
```python
# Network Analysis
network.analyze_performance()     # Analyze overall network performance
network.get_packet_loss()         # Get packet loss percentage
network.get_jitter()              # Get network jitter

# Device Performance
device.get_response_time()        # Get device response time
device.get_processing_time()      # Get processing time
device.get_queue_size()           # Get device queue size
```

### **Export and Logging Functions**
```python
# JSON Export
simulation.export_json()          # Export simulation logs to JSON
simulation.get_logs()             # Get all simulation logs
simulation.get_device_logs(device) # Get specific device logs
simulation.clear_logs()           # Clear simulation logs

# Log Management
log.add_event(event_type, data)   # Add event to log
log.get_timestamp()               # Get current timestamp
log.get_device_events(device)     # Get device-specific events
log.get_protocol_events(protocol) # Get protocol-specific events

# File Operations
export.save_json(filename)        # Save logs to JSON file
export.load_json(filename)        # Load logs from JSON file
export.get_file_size()            # Get exported file size
```

---

## 💡 **Network Performance Scripts**

### **1. Bandwidth Control Demonstration**
```python
# Bandwidth Control Example
# Create devices
sensor = Sensor("temp")
arduino = Arduino("controller")
wifi = WiFi("wifi_module")

# Connect devices
sensor.connect(arduino)
arduino.connect(wifi)

# Set bandwidth limits
wifi.set_bandwidth(1000)          # 1 Mbps bandwidth
arduino.set_bandwidth(500)        # 500 kbps bandwidth

# Power on devices
sensor.turn_on()
arduino.turn_on()
wifi.turn_on()

# Monitor bandwidth usage
current_bandwidth = wifi.get_bandwidth()
print(f"Current WiFi bandwidth: {current_bandwidth} kbps")

# Send data and monitor throughput
temperature = sensor.get_data()
wifi.send_data(temperature)
throughput = wifi.get_throughput()
print(f"Current throughput: {throughput} kbps")

print("Bandwidth control demo completed!")
```

### **2. Latency Measurement and Control**
```python
# Latency Control Example
# Create devices
ultrasonic = Sensor("ultrasonic")
arduino = Arduino("controller")
cloud = Cloud("aws_cloud")

# Connect devices
ultrasonic.connect(arduino)
arduino.connect(cloud)

# Set latency parameters
arduino.set_latency(50)           # 50ms processing latency
cloud.set_latency(200)            # 200ms cloud latency

# Power on devices
ultrasonic.turn_on()
arduino.turn_on()
cloud.turn_on()

# Measure latency
distance = ultrasonic.get_data()
start_time = arduino.get_processing_time()
cloud.send_data(distance)
end_time = cloud.get_processing_time()

total_latency = end_time - start_time
print(f"Total system latency: {total_latency} ms")
print(f"Arduino latency: {arduino.get_latency()} ms")
print(f"Cloud latency: {cloud.get_latency()} ms")

print("Latency measurement completed!")
```

### **3. Throughput Optimization**
```python
# Throughput Optimization Example
# Create devices
temp_sensor = Sensor("temp")
humidity_sensor = Sensor("hum")
arduino = Arduino("controller")
mqtt = MQTT("mqtt_broker")

# Connect devices
temp_sensor.connect(arduino)
humidity_sensor.connect(arduino)
arduino.connect(mqtt)

# Configure for optimal throughput
arduino.set_bandwidth(2000)       # 2 Mbps bandwidth
arduino.set_latency(10)           # 10ms low latency
mqtt.set_bandwidth(5000)          # 5 Mbps for MQTT

# Power on devices
temp_sensor.turn_on()
humidity_sensor.turn_on()
arduino.turn_on()
mqtt.turn_on()

# Optimize data transmission
temperature = temp_sensor.get_data()
humidity = humidity_sensor.get_data()

# Batch data for better throughput
sensor_data = f"Temp:{temperature},Hum:{humidity}"
mqtt.publish("sensors/data", sensor_data)

# Monitor throughput
current_throughput = mqtt.get_throughput()
packet_loss = mqtt.get_packet_loss()
print(f"MQTT throughput: {current_throughput} kbps")
print(f"Packet loss: {packet_loss}%")

print("Throughput optimization completed!")
```

### **4. Baudrate Configuration for Serial Communication**
```python
# Baudrate Configuration Example
# Create devices
gps = Sensor("gps")
arduino = Arduino("uno")
rpi = RaspberryPi("pi")

# Connect devices with serial communication
gps.connect(arduino, protocol="serial")
arduino.connect(rpi, protocol="serial")

# Configure baudrates
gps.set_baudrate(9600)            # GPS standard baudrate
arduino.set_baudrate(115200)       # High-speed Arduino baudrate
rpi.set_baudrate(115200)          # Match Arduino baudrate

# Power on devices
gps.turn_on()
arduino.turn_on()
rpi.turn_on()

# Test serial communication at different baudrates
gps_data = gps.get_data()
arduino.send_serial(gps_data)

# Monitor serial performance
arduino_baudrate = arduino.get_baudrate()
rpi_baudrate = rpi.get_baudrate()
response_time = arduino.get_response_time()

print(f"Arduino baudrate: {arduino_baudrate}")
print(f"Raspberry Pi baudrate: {rpi_baudrate}")
print(f"Serial response time: {response_time} ms")

print("Baudrate configuration completed!")
```

### **5. Time Delay and Timing Analysis**
```python
# Time Delay Analysis Example
# Create devices
button = Sensor("button")
arduino = Arduino("controller")
led = LED("status")
motor = Motor("actuator")

# Connect devices
button.connect(arduino)
arduino.connect(led)
arduino.connect(motor)

# Configure timing parameters
arduino.set_delay(10)             # 10ms processing delay
led.set_delay(5)                  # 5ms LED response delay
motor.set_delay(50)               # 50ms motor activation delay

# Power on devices
button.turn_on()
arduino.turn_on()
led.turn_on()
motor.turn_on()

# Measure timing chain
button_press = button.get_data()
arduino_start = arduino.get_processing_time()
led_response = led.get_processing_time()
motor_response = motor.get_processing_time()

# Calculate total response time
total_response = motor_response - button_press
arduino_processing = led_response - arduino_start
actuator_delay = motor_response - led_response

print(f"Total system response: {total_response} ms")
print(f"Arduino processing: {arduino_processing} ms")
print(f"Actuator delay: {actuator_delay} ms")

# Control actuators based on timing
if button_press == 1:
    led.turn_on()
    motor.activate()
    print("Button pressed - LED ON, Motor ON")
else:
    led.turn_off()
    motor.deactivate()
    print("Button released - LED OFF, Motor OFF")

print("Timing analysis completed!")
```

### **6. Network Performance Monitoring**
```python
# Network Performance Monitoring
# Create devices
temp_sensor = Sensor("temp")
pressure_sensor = Sensor("pressure")
arduino = Arduino("gateway")
wifi = WiFi("network")
cloud = Cloud("aws")

# Create network topology
temp_sensor.connect(arduino)
pressure_sensor.connect(arduino)
arduino.connect(wifi)
wifi.connect(cloud)

# Configure network parameters
wifi.set_bandwidth(1000)          # 1 Mbps
wifi.set_latency(100)             # 100ms latency
cloud.set_bandwidth(5000)         # 5 Mbps cloud connection

# Power on network
temp_sensor.turn_on()
pressure_sensor.turn_on()
arduino.turn_on()
wifi.turn_on()
cloud.turn_on()

# Monitor network performance
network_performance = wifi.analyze_performance()
packet_loss = wifi.get_packet_loss()
jitter = wifi.get_jitter()
queue_size = arduino.get_queue_size()

# Collect sensor data
temperature = temp_sensor.get_data()
pressure = pressure_sensor.get_data()

# Send data with performance monitoring
start_throughput = wifi.get_throughput()
cloud.send_data(f"Temp:{temperature},Pressure:{pressure}")
end_throughput = wifi.get_throughput()

print(f"Network bandwidth: {wifi.get_bandwidth()} kbps")
print(f"Network latency: {wifi.get_latency()} ms")
print(f"Packet loss: {packet_loss}%")
print(f"Network jitter: {jitter} ms")
print(f"Queue size: {queue_size} packets")
print(f"Throughput change: {end_throughput - start_throughput} kbps")

print("Network performance monitoring completed!")
```

### **7. Complete Performance Testing Sample**
```python
# Complete Performance Testing Sample
# Create test network with multiple performance parameters
sensor1 = Sensor("temp_sensor")
sensor2 = Sensor("humidity_sensor")
sensor3 = Sensor("pressure_sensor")
arduino = Arduino("controller")
rpi = RaspberryPi("gateway")
wifi = WiFi("wifi_module")
cloud = Cloud("aws_cloud")

# Connect devices in chain topology
sensor1.connect(arduino)
sensor2.connect(arduino)
sensor3.connect(arduino)
arduino.connect(rpi)
rpi.connect(wifi)
wifi.connect(cloud)

# Configure performance parameters for each device
sensor1.set_delay(5)               # 5ms sensor response delay
sensor2.set_delay(8)               # 8ms sensor response delay
sensor3.set_delay(6)               # 6ms sensor response delay
arduino.set_latency(15)            # 15ms processing latency
rpi.set_latency(25)                # 25ms gateway latency
wifi.set_bandwidth(2000)           # 2 Mbps WiFi bandwidth
wifi.set_latency(50)               # 50ms WiFi latency
cloud.set_bandwidth(10000)         # 10 Mbps cloud bandwidth
cloud.set_latency(100)             # 100ms cloud latency

# Power on all devices
sensor1.turn_on()
sensor2.turn_on()
sensor3.turn_on()
arduino.turn_on()
rpi.turn_on()
wifi.turn_on()
cloud.turn_on()

# Test 1: Bandwidth Measurement
print("=== BANDWIDTH TEST ===")
wifi_bandwidth = wifi.get_bandwidth()
cloud_bandwidth = cloud.get_bandwidth()
arduino_bandwidth = arduino.get_bandwidth()

print(f"WiFi Module Bandwidth: {wifi_bandwidth} kbps")
print(f"Cloud Connection Bandwidth: {cloud_bandwidth} kbps")
print(f"Arduino Bandwidth: {arduino_bandwidth} kbps")

# Test 2: Latency Measurement
print("\n=== LATENCY TEST ===")
start_time = sensor1.get_processing_time()
temp_data = sensor1.get_data()
arduino_time = arduino.get_processing_time()
rpi_time = rpi.get_processing_time()
end_time = cloud.get_processing_time()

sensor_latency = arduino_time - start_time
gateway_latency = rpi_time - arduino_time
network_latency = end_time - rpi_time
total_latency = end_time - start_time

print(f"Sensor to Arduino Latency: {sensor_latency} ms")
print(f"Arduino to Gateway Latency: {gateway_latency} ms")
print(f"Gateway to Cloud Latency: {network_latency} ms")
print(f"Total End-to-End Latency: {total_latency} ms")

# Test 3: Throughput Measurement
print("\n=== THROUGHPUT TEST ===")
start_throughput = wifi.get_throughput()

for i in range(5):
    temp = sensor1.get_data()
    humidity = sensor2.get_data()
    pressure = sensor3.get_data()
    data_packet = f"Temp:{temp},Hum:{humidity},Press:{pressure}"
    cloud.send_data(data_packet)

end_throughput = wifi.get_throughput()
throughput_change = end_throughput - start_throughput
avg_throughput = throughput_change / 5

print(f"Start Throughput: {start_throughput} kbps")
print(f"End Throughput: {end_throughput} kbps")
print(f"Average Throughput per Packet: {avg_throughput} kbps")

# Test 4: Time Delay Analysis
print("\n=== TIME DELAY TEST ===")
sensor1_delay = sensor1.get_delay()
sensor2_delay = sensor2.get_delay()
sensor3_delay = sensor3.get_delay()
arduino_delay = arduino.get_delay()
wifi_delay = wifi.get_delay()

print(f"Sensor 1 Response Delay: {sensor1_delay} ms")
print(f"Sensor 2 Response Delay: {sensor2_delay} ms")
print(f"Sensor 3 Response Delay: {sensor3_delay} ms")
print(f"Arduino Processing Delay: {arduino_delay} ms")
print(f"WiFi Transmission Delay: {wifi_delay} ms")

# Test 5: Network Performance Analysis
print("\n=== NETWORK ANALYSIS ===")
network_perf = wifi.analyze_performance()
packet_loss = wifi.get_packet_loss()
jitter = wifi.get_jitter()
queue_size = arduino.get_queue_size()
response_time = cloud.get_response_time()

print(f"Network Performance Score: {network_perf}")
print(f"Packet Loss Rate: {packet_loss}%")
print(f"Network Jitter: {jitter} ms")
print(f"Arduino Queue Size: {queue_size} packets")
print(f"Cloud Response Time: {response_time} ms")

# Test 6: Performance Summary
print("\n=== PERFORMANCE SUMMARY ===")
total_bandwidth = wifi_bandwidth + cloud_bandwidth
avg_latency = total_latency / 3
network_efficiency = (throughput_change / total_bandwidth) * 100

print(f"Total Available Bandwidth: {total_bandwidth} kbps")
print(f"Average Network Latency: {avg_latency} ms")
print(f"Network Efficiency: {network_efficiency:.2f}%")
print(f"Data Packets Transmitted: 5")
print(f"Total Data Volume: {throughput_change} kbps")

print("\nPerformance testing completed!")
print("All network parameters measured and analyzed.")
```

### **8. JSON Export of Simulation Logs**
```python
# JSON Export Example
# Create devices
temp_sensor = Sensor("temp")
arduino = Arduino("controller")
led = LED("status")

# Connect devices
temp_sensor.connect(arduino)
arduino.connect(led)

# Power on devices
temp_sensor.turn_on()
arduino.turn_on()
led.turn_on()

# Run simulation and log events
temperature = temp_sensor.get_data()
log.add_event("sensor_read", {"device": "temp_sensor", "value": temperature})

if temperature > 30:
    led.turn_on()
    log.add_event("actuator_activate", {"device": "led", "state": "on"})
else:
    led.turn_off()
    log.add_event("actuator_deactivate", {"device": "led", "state": "off"})

# Export simulation logs to JSON
simulation_logs = simulation.get_logs()
export.save_json("simulation_logs.json")

# Get export information
file_size = export.get_file_size()
print(f"Exported JSON file size: {file_size} bytes")
print("Simulation logs exported to simulation_logs.json")

# Example JSON structure:
# {
#   "simulation_id": "sim_001",
#   "timestamp": "2026-04-28T01:00:00Z",
#   "devices": [
#     {
#       "id": "temp_sensor",
#       "type": "Sensor",
#       "events": [
#         {
#           "timestamp": "2026-04-28T01:00:01Z",
#           "type": "sensor_read",
#           "data": {"value": 25.5}
#         }
#       ]
#     }
#   ],
#   "protocols": [
#     {
#       "type": "I2C",
#       "packets": [
#         {
#           "timestamp": "2026-04-28T01:00:01Z",
#           "source": "temp_sensor",
#           "destination": "controller",
#           "data": "temperature_reading"
#         }
#       ]
#     }
#   ]
# }

print("JSON export demo completed!")

### **8. Advanced Logging and Export**
```python
# Advanced Logging Example
# Create multi-device network
temp_sensor = Sensor("temp")
humidity_sensor = Sensor("hum")
ultrasonic = Sensor("distance")
arduino = Arduino("controller")
rpi = RaspberryPi("gateway")
cloud = Cloud("aws_cloud")

# Connect devices
temp_sensor.connect(arduino)
humidity_sensor.connect(arduino)
ultrasonic.connect(arduino)
arduino.connect(rpi)
rpi.connect(cloud)

# Power on all devices
temp_sensor.turn_on()
humidity_sensor.turn_on()
ultrasonic.turn_on()
arduino.turn_on()
rpi.turn_on()
cloud.turn_on()

# Collect sensor data with detailed logging
temperature = temp_sensor.get_data()
log.add_event("sensor_read", {
    "device": "temp_sensor",
    "value": temperature,
    "unit": "celsius",
    "timestamp": log.get_timestamp()
})

humidity = humidity_sensor.get_data()
log.add_event("sensor_read", {
    "device": "humidity_sensor",
    "value": humidity,
    "unit": "percent",
    "timestamp": log.get_timestamp()
})

distance = ultrasonic.get_data()
log.add_event("sensor_read", {
    "device": "ultrasonic",
    "value": distance,
    "unit": "cm",
    "timestamp": log.get_timestamp()
})

# Log network performance
network_performance = rpi.analyze_performance()
log.add_event("network_analysis", {
    "bandwidth": rpi.get_bandwidth(),
    "latency": rpi.get_latency(),
    "packet_loss": rpi.get_packet_loss(),
    "timestamp": log.get_timestamp()
})

# Send data to cloud with logging
sensor_data = f"Temp:{temperature},Hum:{humidity},Dist:{distance}"
cloud.send_data(sensor_data)
log.add_event("cloud_transmission", {
    "data": sensor_data,
    "destination": "aws_cloud",
    "timestamp": log.get_timestamp()
})

# Export comprehensive logs
all_logs = simulation.get_logs()
export.save_json("comprehensive_simulation_logs.json")

# Get device-specific logs
temp_logs = simulation.get_device_logs(temp_sensor)
export.save_json("temperature_sensor_logs.json")

# Get protocol-specific logs
i2c_logs = log.get_protocol_events("I2C")
export.save_json("i2c_protocol_logs.json")

print("Advanced logging and export completed!")
print("Files exported:")
print("- comprehensive_simulation_logs.json")
print("- temperature_sensor_logs.json")
print("- i2c_protocol_logs.json")
```

---

## 📤 **Export Functionality Guide**

### **How to Export Simulation Logs**

#### **Method 1: Basic Export**
```python
# Run your simulation
# ... your simulation code here ...

# Export all logs to JSON
simulation.export_json()
# This will create a file like "simulation_2026-04-28_01-00-00.json"
```

#### **Method 2: Custom Filename**
```python
# Export with custom filename
export.save_json("my_simulation_logs.json")
```

#### **Method 3: Selective Export**
```python
# Export only specific device logs
device_logs = simulation.get_device_logs(my_sensor)
export.save_json("sensor_only_logs.json")

# Export only protocol logs
protocol_logs = log.get_protocol_events("I2C")
export.save_json("i2c_only_logs.json")
```

### **JSON Export Structure**

#### **Complete Simulation Log Format**
```json
{
  "simulation_id": "sim_001",
  "timestamp": "2026-04-28T01:00:00Z",
  "duration": "00:05:30",
  "devices": [
    {
      "id": "temp_sensor",
      "type": "Sensor",
      "connections": ["controller"],
      "events": [
        {
          "timestamp": "2026-04-28T01:00:01Z",
          "type": "device_power_on",
          "data": {"power_consumption": "2.5mA"}
        },
        {
          "timestamp": "2026-04-28T01:00:02Z",
          "type": "sensor_read",
          "data": {"value": 25.5, "unit": "celsius"}
        }
      ]
    }
  ],
  "protocols": [
    {
      "type": "I2C",
      "packets": [
        {
          "timestamp": "2026-04-28T01:00:02Z",
          "source": "temp_sensor",
          "destination": "controller",
          "data": "0x19",
          "color": "orange"
        }
      ]
    }
  ],
  "performance": {
    "total_bandwidth": 1000,
    "average_latency": 50,
    "packet_loss": 0.1,
    "throughput": 850
  }
}
```

### **Export Features**

#### **Automatic Logging**
- All device operations are automatically logged
- Protocol communications are captured with timestamps
- Performance metrics are recorded continuously

#### **Export Options**
- **Full Export**: Complete simulation logs
- **Device-Specific**: Logs for individual devices
- **Protocol-Specific**: Logs for specific protocols
- **Performance-Only**: Network and device performance data

#### **File Management**
- Automatic timestamp-based naming
- Custom filename support
- File size optimization
- Multiple export formats support

### **Using Export Button**

#### **Web Interface Export**
1. Run your simulation
2. Click "Export" button in the simulator interface
3. Choose export type:
   - Complete Logs
   - Device Logs
   - Protocol Logs
   - Performance Data
4. Download generated JSON file

---

## ⏸️ **Pause/Resume Functionality**

### **How to Use Pause/Resume**

#### **Basic Operation**
1. **Start Simulation** - Click "▶️ Start" button
2. **Pause Simulation** - Click "⏸️ Pause" button
3. **Resume Simulation** - Button changes to "▶️ Resume" - click to continue
4. **State Preservation** - Simulation continues from exact pause point

#### **Button Behavior**
- **Initial State**: "⏸️ Pause" button
- **After Pause**: Button changes to "▶️ Resume"
- **After Resume**: Button changes back to "⏸️ Pause"
- **After Reset**: Button resets to "⏸️ Pause"

### **Pause/Resume Features**

#### **State Management**
```python
# Simulation state is automatically preserved
simulation_time = current_time  # Preserved during pause
device_states = current_states  # All device states saved
packet_positions = current_positions  # Packet positions saved
network_status = current_status  # Network conditions preserved
```

#### **What Gets Preserved**
- ✅ **Simulation Time**: Continues from exact pause point
- ✅ **Device States**: All on/off states maintained
- ✅ **Packet Positions**: Network packets freeze in place
- ✅ **Network Load**: Current load conditions preserved
- ✅ **Performance Metrics**: Bandwidth, latency, throughput maintained
- ✅ **Protocol States**: Current communication states saved

#### **Resume Behavior**
- **Seamless Continuation**: No data loss during pause
- **Packet Animation**: Packets continue from pause position
- **Time Counter**: Continues from paused time value
- **Device Operations**: Resume mid-operation if interrupted
- **Network Communication**: Continue ongoing transmissions

### **Pause/Resume Use Cases**

#### **Educational Demonstrations**
- Pause to explain specific network events
- Resume to continue demonstration
- Step-by-step protocol analysis

#### **Debugging and Analysis**
- Pause at critical moments for detailed analysis
- Resume to continue testing
- Examine packet positions and routes

#### **Performance Testing**
- Pause to measure system state
- Resume to continue performance monitoring
- Analyze network conditions at specific points

### **Technical Implementation**

#### **JavaScript Functions**
```javascript
// Toggle between pause and resume
function togglePauseResume() {
    const pauseResumeBtn = document.getElementById("pauseResumeBtn");
    
    if (isPaused) {
        // Resume logic
        isPaused = false;
        pauseResumeBtn.innerHTML = '⏸️ Pause';
        // Continue simulation from preserved state
    } else {
        // Pause logic
        isPaused = true;
        pauseResumeBtn.innerHTML = '▶️ Resume';
        // Preserve current simulation state
    }
}
```

#### **State Preservation**
```javascript
// State variables automatically preserved
let simulationTime = 0;        // Current simulation time
let packetCount = 0;           // Number of packets sent
let activePackets = [];        // Active packet positions
let deviceStates = {};         // Current device states
let networkMetrics = {};       // Performance metrics
```

#### **Command Line Export**
```python
# Export from script
simulation.export_json()

# Export with specific options
export.save_json("custom_name.json")
```

### **Export Use Cases**

#### **Research Analysis**
- Export data for academic research
- Analyze protocol performance
- Study device behavior patterns

#### **Debugging**
- Export detailed logs for troubleshooting
- Analyze timing issues
- Review communication patterns

#### **Documentation**
- Create simulation records
- Generate experiment reports
- Share simulation results

---

## 💡 **Validated Executable Scripts**

## 💡 **Validated Executable Scripts**

### **1. Basic LED Blinking**
```python
# Create devices
arduino = Arduino("uno")
led = LED("status")

# Connect LED to Arduino
arduino.connect(led)

# Power on system
arduino.turn_on()
led.turn_on()

# Blink LED
led.turn_on()
led.turn_off()
led.turn_on()
led.turn_off()

print("LED blinking completed!")
```

### **2. Traffic Signal System**
```python
# Create devices
arduino = Arduino("traffic_controller")
red_led = LED("red")
yellow_led = LED("yellow")
green_led = LED("green")

# Connect all LEDs to Arduino
arduino.connect(red_led)
arduino.connect(yellow_led)
arduino.connect(green_led)

# Power on system
arduino.turn_on()
red_led.turn_on()
yellow_led.turn_on()
green_led.turn_on()

# Traffic light sequence
red_led.turn_on()
yellow_led.turn_off()
green_led.turn_off()
red_led.turn_off()
yellow_led.turn_on()
green_led.turn_off()
red_led.turn_off()
yellow_led.turn_off()
green_led.turn_on()

print("Traffic signal system completed!")
```

### **3. LDR-Based Lighting**
```python
# LDR Sensor Based LED Control
# Create devices
ldr_sensor = Sensor("ldr")
arduino = Arduino("light_controller")
led = LED("room_light")

# Connect LDR to Arduino, Arduino to LED
ldr_sensor.connect(arduino)
arduino.connect(led)

# Power on system
ldr_sensor.turn_on()
arduino.turn_on()
led.turn_on()

# Light control based on LDR reading
light_level = ldr_sensor.get_data()
if light_level < 30:  # Dark environment
    led.turn_on()
    print("Dark detected - LED ON")
else:  # Bright environment
    led.turn_off()
    print("Bright detected - LED OFF")

print("LDR lighting control completed!")
```

### **4. Push Button LED Control**
```python
# Push Button LED Control
# Create devices
button = Sensor("push_button")
arduino = Arduino("button_controller")
led = LED("indicator")

# Connect button to Arduino, Arduino to LED
button.connect(arduino)
arduino.connect(led)

# Power on system
button.turn_on()
arduino.turn_on()
led.turn_on()

# Button control logic
button_state = button.get_data()
if button_state == 1:  # Button pressed
    led.turn_on()
    print("Button pressed - LED ON")
else:  # Button released
    led.turn_off()
    print("Button released - LED OFF")

print("Button LED control completed!")
```

### **5. Temperature Sensor with LED Control**
```python
# Temperature Sensor with LED Control
# Create devices
temp_sensor = Sensor("temp")
arduino = Arduino("temp_controller")
led = LED("warning_led")

# Connect sensor to Arduino, Arduino to LED
temp_sensor.connect(arduino)
arduino.connect(led)

# Power on system
temp_sensor.turn_on()
arduino.turn_on()
led.turn_on()

# Temperature monitoring
temperature = temp_sensor.get_data()
print(f"Temperature: {temperature}°C")

if temperature > 30:  # High temperature
    led.turn_on()
    print("High temperature detected - Warning LED ON")
else:  # Normal temperature
    led.turn_off()
    print("Normal temperature - LED OFF")

print("Temperature monitoring completed!")
```

### **6. Ultrasonic Sensor Proximity Detection**
```python
# Ultrasonic Sensor for Object Detection
# Create devices
ultrasonic = Sensor("ultrasonic")
arduino = Arduino("proximity_controller")
led = LED("proximity_led")

# Connect sensor to Arduino, Arduino to LED
ultrasonic.connect(arduino)
arduino.connect(led)

# Power on system
ultrasonic.turn_on()
arduino.turn_on()
led.turn_on()

# Proximity detection
distance = ultrasonic.get_data()
print(f"Distance: {distance} cm")

if distance < 20:  # Object closer than 20cm
    led.turn_on()
    print("Object detected nearby - LED ON")
else:  # No object nearby
    led.turn_off()
    print("No object detected - LED OFF")

print("Proximity detection completed!")
```

### **7. Temperature with Display**
```python
# Temperature with Display
# Create devices
temp_sensor = Sensor("temp")
arduino = Arduino("data_logger")
display = Display("lcd_screen")

# Connect components
temp_sensor.connect(arduino)
arduino.connect(display)

# Power on system
temp_sensor.turn_on()
arduino.turn_on()
display.turn_on()

# Display temperature
temperature = temp_sensor.get_data()
message = f"Temp: {temperature}°C"
display.show(message)
print(f"Displayed: {message}")

print("Temperature display system completed!")
```

### **8. GSM Module Message Sending**
```python
# GSM Module for SMS Sending
# Create devices
temp_sensor = Sensor("temp")
arduino = Arduino("gsm_controller")
gsm = GSM("sms_module")

# Connect components
temp_sensor.connect(arduino)
arduino.connect(gsm)

# Power on system
temp_sensor.turn_on()
arduino.turn_on()
gsm.turn_on()

# Send SMS based on temperature
temperature = temp_sensor.get_data()
if temperature > 35:  # High temperature threshold
    message = f"Warning: High temperature {temperature}°C detected!"
    phone_number = "+1234567890"
    gsm.send_sms(phone_number, message)
    print(f"SMS sent to {phone_number}: {message}")
else:
    print(f"Temperature normal ({temperature}°C) - No SMS sent")

print("GSM alert system completed!")
```

### **9. MQTT Protocol Data Publishing**
```python
# MQTT Protocol Data Publishing
# Create devices
temp_sensor = Sensor("temp")
humidity_sensor = Sensor("hum")
arduino = Arduino("mqtt_publisher")
mqtt_broker = MQTT("cloud_broker")

# Connect components
temp_sensor.connect(arduino)
humidity_sensor.connect(arduino)
arduino.connect(mqtt_broker)

# Power on system
temp_sensor.turn_on()
humidity_sensor.turn_on()
arduino.turn_on()
mqtt_broker.turn_on()

# Publish sensor data via MQTT
temperature = temp_sensor.get_data()
humidity = humidity_sensor.get_data()

# Publish to MQTT topics
mqtt_broker.publish("sensors/temperature", temperature)
mqtt_broker.publish("sensors/humidity", humidity)

print(f"Published: Temp={temperature}°C, Hum={humidity}%")
print("MQTT publishing completed!")
```

---

## 🔧 **Advanced Script Examples**

### **10. Multi-Sensor IoT System**
```python
# Complete IoT Monitoring System
# Create devices
temp_sensor = Sensor("temp")
humidity_sensor = Sensor("hum")
ldr_sensor = Sensor("ldr")
ultrasonic = Sensor("distance")
arduino = Arduino("central_controller")
rpi = RaspberryPi("gateway")
cloud = Cloud("aws_cloud")
led = LED("status")
display = Display("lcd")

# Create network topology
temp_sensor.connect(arduino)
humidity_sensor.connect(arduino)
ldr_sensor.connect(arduino)
ultrasonic.connect(arduino)
arduino.connect(rpi)
rpi.connect(cloud)
arduino.connect(led)
arduino.connect(display)

# Power on all devices
temp_sensor.turn_on()
humidity_sensor.turn_on()
ldr_sensor.turn_on()
ultrasonic.turn_on()
arduino.turn_on()
rpi.turn_on()
cloud.turn_on()
led.turn_on()
display.turn_on()

# Comprehensive monitoring
temp = temp_sensor.get_data()
humidity = humidity_sensor.get_data()
light = ldr_sensor.get_data()
distance = ultrasonic.get_data()

# Create status message
status = f"Temp:{temp}°C Hum:{humidity}% Light:{light}% Dist:{distance}cm"
display.show(status)
cloud.send_data(status)

# Control LED based on conditions
if temp > 30 or distance < 20:
    led.turn_on()
else:
    led.turn_off()

print(f"Monitoring: {status}")
print("Multi-sensor IoT system completed!")
```

---

## 🎯 **Professor Q&A - Script Writing Guidelines**

### **🔧 Basic Script Writing Process**

#### **Step 1: Device Creation**
```python
# Create devices with meaningful names
arduino = Arduino("main_controller")
led = LED("status_light")
sensor = TemperatureSensor("temp_sensor_01")
```

#### **Step 2: Network Connections**
```python
# Connect devices following IoT hierarchy
sensor.connect(arduino)     # Sensor → Controller (I2C Protocol)
arduino.connect(led)       # Controller → Actuator (GPIO Protocol)
```

#### **Step 3: System Initialization**
```python
# Power on all devices
sensor.turn_on()
arduino.turn_on()
led.turn_on()
```

#### **Step 4: Control Logic**
```python
# Add intelligent behavior
temperature = sensor.read()
if temperature > 30:
    led.turn_on()
else:
    led.turn_off()
```

---

## 🎓 **Professor-Specific Questions & Answers**

### **Q: "What is the logic behind device connections?"**
```python
# Answer: IoT follows hierarchical architecture
# Sensors → Controllers → Gateways → Cloud

# Physical layer connections
sensor.connect(arduino)        # Low-level communication (I2C/SPI)
arduino.connect(raspberry_pi)  # Data processing (Serial/UART)
raspberry_pi.connect(cloud)    # Network communication (WiFi)

# Each connection represents a real-world protocol
```

### **Q: "How do you handle multiple devices efficiently?"**
```python
# Answer: Use arrays and loops for scalability

# Create multiple sensors
sensors = []
for i in range(5):
    sensor = TemperatureSensor(f"temp_{i}")
    sensor.connect(arduino)
    sensors.append(sensor)

# Read all sensors efficiently
for sensor in sensors:
    temp = sensor.read()
    print(f"{sensor.id()}: {temp}°C")
```

### **Q: "What about error handling in your scripts?"**
```python
# Answer: Implement validation and error checking

def safe_sensor_read(sensor, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            value = sensor.read()
            if value is not None and 0 <= value <= 100:
                return value
        except:
            print(f"Attempt {attempt + 1} failed for {sensor.id()}")
    
    print(f"Sensor {sensor.id()} failed after {max_attempts} attempts")
    return None  # Default value on failure
```

### **Q: "How do you simulate real-world timing?"**
```python
# Answer: Use realistic delays and timing

import time

# Real-world sensor reading intervals
def real_world_monitoring():
    while True:
        temperature = sensor.read()
        humidity = humidity_sensor.read()
        
        # Process data
        process_sensor_data(temperature, humidity)
        
        # Real-world delay (sensors don't read instantly)
        time.sleep(5)  # Read every 5 seconds (realistic)
```

---

## 🔧 **Advanced Script Writing Concepts**

### **Custom Device Behaviors**
```python
# Answer: Create functions for complex behaviors

def smart_thermostat(target_temp=22):
    current_temp = temp_sensor.read()
    
    if current_temp < target_temp - 2:
        heater.turn_on()
        cooler.turn_off()
    elif current_temp > target_temp + 2:
        heater.turn_off()
        cooler.turn_on()
    else:
        heater.turn_off()
        cooler.turn_off()
    
    print(f"Temp: {current_temp}°C, Target: {target_temp}°C")
```

### **Data Logging and Storage**
```python
# Answer: Implement data collection for analysis

def log_sensor_data():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = temp_sensor.read()
    humidity = humidity_sensor.read()
    
    # Create log entry
    log_entry = f"{timestamp},{temperature},{humidity}"
    
    # Store for analysis (simulated)
    data_log.append(log_entry)
    print(f"Logged: {log_entry}")
```

### **Network Communication Patterns**
```python
# Answer: Demonstrate different communication patterns

def publish_to_cloud():
    # MQTT-style publishing
    sensor_data = {
        "device_id": "iot_001",
        "temperature": temp_sensor.read(),
        "humidity": humidity_sensor.read(),
        "timestamp": time.time()
    }
    
    cloud.publish("sensors/data", sensor_data)
    print(f"Published to cloud: {sensor_data}")
```

---

## 📚 **Protocol Implementation Examples**

### **I2C Protocol Communication**
```python
# Answer: I2C is for short-range, multi-device communication

def i2c_communication():
    # Multiple devices on same I2C bus
    temp_sensor.connect(arduino, address=0x48)  # Temperature sensor
    humidity_sensor.connect(arduino, address=0x40)  # Humidity sensor
    
    # Arduino acts as I2C master
    arduino.configure_i2c(frequency=100000)  # 100kHz I2C clock
```

### **Serial Communication**
```python
# Answer: Serial/UART for point-to-point communication

def serial_communication():
    # Arduino to Raspberry Pi communication
    arduino.connect(rpi, protocol="serial", baudrate=9600)
    
    # Send data in serial format
    data = f"TEMP:{temp_sensor.read()},HUM:{humidity_sensor.read()}"
    arduino.send_serial(data)
```

### **WiFi Communication**
```python
# Answer: WiFi for wireless network communication

def wifi_communication():
    # Connect to WiFi network
    rpi.connect(wifi_network, ssid="IoT_Network", password="secure123")
    
    # Send data to cloud
    cloud_data = {
        "device": "iot_sensor_001",
        "readings": get_sensor_readings()
    }
    rpi.send_http_post("https://api.iot-cloud.com/data", cloud_data)
```

---

## 🎯 **Debugging and Optimization**

### **Debugging Techniques**
```python
# Answer: Use systematic debugging approach

def debug_script():
    print("=== Debug Session Started ===")
    
    # Check device states
    print(f"Arduino state: {arduino.state}")
    print(f"Sensor state: {temp_sensor.state}")
    print(f"LED state: {led.state}")
    
    # Test connections
    print(f"Sensor connected to Arduino: {temp_sensor in arduino.connections}")
    print(f"Arduino connected to LED: {led in arduino.connections}")
    
    # Test sensor reading
    test_reading = temp_sensor.read()
    print(f"Test sensor reading: {test_reading}")
```

### **Performance Optimization**
```python
# Answer: Optimize for efficiency and speed

def optimized_monitoring():
    # Use efficient data structures
    sensor_data = {}
    
    # Batch sensor readings
    def read_all_sensors():
        sensor_data['temperature'] = temp_sensor.read()
        sensor_data['humidity'] = humidity_sensor.read()
        sensor_data['light'] = ldr_sensor.read()
        return sensor_data
    
    # Process data efficiently
    while True:
        data = read_all_sensors()
        process_batch_data(data)
        time.sleep(1)  # Optimized timing
```

---

## 🏆 **Key Points for Professor**

### **Educational Value**
- **Progressive Complexity**: From simple to advanced scripts
- **Real-World Relevance**: Mirrors actual IoT implementations
- **Protocol Understanding**: Visual learning of communication
- **Problem-Solving**: Debugging and optimization skills

### **Technical Excellence**
- **Scalable Architecture**: Handles multiple devices efficiently
- **Error Handling**: Robust and reliable code
- **Performance Optimization**: Efficient resource usage
- **Standards Compliance**: Follows industry protocols

---

## 📚 **Protocol Information**

### **Protocol Colors in Visualization**
- 🟠 **I2C**: Sensor to microcontroller communication
- 🟡 **GPIO**: Digital control signals
- 🟣 **Serial**: UART/RS232 communication
- 🔵 **WiFi**: Wireless network communication
- 🟢 **LoRa**: Long-range communication
- 🔴 **Zigbee**: Mesh network communication

### **Device Connection Rules**
- Sensors connect to controllers (Arduino, ESP32)
- Controllers connect to SBCs (RaspberryPi) or actuators
- SBCs connect to cloud services
- Actuators connect directly to controllers

---

## 🚀 **Getting Started**

1. **Open IoT Simulator**
2. **Go to Script Editor**
3. **Copy any script from above**
4. **Click "Run Simulation"**
5. **Watch protocol visualization**
6. **Modify and experiment!**

## 📖 **Additional Tips**

### **Best Practices**
- Always power on devices before using them
- Use meaningful device IDs for easier debugging
- Add print statements to monitor values
- Test simple connections first, then build complexity
- Use comments to document your code

### **Common Issues**
- Make sure devices are connected before running
- Check that devices are powered on
- Verify correct device IDs in connections
- Use appropriate time delays for realistic simulation

### **Troubleshooting**
- If simulation doesn't start, check device connections
- If protocols don't show, verify device types
- If LEDs don't work, ensure power is on
- Use the simulation log for error messages

**Happy IoT Learning!** 🎓🚀

---

## 📞 **Support**

For questions or issues with the IoT Simulator:
- Check the simulation log for error messages
- Verify device connections and power status
- Review script syntax and device IDs
- Consult the protocol visualization for debugging

**IoT Network Simulator - Making IoT Education Accessible!** 🌐💡
