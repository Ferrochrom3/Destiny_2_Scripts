"""
Require:
 - opencv-python
 - Pillow
 - PyScreeze version=0.1.27
 - PyAutoGUI version=0.9.50
    - PyAutoGui newer versions doesn't allow image checks by using if pyautogui.locateOnScreen() when image is not present on screen, it will throw an exception.


print(pyautogui.position())                                       Print current mouse cursor location
time.sleep(x)                                                     Delay x seconds

pyautogui.click()                                                 Click (x, y)
pyautogui.click(clicks=3, interval=0.1)                           Click once every 0.1 seconds for 3 times
pyautogui.mouseDown(button='left')                                Hold down left mouse button
pyautogui.mouseUp(button='left')                                  Release left mouse button
pyautogui.moveTo(x, y, duration=1)                                Move mouse to (x, y) taking a total of 1 second
pyautogui.moveRel(100, 100, duration=1)                           Move mouse by (x, y) from the current position taking a total of 1 second

pyautogui.press()                                                 Press a key like 'a'
pyautogui.keyDown('ctrl')                                         Hold down ctrl
pyautogui.keyUp('ctrl')                                           Release ctrl

keyboard.is_pressed('a')                                          Check if 'a' is pressed
keyboard.press('a')                                               Hold down 'a'
keyboard.release('a')                                             Release 'a'
keyboard.press_and_release('a')           

Controller().click(Button.x1)                                     Click mouse button 4 (x2 is 5)

pyautogui.FAILSAFE = False                                        Remove mouse movement restrictions

region = (x, y, w, h)                                             (x-coord of the top-left corner, y-coord of the top-left corner, Width of the region, Height of the region)

Scripts that uses multiple versions that has the same .py file in each version, such as resolution_config.py must import their own scripts with a path
Ex. from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import resolution_config

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")                                                               Get the absolute path of "Destiny_2_Scripts"
folder_path = os.path.dirname(destiny_2_scripts_path)                                                                       Get the path of the folder that contains "Destiny_2_Scripts"
sys.path.insert(0, folder_path)                                                                                             Insert the folder that contains "Destiny_2_Scripts" to system path so any scripts in "Destiny_2_Scripts" can be imported
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error, fix_internet_error   Dynamically inserts the path needed to get to "Destiny_2_Scripts" so any scripts in Destiny_2_Scripts can be imported like this
from *some path to a folder* import resolution_config                                                                       Cannot just do "import resolution_config" when resolution_config.py is imported in another script
                                                                                                                            where that other script also uses a resolution_config.py file that is different

if getattr(sys, "frozen", False):                                                                                           Determine if the script is running as a bundled executable
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"                                   The path from "Destiny_2_Scripts" to the files that this code is used in
else:                                                                                                                       
    base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")                                                 Join the base path and the image path

"""

import os
import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style
from pynput.mouse import Button, Controller

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

# Get current monitor resolution, used to make script compatible with multiple resolutions
screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"

# Determine based image path depending on if the script is running as a bundled executable or in development (such as VS code)
if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


# Variables
start_time = time.time()


# Main AFK function
def my_function():
    global start_time
    start_time = time.time()

    while True:
        print(pyautogui.mouseInfo())
        break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    """
    Use win32api library to move mouse position to by an (x, y) off set. +x moves to the right and +y moves down.\n
    Ex. (100, 100) moves the mouse 100 pixels to the right and 100 pixels down relative to current mouse position.

    Args:
        x (int): Move mouse by some x offset (+x moves to the right, -x moves to the left).
        y (int): Move mouse by some y offset (+y moves down, -y moves up).
        wait_time (float, optional): Wait some time (in seconds) after mouse movement to allow the mouse to properly move to position before further inputs or to move some offset and wait some time at the new position. Defaults to 0.1.
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def start_afk():
    afk_thread = threading.Thread(target=my_function)
    afk_thread.start()
    print("Execution Started")


print("Testing")
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
