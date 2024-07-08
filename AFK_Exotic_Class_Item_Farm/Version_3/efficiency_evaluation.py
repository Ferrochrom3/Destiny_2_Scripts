import time
import collect_loot


def display_status(start_time: float):
    """
    Shows the following metrics related to chest collection:
    1. Number of Attempts: The total number of times the character loads into The Landing and checks for chest spawn.
    2. Number of Chests Obtained: The total number of chests opened.
    3. Rate of Success: The % of chests obtained over number of attempts.
    4. Average Time Per Success: The average time, in seconds, for a chest to be collected.

    Args:
        start_time (float): The time when the script started.
    """
    rate_of_success = round((collect_loot.number_of_chests_obtained / collect_loot.collect_loot_attempts) * 100, 2)

    if collect_loot.number_of_chests_obtained > 0:
        average_time_per_success = round(time.time() - start_time) / collect_loot.number_of_chests_obtained
    else:
        average_time_per_success = "NAN"

    # fmt: off
    print(f"Number of Attempts: {collect_loot.collect_loot_attempts}"
          f"\nNumber of Chests Obtained: {collect_loot.number_of_chests_obtained}"
          f"\nRate of Success: {rate_of_success}%"
          f"\nAverage Time Per Success: {average_time_per_success}s")
    # fmt: on
