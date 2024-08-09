import tkinter

current_status = "None"


def update_status(label: tkinter.Label, start_time: float, update_frequency: float):
    """
    Updates the status label every second.

    Args:
        label (tkinter.Label): The Tkinter Label widget to update.
        start_time (float): The time when the script started.
        update_frequency (float): How often to update the status, in milliseconds.
    """
    label.config(text=current_status)
    label.after(update_frequency, update_status, label, start_time, update_frequency)  # Schedule the next update


def display_status(start_time: float, update_frequency: float):
    """
    Displays and updates the afk status in a Tkinter overlay window every "update_frequency" milliseconds.

    Args:
        start_time (float): The time when the script started.
        update_frequency (float): How often to update the status, in milliseconds.
    """
    window = tkinter.Tk()
    window.overrideredirect(True)  # Remove window title bar and borders
    window.lift()  # Show Tkinter window
    window.attributes("-topmost", True)  # Keep the window on top
    window.attributes("-disabled", True)  # Disable interaction with the window
    window.attributes("-alpha", 0.5)

    # Create a Label with left-aligned text
    label = tkinter.Label(window, text="Loading...", font=("Arial", 15), fg="black", bg="white", justify="left")
    label.pack()

    # Start the update loop
    update_status(label, start_time, update_frequency)

    window.mainloop()
