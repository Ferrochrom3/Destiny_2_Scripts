import os
import sys
import time
import keyboard
import pyautogui
import resolution_config

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.Dungeon.AFK_Warlords_Ruin_First_Boss_Farm import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/Dungeon/AFK_Warlords_Ruin_First_Boss_Farm/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


def collect_loot_from_DIM():
    keyboard.press_and_release("alt+tab")
    time.sleep(1)

    # Refresh DIM
    pyautogui.moveTo(config["DIM_refresh_area"][0], config["DIM_refresh_area"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    keyboard.press_and_release("r")
    time.sleep(5)

    # Collect loot
    pyautogui.moveTo(config["DIM_console_area"][0], config["DIM_console_area"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    keyboard.write('document.querySelector(".dim-button").click()')
    time.sleep(0.1)
    keyboard.press_and_release("enter")
    time.sleep(0.3)

    keyboard.press_and_release("alt+tab")
