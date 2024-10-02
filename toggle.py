from machine import Pin
import time

# Setup LED on GPIO 16 and Button on GPIO 22
led1 = Pin(16, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Variables to store the LED state and debounce delay
led_state = False
previous_button_state = 0
debounce_delay = 200  # 200 ms debounce delay
last_debounce_time = time.ticks_ms()

while True:
    # Read the button state
    current_button_state = sw5.value()

    # Check if the button state changed and debounce
    if current_button_state != previous_button_state:
        last_debounce_time = time.ticks_ms()

    if (time.ticks_ms() - last_debounce_time) > debounce_delay:
        # Toggle the LED state when the button is pressed
        if current_button_state == 1 and previous_button_state == 0:
            led_state = not led_state

    # Set the LED based on the state
    led1.value(led_state)
    previous_button_state = current_button_state
