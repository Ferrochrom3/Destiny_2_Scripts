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

"""
Location     : Any
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
Reward       : Any

Setup:
 - Any
 
Process:
 - Any

Additional Notes:
 - Any
"""

if getattr(sys, "frozen", False):
    image_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    image_path = os.path.dirname(__file__)


start_time = time.time()


def my_function():
    global start_time
    start_time = time.time()

    while True:
        break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
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
