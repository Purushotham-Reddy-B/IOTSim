from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

def create_project_report():
    doc = SimpleDocTemplate("IoT_Simulator_Project_Report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.darkblue,
        alignment=TA_CENTER,
        spaceAfter=30
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.darkblue,
        spaceAfter=12
    )

    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.darkgreen,
        spaceAfter=10
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12
    )

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        spaceAfter=10
    )

    # Title
    story.append(Paragraph("IoT Network Simulator - Complete Project Report", title_style))
    story.append(Spacer(1, 0.2*inch))

    # Project Overview
    story.append(Paragraph("1. PROJECT OVERVIEW", heading_style))
    story.append(Paragraph(
        "The IoT Network Simulator is a comprehensive web-based application that allows users to create, "
        "visualize, and simulate IoT networks using Python scripts. The simulator provides an intuitive "
        "interface for designing complex IoT topologies and analyzing their behavior through visual "
        "animations and data packet flow.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))

    # Key Features
    story.append(Paragraph("2. KEY FEATURES", heading_style))
    
    features = [
        ["Feature", "Description"],
        ["Python Script Editor", "Write IoT network scripts using Python syntax with CodeMirror editor"],
        ["Visual Network Simulation", "Real-time visualization of IoT networks using Cytoscape.js"],
        ["Device Support", "30+ IoT device types including sensors, controllers, actuators, and communication modules"],
        ["Network Persistence", "Save and load network configurations with timestamps"],
        ["Trace File System", "NS2-style trace file generation for network analysis"],
        ["Export Functionality", "JSON export of simulation logs, device data, and performance metrics"],
        ["Pause/Resume", "Control simulation flow with pause and resume capabilities"],
        ["Packet Animation", "Visual representation of data packets flowing through the network"],
        ["Protocol Detection", "Automatic protocol identification (I2C, SPI, GPIO, WiFi, Bluetooth, LoRa, Zigbee)"],
        ["Performance Monitoring", "Real-time tracking of network load, active nodes, and packet counts"]
    ]
    
    feature_table = Table(features, colWidths=[2.5*inch, 4*inch])
    feature_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
        ('ALIGN', (0, 0), (1, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(feature_table)
    story.append(Spacer(1, 0.2*inch))

    # Project Structure
    story.append(Paragraph("3. PROJECT STRUCTURE", heading_style))
    
    structure = [
        ["File/Directory", "Description", "Size/Info"],
        ["app.py", "Flask backend with IoT classes and API endpoints", "651 lines"],
        ["templates/index.html", "Landing page with editor link", "16 lines"],
        ["templates/editor.html", "Python script editor with CodeMirror", "238 lines"],
        ["templates/simulation.html", "Network visualization and simulation interface", "907 lines"],
        ["static/cytoscape.min.js", "Cytoscape.js library for graph visualization", "361 KB"],
        ["static/style.css", "Custom styling for the application", "6 KB"],
        ["README.md", "Comprehensive documentation with script examples", "1623 lines"],
        ["enhanced_ldr_test.py", "Test script for LDR sensor simulation", "25 lines"],
        ["saved_networks/", "Directory for saved network configurations", "4 networks"],
        ["trace_files/", "Directory for NS2-style trace files", "Empty"],
        ["simulations.db", "SQLite database for simulation data", "12 KB"],
        ["data.json", "Sample network topology data", "610 bytes"]
    ]
    
    structure_table = Table(structure, colWidths=[2*inch, 2.5*inch, 2*inch])
    structure_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.black),
        ('ALIGN', (0, 0), (2, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (2, 0), 9),
        ('BOTTOMPADDING', (0, 0), (2, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(structure_table)
    story.append(Spacer(1, 0.2*inch))

    # Backend Architecture
    story.append(Paragraph("4. BACKEND ARCHITECTURE (app.py)", heading_style))
    story.append(Paragraph("The Flask backend implements the following components:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    backend_components = [
        ["Component", "Description"],
        ["IoTNetwork Class", "Manages network nodes, edges, and device states"],
        ["IoTDevice Class", "Base class for all IoT devices with turn_on/turn_off methods"],
        ["Device Classes", "30+ specific device classes (Sensor, Arduino, LED, WiFi, etc.)"],
        ["validate_python_script()", "Validates Python syntax and device creation"],
        ["/simulate Endpoint", "Executes script and returns network topology"],
        ["/save_network Endpoint", "Saves network configuration to JSON file"],
        ["/load_network Endpoint", "Loads saved network from JSON file"],
        ["/list_networks Endpoint", "Lists all saved networks with metadata"],
        ["/delete_network Endpoint", "Deletes saved network files"],
        ["/create_trace_file Endpoint", "Creates NS2-style trace files"],
        ["/append_trace Endpoint", "Appends trace events to existing files"],
        ["/list_trace_files Endpoint", "Lists all trace files"],
        ["/get_trace_file Endpoint", "Downloads trace files"],
        ["/delete_trace_file Endpoint", "Deletes trace files"]
    ]
    
    backend_table = Table(backend_components, colWidths=[2.5*inch, 4*inch])
    backend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.lightyellow),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
        ('ALIGN', (0, 0), (1, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(backend_table)
    story.append(Spacer(1, 0.2*inch))

    # Device Types
    story.append(Paragraph("5. SUPPORTED DEVICE TYPES", heading_style))
    story.append(Paragraph("The simulator supports 30+ IoT device types organized into categories:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    device_categories = [
        ["Category", "Device Types"],
        ["Sensors", "Sensor, TemperatureSensor, HumiditySensor, LDRSensor, UltrasonicSensor, PressureSensor, MotionSensor"],
        ["Controllers", "Arduino, ESP32, ESP8266, STM32, PIC, RaspberryPi, BeagleBone, JetsonNano"],
        ["Actuators", "LED, Motor, Servo, Buzzer, Display, Relay, Solenoid"],
        ["Communication", "WiFi, Bluetooth, LoRa, Zigbee, GSM, MQTT, Ethernet"],
        ["Power", "Battery, PowerSupply, SolarPanel"],
        ["Storage", "SDCard, EEPROM, FlashMemory"],
        ["Components", "Resistor, Capacitor, Button, Switch, Potentiometer"],
        ["Network", "Gateway, Router, Switch, Server, Cloud, Mobile, Camera"]
    ]
    
    device_table = Table(device_categories, colWidths=[1.5*inch, 5*inch])
    device_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.lavender),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
        ('ALIGN', (0, 0), (1, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(device_table)
    story.append(Spacer(1, 0.2*inch))

    story.append(PageBreak())

    # Frontend Features
    story.append(Paragraph("6. FRONTEND FEATURES", heading_style))
    
    story.append(Paragraph("6.1 Editor Interface (editor.html)", subheading_style))
    editor_features = [
        "CodeMirror integration with Python syntax highlighting",
        "Monokai theme for better code readability",
        "Validate button to check script syntax",
        "Run Simulation button to execute and visualize",
        "Load Example button to load sample scripts",
        "Save Network button to persist network configurations",
        "Load Network button to retrieve saved networks",
        "Modal dialog for network management (load/delete)"
    ]
    for feature in editor_features:
        story.append(Paragraph(f"• {feature}", normal_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph("6.2 Simulation Interface (simulation.html)", subheading_style))
    sim_features = [
        "Cytoscape.js for interactive network visualization",
        "Breadthfirst layout algorithm for automatic graph arrangement",
        "Color-coded nodes by device type (30+ unique colors/shapes)",
        "Real-time packet animation along network edges",
        "Start/Pause/Resume/Reset simulation controls",
        "Step-by-step simulation mode",
        "Packet mode toggle (Basic/Advanced/Visual)",
        "Export JSON data button",
        "Download trace file button (.tr format)",
        "Clear trace data button",
        "Real-time status display (time, packets, load, nodes)",
        "Simulation log with timestamped events",
        "Protocol detection and labeling",
        "Edge activation animations during data flow"
    ]
    for feature in sim_features:
        story.append(Paragraph(f"• {feature}", normal_style))
    story.append(Spacer(1, 0.2*inch))

    # Protocol Detection
    story.append(Paragraph("7. PROTOCOL DETECTION SYSTEM", heading_style))
    story.append(Paragraph("The simulator automatically detects communication protocols based on device types:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    protocols = [
        ["Protocol", "Source Device", "Target Device", "Description"],
        ["I2C", "Sensor", "Arduino/Gateway", "Inter-Integrated Circuit protocol"],
        ["SPI", "Sensor", "RaspberryPi", "Serial Peripheral Interface"],
        ["UART", "Sensor", "Arduino/ESP32", "Universal Asynchronous Receiver-Transmitter"],
        ["GPIO", "Arduino/RPi/ESP32", "Motor/Actuator", "General Purpose Input/Output"],
        ["WiFi", "WiFi Module", "Gateway/Cloud", "Wireless network communication"],
        ["Bluetooth", "Bluetooth Module", "Mobile/Gateway", "Short-range wireless"],
        ["LoRa", "LoRa Module", "Gateway/Cloud", "Long-range wireless"],
        ["Zigbee", "Zigbee Module", "Gateway/Router", "Mesh network protocol"],
        ["MQTT", "Gateway/Router", "Cloud/Server", "Message Queuing Telemetry Transport"],
        ["HTTP", "Gateway/Router", "Cloud/Server", "HyperText Transfer Protocol"]
    ]
    
    protocol_table = Table(protocols, colWidths=[1*inch, 1.5*inch, 1.5*inch, 2.5*inch])
    protocol_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (3, 0), colors.lightcoral),
        ('TEXTCOLOR', (0, 0), (3, 0), colors.black),
        ('ALIGN', (0, 0), (3, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (3, 0), 9),
        ('BOTTOMPADDING', (0, 0), (3, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(protocol_table)
    story.append(Spacer(1, 0.2*inch))

    # Saved Networks
    story.append(Paragraph("8. SAVED NETWORKS", heading_style))
    story.append(Paragraph("The following network configurations are currently saved:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    saved_networks = [
        ["Network Name", "Filename", "Created Date"],
        ["Industry system", "Industry system_20260403_214541.json", "April 3, 2026"],
        ["Smart Home Automation", "smart home automation network_20260403_214401.json", "April 3, 2026"],
        ["LED LDR", "LED LDR_20260428_114225.json", "April 28, 2026"],
        ["Unnamed", "!_20260402_210630.json", "April 2, 2026"]
    ]
    
    networks_table = Table(saved_networks, colWidths=[2*inch, 3*inch, 2*inch])
    networks_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), colors.lightsteelblue),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.black),
        ('ALIGN', (0, 0), (2, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (2, 0), 10),
        ('BOTTOMPADDING', (0, 0), (2, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(networks_table)
    story.append(Spacer(1, 0.2*inch))

    # Documentation
    story.append(Paragraph("9. DOCUMENTATION (README.md)", heading_style))
    story.append(Paragraph("The README.md file contains comprehensive documentation including:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    doc_sections = [
        "Basic script structure and how to write IoT scripts",
        "Complete device inventory with all 30+ device types",
        "Network performance parameters (bandwidth, latency, throughput)",
        "Performance monitoring functions",
        "Export and logging functions",
        "8 detailed network performance script examples",
        "Export functionality guide with JSON structure",
        "Pause/Resume functionality documentation",
        "6 validated executable script examples",
        "Technical implementation details"
    ]
    for section in doc_sections:
        story.append(Paragraph(f"• {section}", normal_style))
    story.append(Spacer(1, 0.2*inch))

    story.append(PageBreak())

    # Example Scripts
    story.append(Paragraph("10. EXAMPLE SCRIPTS", heading_style))
    story.append(Paragraph("The README includes several validated executable scripts:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    examples = [
        ["Script Name", "Description", "Devices Used"],
        ["Basic LED Blinking", "Simple LED on/off demonstration", "Arduino, LED"],
        ["Traffic Signal System", "Three-LED traffic light sequence", "Arduino, 3 LEDs"],
        ["LDR-Based Lighting", "Light sensor controlling LED", "LDR Sensor, Arduino, LED"],
        ["Push Button LED Control", "Button-controlled LED", "Button Sensor, Arduino, LED"],
        ["Temperature Sensor", "Temperature monitoring with LED warning", "Temp Sensor, Arduino, LED"],
        ["Ultrasonic Proximity", "Object detection with distance sensor", "Ultrasonic Sensor, Arduino, LED"],
        ["Bandwidth Control", "Bandwidth measurement and control", "Sensor, Arduino, WiFi"],
        ["Latency Measurement", "End-to-end latency analysis", "Ultrasonic, Arduino, Cloud"],
        ["Throughput Optimization", "Data transmission optimization", "2 Sensors, Arduino, MQTT"],
        ["Baudrate Configuration", "Serial communication setup", "GPS, Arduino, RaspberryPi"]
    ]
    
    examples_table = Table(examples, colWidths=[1.8*inch, 2.5*inch, 2.2*inch])
    examples_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), colors.lightpink),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.black),
        ('ALIGN', (0, 0), (2, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (2, 0), 9),
        ('BOTTOMPADDING', (0, 0), (2, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(examples_table)
    story.append(Spacer(1, 0.2*inch))

    # API Endpoints
    story.append(Paragraph("11. API ENDPOINTS", heading_style))
    story.append(Paragraph("The Flask application provides the following REST API endpoints:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    api_endpoints = [
        ["Endpoint", "Method", "Purpose"],
        ["/", "GET", "Landing page"],
        ["/editor", "GET", "Python script editor"],
        ["/simulation", "GET", "Network simulation viewer"],
        ["/simulate", "POST", "Execute script and return network data"],
        ["/save_network", "POST", "Save network configuration"],
        ["/load_network", "POST", "Load saved network"],
        ["/list_networks", "GET", "List all saved networks"],
        ["/delete_network", "POST", "Delete a saved network"],
        ["/create_trace_file", "POST", "Create new trace file"],
        ["/append_trace", "POST", "Append events to trace file"],
        ["/list_trace_files", "GET", "List all trace files"],
        ["/get_trace_file/<filename>", "GET", "Download trace file"],
        ["/delete_trace_file", "POST", "Delete trace file"]
    ]
    
    api_table = Table(api_endpoints, colWidths=[2*inch, 1.5*inch, 3*inch])
    api_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), colors.lightgoldenrodyellow),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.black),
        ('ALIGN', (0, 0), (2, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (2, 0), 10),
        ('BOTTOMPADDING', (0, 0), (2, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(api_table)
    story.append(Spacer(1, 0.2*inch))

    # Trace File Format
    story.append(Paragraph("12. TRACE FILE FORMAT (NS2-style)", heading_style))
    story.append(Paragraph("Trace files use NS2 format with the following structure:", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Format: time event source target packetType description", code_style))
    story.append(Paragraph("Event Types: s=send, r=receive, d=drop, f=forward", code_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Example trace entry:", normal_style))
    story.append(Paragraph("0.123456 s sensor01 arduino01 i2c \"Temperature reading sent\"", code_style))
    story.append(Spacer(1, 0.2*inch))

    # Export Format
    story.append(Paragraph("13. JSON EXPORT FORMAT", heading_style))
    story.append(Paragraph("The export functionality generates comprehensive JSON files with:", normal_style))
    story.append(Spacer(1, 0.1*inch))

    export_fields = [
        "simulation_id: Unique identifier for the simulation",
        "timestamp: ISO format timestamp of export",
        "simulation_time: Total simulation duration in seconds",
        "packet_count: Total number of packets transmitted",
        "devices: Array of all devices with type, connections, and status",
        "protocols: Array of protocols used with packet counts",
        "performance: Network load, active nodes, active packets",
        "trace_data: Complete trace event history",
        "network_topology: Complete graph structure with nodes and edges"
    ]
    for field in export_fields:
        story.append(Paragraph(f"• {field}", normal_style))
    story.append(Spacer(1, 0.2*inch))

    # Technologies Used
    story.append(Paragraph("14. TECHNOLOGIES USED", heading_style))
    
    technologies = [
        ["Category", "Technology", "Purpose"],
        ["Backend", "Python", "Server-side logic and IoT classes"],
        ["Backend", "Flask", "Web framework and API"],
        ["Frontend", "HTML5", "Page structure"],
        ["Frontend", "JavaScript", "Client-side logic and simulation"],
        ["Frontend", "Cytoscape.js", "Graph visualization"],
        ["Frontend", "CodeMirror", "Code editor with syntax highlighting"],
        ["Data Storage", "JSON", "Network configurations and exports"],
        ["Data Storage", "SQLite", "Simulation database (simulations.db)"],
        ["Styling", "CSS3", "User interface styling"],
        ["Documentation", "Markdown", "README documentation"]
    ]
    
    tech_table = Table(technologies, colWidths=[1.5*inch, 2*inch, 3*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), colors.thistle),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.black),
        ('ALIGN', (0, 0), (2, -1), TA_LEFT),
        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (2, 0), 10),
        ('BOTTOMPADDING', (0, 0), (2, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(tech_table)
    story.append(Spacer(1, 0.2*inch))

    # Conclusion
    story.append(Paragraph("15. CONCLUSION", heading_style))
    story.append(Paragraph(
        "The IoT Network Simulator is a feature-rich application that provides a complete environment for "
        "designing, visualizing, and analyzing IoT networks. With support for 30+ device types, automatic "
        "protocol detection, real-time simulation, and comprehensive export capabilities, it serves as an "
        "excellent tool for education, research, and development in the IoT domain.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "The project demonstrates strong software engineering practices with modular architecture, "
        "comprehensive documentation, and user-friendly interfaces. The combination of Flask backend "
        "and JavaScript frontend provides a responsive and interactive experience for users.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "Future enhancements could include additional device types, more sophisticated protocol simulation, "
        "performance optimization for large networks, and integration with real IoT hardware.",
        normal_style
    ))

    # Build the PDF
    doc.build(story)
    print("PDF report generated successfully: IoT_Simulator_Project_Report.pdf")

if __name__ == "__main__":
    create_project_report()
