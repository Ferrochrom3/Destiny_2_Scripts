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

    try:
        x, y = pyautogui.locateCenterOnScreen(os.path.join(image_path, "DIM Collect Postmaster.png"), confidence=0.7)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        keyboard.press_and_release("alt+tab")
    except TypeError:
        keyboard.press_and_release("alt+tab")
        print("DIM Collect Postmaster is not found")
