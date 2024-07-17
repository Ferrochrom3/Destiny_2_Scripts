import time
import tkinter

total_failed_attempts = 0
total_success_attempts = 0
consecutive_failed_attempts = 0


def safe_divide(numerator: float, denominator: float):
    return numerator / denominator if denominator != 0 else 0


def create_status(start_time: float):
    """
    Creates the following metrics related to boss yeeting:
    1. Total Time: Total amount of time spent afking
    2. Total Attempts: Total number of attempts to yeet the boss
    3. Failed Attempts: Number of attempts that failed to kill the boss
    4. Success Attempts: Number of attempts that successfully killed the boss
    5. Success Rate: How likely it is to kill the boss
    6. Average Time Per Attempt: On average, how long it takes to execute one cycle
    7. Average Time Per Success: On average, how long it takes to successfully kill the boss once

    Args:
        start_time (float): The time when the script started running.

    Returns:
        str: Current status of the execuction that has the above metrics.
    """
    total_time = time.time() - start_time
    total_attempts = total_success_attempts + total_failed_attempts

    success_rate = round(safe_divide(total_success_attempts, total_attempts) * 100, 2)
    average_time_per_attempt = round(safe_divide(total_time, total_attempts), 2)
    average_time_per_success = round(safe_divide(total_time, total_success_attempts), 2)

    status = (
        f"Total Attempts: {total_attempts}"
        f"\nFailed Attempts - {total_failed_attempts}"
        f"\nSuccess Attempts - {total_success_attempts}"
        f"\nSuccess Rate - {success_rate}%"
        f"\nAverage Time Per Attempt - {average_time_per_attempt}s"
        f"\nAverage Time Per Success - {average_time_per_success}s"
    )

    return status


def update_status(label: tkinter.Label, start_time: float, update_frequency: float):
    """
    Updates the status label every second.

    Args:
        label (tkinter.Label): The Tkinter Label widget to update.
        start_time (float): The time when the script started.
        update_frequency (float): How often to update the status, in milliseconds.
    """
    status = create_status(start_time)
    label.config(text=status)
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
    window.wm_attributes("-topmost", True)  # Keep the window on top
    window.wm_attributes("-disabled", True)  # Disable interaction with the window
    window.wm_attributes("-transparentcolor", "white")  # Set window to transparent so text overlays on screen

    # Create a Label with left-aligned text
    label = tkinter.Label(window, text="Loading...", font=(7), fg="black", bg="white", justify="left")
    label.pack()

    # Start the update loop
    update_status(label, start_time, update_frequency)

    window.mainloop()
