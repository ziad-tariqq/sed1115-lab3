from machine import Pin

# Define the inputs and outputs
led1 = Pin(18, Pin.OUT)  # LED connected to GPIO 18
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Button connected to GPIO 22 with pull-down

while True:
    # LED on when button is not pressed, off when button is pressed
    if sw5.value() != 1:
        led1.on()
    else:
        led1.off()
