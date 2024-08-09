import os
import sys
import time
import pyautogui
import win32api
import win32con

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)

from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import status_display
from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    base_path = os.path.dirname(__file__)


image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def launch_shattered_throne():
    """
    Launch The Shattered Throne dungeon from orbit from the planets page.
     - Click on Dreaming City
     - Move up to click the dungeon icon, then launch
    """

    status_display.current_status = "Launch The Shattered Throne"

    # Try to click on Dreaming City
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(os.path.join(image_path, "Dreaming City.png"), confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            win32api_move_mouse(-600, 0)  # Move mouse towards center after clicking to avoid moving to map
            time.sleep(2)
            break
        except TypeError:
            pass

    win32api_move_mouse(config["dreaming_city_move_up"][0], config["dreaming_city_move_up"][1])
    time.sleep(0.5)
    win32api_move_mouse(config["dreaming_city_move_down"][0], config["dreaming_city_move_down"][1])

    # Try click on dungeon
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(os.path.join(image_path, "Dungeon Icon.png"), confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
            pyautogui.moveTo(config["launch_button"][0], config["launch_button"][1])
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        except TypeError:
            pass
