import os
import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)

from Destiny_2_Scripts.Crucible.AFK_Silver_Leaves_Farm import resolution_config

"""
Location     : Crucible Private Match
Subclass     : Any
Abilities    : Any
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any
               Energy  - Any
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : Silver Leaves, Cruicible Reputation, Seasonal Weapons, Seasonal Engrams

Setup:
 - Set Private Match to "Collision" mode.
 - Change map to "The Burnout".
 - Change "Match Score Limit" to 25
 - Start the script after clicking on the "Launch" button.

Process:
 - After game starts, the character will run towards Zone B and captures the zone.
 - Points will slowly build up and after completion, 4-5 Silver Leaves will be rewarded.

 Additional Notes:
 - None
"""

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/Crucible/AFK_Silver_Leaves_Farm/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


start_time = time.time()


def my_function():
    global start_time
    start_time = time.time()

    while True:
        if pyautogui.locateOnScreen(os.path.join(image_path, "Zone B.png"), confidence=0.8):
            # Run towards Zone B
            print("Loaded in. Running towards Zone B")
            win32api_move_mouse(-100, 0)
            run_forward(4)
            win32api_move_mouse(1600, 0)
            run_forward(2.4)

            # Wait until game finishes
            print("Waiting for game completion")
            while True:
                if pyautogui.locateCenterOnScreen(os.path.join(image_path, "Crucible Icon.png"), confidence=0.8):
                    keyboard.press("o")
                    time.sleep(3.5)
                    keyboard.release("o")
                    break

            # Click "Launch" after exiting
            print("Waiting to return to orbit")
            while True:
                if pyautogui.locateOnScreen(os.path.join(image_path, "Collision.png"), confidence=0.7, region=config["gamemode_region"]):
                    pyautogui.moveTo(config["launch_button_coord"][0], config["launch_button_coord"][1])
                    time.sleep(0.1)
                    pyautogui.leftClick()
                    break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def run_forward(running_duration: float, wait_time: float = 0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def start_afk():
    afk_thread = threading.Thread(target=my_function)
    afk_thread.start()
    print("Execution Started")


print("Press F7 to Start")
print("Press F8 to Exit\n")

while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
