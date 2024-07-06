import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
import relaunch
import collect_loot
import resolution_config
from colorama import Fore, Style

"""
Location     : The Pale Heart
Subclass     : Strand Titan
Abilities    : Towering Barricade
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any Non-Lightweight weapon
               Energy  - Still Hunter
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : T1 Mobility
Reward       : Exotic Class Items, Pale Heart Engrams, Ghost Reputations, Gunsmith Engrams

Additional Notes:
 - Must plant the Luminescent Seed by the chest.
 - Chest spawn is manipulated by standing at a specific spot before other chests have spawned. Must execute the script shortly after landing.
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

start_time = time.time()
image_path = "Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_3"


def my_function():
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Strand Barricade.png", confidence=0.9) and relaunch.number_of_relaunching >= relaunch.max_number_of_relaunching:
            relaunch.number_of_relaunching = 0
            relaunch.relaunch_into_the_pale_heart()

        elif pyautogui.locateOnScreen(f"{image_path}/Strand Barricade.png", confidence=0.9):
            collect_loot.collect_loot_attempts += 1

            # Run to corner
            keyboard.press_and_release("1")
            turn_camera(-800, 0)
            run_forward(3.5)
            turn_camera(200, 0)
            run_forward(3.5)
            turn_camera(2600, 0)

            # Swap to Still Hunter and check for chest spawn
            keyboard.press_and_release("2")
            time.sleep(1)
            pyautogui.mouseDown(button="right")
            elapsed_time = time.time()
            while True:
                if pyautogui.locateOnScreen(f"{image_path}/Chest Icon.png", confidence=0.8, region=resolution_config.chest_detection_region):
                    print("Chest Found")
                    break
                if time.time() - elapsed_time >= 50:
                    print("Over 50s...Chest Not Found...")
                    break
            pyautogui.mouseUp(button="right")

            # Run towards chest
            run_forward(2)
            turn_camera(700, 0)
            run_forward(3)
            turn_camera(-1200, 0)
            run_forward(5)
            turn_camera(-1770, 220)

            collect_loot.collect_loot()
            relaunch.relaunch_the_landing()


def turn_camera(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def run_forward(running_duration: float, wait_time: float = 0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def display_status():
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


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("shift+w")
    pyautogui.mouseUp(button="right")
    display_status()

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
