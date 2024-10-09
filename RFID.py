from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

# Create an instance of the SimpleMFRC522 class
reader = SimpleMFRC522()

try:
    # Ask the user whether to read or write
    action = input("Type 'write' to write data or 'read' to read data: ").strip().lower()

    if action == 'write':
        # Writing mode
        text = input("Enter the data you want to write to the tag: ")
        print("Now place your tag near the reader to write the data...")
        reader.write(text)
        print("Data written successfully!")

    elif action == 'read':
        # Reading mode
        print("Hold a tag near the reader to read the data...")
        id, text = reader.read()
        print(f"ID: {id}\nText: {text}")

    else:
        print("Invalid option. Please type 'write' or 'read'.")

except Exception as e:
    print(f"Error: {e}")

finally:
    GPIO.cleanup()
