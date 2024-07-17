import sys
import os
import time
import tkinter

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import relaunch

number_of_runs = 0

number_of_chests_obtained = 0
number_of_chests_missed = 0
missed_chests = []
number_of_chests_before_reset = 35

number_of_drops = 0


def safe_divide(numerator: float, denominator: float):
    return numerator / denominator if denominator != 0 else 0


def create_status(start_time: float):
    """
    Creates the following metrics related to chest collection:
    1. Number of Runs: The total number of runs.
    2. Number of Chests Obtained: The total number of chests opened.
    3. Number of Drops: The total number of exotic class item obtained.
    4. Number of Missed Chests: The number of chests missed when trying to open a chest (could due to various reasons).
    5. Missed Chest Rate: How much % of chests are missed.
    6. Drop Rate: The chance of a an exotic class item drop.
    7. Average Chests Per Run: On average, how many chests obtained for each run.
    8. Average Time Taken For One Chest: On average, how long does it take to get one chest.
    9. Average Time Per Drop: On average, how long does it take to get one drop.
    10. Number of Missed The Landing Relaunch: The amout of times the mouse cursor did not move to the landing zone correctly when relaunching The Landing.
    11. Number of Missed The Pale Heart Relaunch: The amount of times the mouse cursor did not move to the landing zone correctly when relaunching The Pale Heart.

    Args:
        start_time (float): The time when the script started.
    """

    total_time_seconds = round(time.time() - start_time)
    total_time_minutes = round((time.time() - start_time) / 60, 2)
    total_time_hours = round((time.time() - start_time) / 3600, 2)
    total_time = f"{total_time_seconds} seconds | {total_time_minutes} minutes | {total_time_hours} hours"

    average_chests_per_run = round(safe_divide(number_of_chests_obtained, number_of_runs), 2)
    average_time_taken_for_one_chest = round(safe_divide(total_time_seconds, number_of_chests_obtained), 2)
    drop_rate = round(safe_divide(number_of_drops, number_of_chests_obtained) * 100, 2)
    missed_chest_rate = round(safe_divide(number_of_chests_missed, number_of_chests_obtained + number_of_chests_missed) * 100, 2)
    average_time_per_drop = round(safe_divide(total_time_seconds, number_of_drops), 2)

    status = (
        f"Total Time: {total_time}"
        f"\nNumber of Runs: {number_of_runs}"
        f"\nNumber of Chests Obtained: {number_of_chests_obtained}"
        f"\nNumber of Drops: {number_of_drops}"
        f"\nNumber of Missed Chests: {number_of_chests_missed}"
        f"\nDrop Rate: {drop_rate}%"
        f"\nMissed Chest Rate: {missed_chest_rate}%"
        f"\nAverage Chests Per Run: {average_chests_per_run}"
        f"\nAverage Time Taken For One Chest: {average_time_taken_for_one_chest}s"
        f"\nAverage Time Per Drop: {average_time_per_drop}"
        f"\nNumber of Missed The Landing Relaunch: {relaunch.number_of_missed_the_landing_relaunch}"
        f"\nNumber of Missed The Pale Heart Relaunch: {relaunch.number_of_missed_the_pale_heart_relaunch}"
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
    window.attributes("-topmost", True)  # Keep the window on top
    window.attributes("-disabled", True)  # Disable interaction with the window
    window.attributes("-alpha", 0.5)

    # Create a Label with left-aligned text
    label = tkinter.Label(window, text="Loading...", font=(10), fg="black", bg="white", justify="left")
    label.pack()

    # Start the update loop
    update_status(label, start_time, update_frequency)

    window.mainloop()
