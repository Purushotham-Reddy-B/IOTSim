ldr = Sensor("ldr_sensor")
arduino = Arduino("uno")
led = LED("status_led")
display = Display("intensity_display")
sensor2 = Sensor("backup_sensor")

# Create multiple connections to see more data flow
ldr.connect(arduino)
sensor2.connect(arduino)
arduino.connect(led)
arduino.connect(display)
led.connect(display)

# Power all devices to maximize packet flow
ldr.turn_on()
sensor2.turn_on()
arduino.turn_on()
led.turn_on()
display.turn_on()

# This creates more diverse packet types:
# - SENSOR packets from LDR and backup sensor
# - CONTROL packets from Arduino to LED/Display
# - DATA packets from LED to Display
