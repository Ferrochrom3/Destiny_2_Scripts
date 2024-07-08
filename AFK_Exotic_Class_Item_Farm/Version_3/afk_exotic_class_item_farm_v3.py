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
from efficiency_evaluation import display_status

"""
Location     : The Pale Heart
Subclass     : Depends on "Abilities"
Abilities    : *Check "Additional Notes"
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any Non-Lightweight weapon
               Energy  - Still Hunt
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : Exotic Class Items, Pale Heart Engrams, Ghost Reputations, Gunsmith Engrams

Additional Notes:
 - Must plant the Luminescent Seed by the chest.
 - Chest spawn is manipulated by standing at a specific spot before other chests have spawned. Must execute the script shortly after landing.
 - Must equip Wombo Detector Ghost mod.
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

start_time = time.time()
image_path = f"Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_3/Image_{current_monitor_resolution}"


def my_function():
    while True:
        # Relaunch the landing if mouse cursor did not move to landing zone correctly
        if pyautogui.locateOnScreen(f"{image_path}/Pathfinder Icon.png", confidence=0.8):
            print("Cursor did not move to landing zone correctly...Retrying...")
            keyboard.press_and_release("m")
            time.sleep(1)
            relaunch.relaunch_the_landing()

        # Relaunch into the Pale Heart before Overthrow level reaches 2
        elif pyautogui.locateOnScreen(f"{image_path}/Overthrow The Landing Icon.png", confidence=0.9) and relaunch.number_of_relaunching >= relaunch.max_number_of_relaunching:
            time.sleep(0.5)
            relaunch.number_of_relaunching = 0
            relaunch.relaunch_into_the_pale_heart()

        # Try to collect chest and relaunch The Landing after collecting loot
        elif pyautogui.locateOnScreen(f"{image_path}/Overthrow The Landing Icon.png", confidence=0.9):
            time.sleep(0.5)
            collect_loot.collect_loot_attempts += 1

            # Run to corner
            keyboard.press_and_release("1")
            win32api_move_mouse(-800, 0)
            run_forward(3.5)
            win32api_move_mouse(200, 0)
            run_forward(3.5)
            win32api_move_mouse(2600, 0)

            # Swap to Still Hunter and check for chest spawn
            keyboard.press_and_release("2")
            time.sleep(1)
            pyautogui.mouseDown(button="right")

            elapsed_time = time.time()
            while True:
                if pyautogui.locateOnScreen(f"{image_path}/Chest Icon.png", confidence=0.8, region=config["chest_detection_region"]):
                    print("Chest found, running towards chest")
                    pyautogui.mouseUp(button="right")
                    run_forward(2)
                    win32api_move_mouse(700, 0)
                    run_forward(3)
                    win32api_move_mouse(-1200, 0)
                    run_forward(5)
                    win32api_move_mouse(-1770, 220)
                    collect_loot.collect_loot()
                    break

                if time.time() - elapsed_time >= 40:
                    print("Over 40s...Chest Not Found...")
                    pyautogui.mouseUp(button="right")
                    break

            relaunch.relaunch_the_landing()


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def run_forward(running_duration: float, wait_time: float = 0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("shift+w")
    pyautogui.mouseUp(button="right")
    display_status(start_time)

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
