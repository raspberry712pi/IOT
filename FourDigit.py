import RPi.GPIO as GPIO
import time
from datetime import datetime

# GPIO setup
GPIO.setmode(GPIO.BCM)
segments = [2, 3, 4, 17, 27, 22, 10] # Adjust these pins as per your wiring
digits = [11, 5, 6, 13] # Adjust these pins as per your wiring

# Set up segment pins
for seg in segments:
    GPIO.setup(seg, GPIO.OUT)
    GPIO.output(seg, 0)

# Set up digit control pins
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

# Segment configurations for numbers 0-9
number_map = {
    '0': (1, 1, 1, 1, 1, 1, 0),
    '1': (0, 1, 1, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1),
    '3': (1, 1, 1, 1, 0, 0, 1),
    '4': (0, 1, 1, 0, 0, 1, 1),
    '5': (1, 0, 1, 1, 0, 1, 1),
    '6': (1, 0, 1, 1, 1, 1, 1),
    '7': (1, 1, 1, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1),
}

def display_digit(digit_index, num):
    # Turn off all digit pins
    for d in digits:
        GPIO.output(d, 1)
    
    # Set segments for the current number
    seg_values = number_map.get(num, (0, 0, 0, 0, 0, 0, 0))
    for i in range(7):
        GPIO.output(segments[i], seg_values[i])
    
    # Enable the selected digit
    GPIO.output(digits[digit_index], 0)
    time.sleep(0.001) # Small delay to stabilize the display
    GPIO.output(digits[digit_index], 1)

try:
    while True:
        # Get current time in HHMM format
        current_time = datetime.now().strftime("%H%M")
        
        # Display each digit on the 4-digit display
        for i, digit in enumerate(current_time):
            display_digit(i, digit)
            time.sleep(0.005) # Short delay between digits for multiplexing

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

