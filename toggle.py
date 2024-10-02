from machine import Pin
import time

# Setup LED and button
led1 = Pin(16, Pin.OUT)  # LED connected to GP16 (LED1)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Button connected to GPIO 22

# Initialize state variables
led_state = False  # Start with LED off
previous_button_state = 0
debounce_delay = 200  # 200 ms debounce delay
last_debounce_time = time.ticks_ms()

while True:
    current_button_state = sw5.value()

    # If button state has changed
    if current_button_state != previous_button_state:
        last_debounce_time = time.ticks_ms()  # Reset the debounce timer

    # If enough time has passed since the last debounce
    if (time.ticks_ms() - last_debounce_time) > debounce_delay:
        if current_button_state == 1 and previous_button_state == 0:
            led_state = not led_state  # Toggle the LED state
            print("LED Toggled: ", led_state)  # Debug to show LED state change

    # Set LED state based on toggled value
    led1.value(led_state)

    previous_button_state = current_button_state
