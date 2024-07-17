import sys
import os
import time

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


def display_status(start_time: float):
    """
    Shows the following metrics related to chest collection:
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

    try:
        total_time = time.time() - start_time
        average_chests_per_run = number_of_chests_obtained / number_of_runs
        average_time_taken_for_one_chest = total_time / number_of_chests_obtained
        drop_rate = round((number_of_drops / number_of_chests_obtained) * 100, 2)
        missed_chest_rate = round((number_of_chests_missed / (number_of_chests_obtained + number_of_chests_missed) * 100), 2)
        average_time_per_drop = round(total_time / number_of_drops, 2)

        # fmt: off
        print(f"\nNumber of Runs: {number_of_runs}"
            f"\nNumber of Chests Obtained: {number_of_chests_obtained}"
            f"\nNumber of Drops: {number_of_drops}"
            f"\nNumber of Missed Chests: {number_of_chests_missed}"
            f"\nDrop Rate: {drop_rate}%"
            f"\nMissed Chest Rate: {missed_chest_rate}%"
            f"\nAverage Chests Per Run: {average_chests_per_run}"
            f"\nAverage Time Taken For One Chest: {average_time_taken_for_one_chest}"
            f"\nAverage Time Per Drop: {average_time_per_drop}"
            f"\nNumber of Missed The Landing Relaunch: {relaunch.number_of_missed_the_landing_relaunch}"
            f"\nNumber of Missed The Pale Heart Relaunch: {relaunch.number_of_missed_the_pale_heart_relaunch}")
        # fmt: on

        print("Missed Chests: ", missed_chests)

    except ZeroDivisionError:
        pass
