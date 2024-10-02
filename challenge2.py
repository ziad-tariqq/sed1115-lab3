from machine import Pin

led_onboard = Pin(25, Pin.OUT)

# Turn on the onboard LED
led_onboard.on()


# Setup LEDs and buttons
led1 = Pin(18, Pin.OUT)  # LED1 on GPIO 18
led2 = Pin(17, Pin.OUT)  # LED2 on GPIO 17
led3 = Pin(16, Pin.OUT)  # LED3 on GPIO 16
led4 = Pin(25, Pin.OUT)  # Onboard LED on GPIO 25

sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)  # Button 1 on GPIO 10
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)  # Button 2 on GPIO 11
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Button 3 on GPIO 12
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)  # Button 4 on GPIO 13

while True:
    # Button controls for LEDs
    led1.value(sw1.value())  # LED1 controlled by Button 1
    led2.value(sw2.value())  # LED2 controlled by Button 2
    led3.value(sw3.value())  # LED3 controlled by Button 3
    led4.value(sw4.value())  # Onboard LED controlled by Button 4
