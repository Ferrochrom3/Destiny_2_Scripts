import time
import tkinter
import win32con
import win32gui

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
    4 Consecutive Failed Attempts: Number of consecutive failed attempts, run will be reset after reaching 10
    5. Success Attempts: Number of attempts that successfully killed the boss
    6. Success Rate: How likely it is to kill the boss
    7. Average Time Per Attempt: On average, how long it takes to execute one cycle
    8. Average Time Per Success: On average, how long it takes to successfully kill the boss once

    Args:
        start_time (float): The time when the script started running.

    Returns:
        str: Current status of the execuction that has the above metrics.
    """
    total_time_seconds = round(time.time() - start_time)
    total_time_minutes = round((time.time() - start_time) / 60, 2)
    total_time_hours = round((time.time() - start_time) / 3600, 2)
    total_time = f"{total_time_seconds} seconds | {total_time_minutes} minutes | {total_time_hours} hours"

    total_attempts = total_success_attempts + total_failed_attempts
    success_rate = round(safe_divide(total_success_attempts, total_attempts) * 100, 2)

    average_time_per_attempt_seconds = round(safe_divide(total_time_seconds, total_attempts), 2)
    average_time_per_attempt_minutes = round(safe_divide(total_time_minutes, total_attempts), 2)
    average_time_per_attempt_hours = round(safe_divide(total_time_hours, total_attempts), 2)
    average_time_per_attempt = f"{average_time_per_attempt_seconds} seconds | {average_time_per_attempt_minutes} minutes | {average_time_per_attempt_hours} hours"

    average_time_per_success_seconds = round(safe_divide(total_time_seconds, total_success_attempts), 2)
    average_time_per_success_minutes = round(safe_divide(total_time_minutes, total_success_attempts), 2)
    average_time_per_success_hours = round(safe_divide(total_time_hours, total_success_attempts), 2)
    average_time_per_success = f"{average_time_per_success_seconds} seconds | {average_time_per_success_minutes} minutes | {average_time_per_success_hours} hours"

    status = (
        f"Total Time: {total_time}"
        f"\nTotal Attempts: {total_attempts}"
        f"\nFailed Attempts - {total_failed_attempts}"
        f"\nConsecutive Failed Attempts: {consecutive_failed_attempts}"
        f"\nSuccess Attempts - {total_success_attempts}"
        f"\nSuccess Rate - {success_rate}%"
        f"\nAverage Time Per Attempt - {average_time_per_attempt}"
        f"\nAverage Time Per Success - {average_time_per_success}"
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


def make_window_click_through(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)  # Get the current window style
    ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT  # Add the WS_EX_LAYERED and WS_EX_TRANSPARENT styles to make it click-through
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)  # Set the new window style


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
    label = tkinter.Label(window, text="Loading...", font=("Arial", 10), fg="black", bg="white", justify="left")
    label.pack()

    window.geometry("+0+600")  # Move window down by 600 pixels

    hwnd = win32gui.FindWindow(None, window.winfo_toplevel().title())  # Get the top level window title, which will be Tkinter overlay window
    make_window_click_through(hwnd)  # Make the overlay window click-throughable

    # Start the update loop
    update_status(label, start_time, update_frequency)

    window.mainloop()
