import time
from bearlibterminal import terminal

# Initialize the terminal
terminal.open()

# Set the text to be displayed
text = "Flashing text"

# Set the flashing frequency (in seconds)
frequency = 0.5

while True:
  # Clear the screen
  terminal.clear()

  # Toggle the flashing effect
  if time.time() % frequency < frequency / 2:
    terminal.print(0, 0, text)
  
  # Refresh the terminal to update the display
  terminal.refresh()

  # Check if there is any input available
  if terminal.has_input():
    # Read a key press from the user if there is input available
    key = terminal.read()

    # Check if the key press is the "Q" key
    if key == terminal.TK_Q:
      # Exit the loop if the "Q" key was pressed
      break

# Close the terminal when the loop is finished
terminal.close()
