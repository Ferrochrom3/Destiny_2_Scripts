import os
import sys
import time
import keyboard
import pyautogui

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import efficiency_evaluation
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/Image_{current_monitor_resolution}"


def collect_loot():

    time.sleep(0.5)

    if pyautogui.locateOnScreen(f"{image_path}/Alt Button.png", confidence=0.8, region=config["chest_collection_region"]):
        efficiency_evaluation.number_of_chests_obtained += 1
        keyboard.press("alt")
        time.sleep(1.5)
        keyboard.release("alt")
    else:
        efficiency_evaluation.number_of_missed_chest += 1
