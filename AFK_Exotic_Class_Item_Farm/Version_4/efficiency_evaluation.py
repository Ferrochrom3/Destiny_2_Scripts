import time
import relaunch

number_of_runs = 0
number_of_chests_obtained = 0
number_of_missed_chest = 0


def display_status(start_time: float):
    """
    Shows the following metrics related to chest collection:
    1. Number of Runs: The total number of runs.
    2. Number of Chests Obtained: The total number of chests opened.
    3. Number of Missed Chests: The number of chests missed when trying to open a chest (could due to various reasons).
    4. Average Chests Per Run: On average, how many chests obtained for each run.
    5. Average Time Taken For One Chest: On average, how long does it take to get one chest.
    6. Number of Missed The Landing Relaunch: The amout of times the mouse cursor did not move to the landing zone correctly when relaunching The Landing.
    7. Number of Missed The Pale Heart Relaunch: The amount of times the mouse cursor did not move to the landing zone correctly when relaunching The Pale Heart.

    Args:
        start_time (float): The time when the script started.
    """

    total_time = time.time() - start_time
    average_chests_per_run = number_of_chests_obtained / number_of_runs
    average_time_taken_for_one_chest = total_time / number_of_chests_obtained

    # fmt: off
    print(f"\nNumber of Runs: {number_of_runs}"
          f"\nNumber of Chests Obtained: {number_of_chests_obtained}"
          f"\nNumber of Missed Chests: {number_of_missed_chest}"
          f"\nAverage Chests Per Run: {average_chests_per_run}"
          f"\nAverage Time Taken For One Chest: {average_time_taken_for_one_chest}"
          f"\nNumber of Missed The Landing Relaunch: {relaunch.number_of_missed_the_landing_relaunch}"
          f"\nNumber of Missed The Pale Heart Relaunch: {relaunch.number_of_missed_the_pale_heart_relaunch}")
    # fmt: on
