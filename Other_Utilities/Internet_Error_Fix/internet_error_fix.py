import os
import sys
import time
import pyautogui
import keyboard

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix import error_resolution_config

"""
Additional Note
 - Currently works with The Final Shape intro screen.
 - Any other pop up screen will stop this from reloading into the game properly.
"""

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = error_resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/Other_Utilities/Internet_Error_Fix/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


def is_internet_error():
    """Check if an internet error code has occured or if the player is in the intro screen (Currently uses The Final Shape intro screen).

    Returns:
        boolean: Whether or not an error code has occured.
    """

    # Error may occur during execution, which takes you to the intro screen when checking for error code screen hit, add intro screen check to get out of the loop if that happens.
    if (
        pyautogui.locateOnScreen(os.path.join(image_path, "Error Code Icon.png"), confidence=0.9)
        or pyautogui.locateOnScreen(os.path.join(image_path, "Attention Icon.png"), confidence=0.9)
        or pyautogui.locateOnScreen(os.path.join(image_path, "The Final Shape.png"), confidence=0.9)
    ):
        return True

    return False


def fix_internet_error(character_to_select: str):
    """
    Exit the error code screen (which takes you to the main intro screen) and continue to character selection screen and click Hunter Human.

    Args:
        character_to_select (str): From top to bottom, which character to select (First, Second, or Third). The characters will be converted to lower cases automatically.
    """

    character_to_select = character_to_select.lower()

    print("Internet error has occured...Trying to fix it...")
    if pyautogui.locateOnScreen(os.path.join(image_path, "Error Code Icon.png"), confidence=0.8) or pyautogui.locateOnScreen(f"{image_path}/Attention Icon.png", confidence=0.8):
        keyboard.press_and_release("space")

    print("Waiting for The Final Shape Screen...")
    while True:
        if pyautogui.locateOnScreen(os.path.join(image_path, "The Final Shape.png"), confidence=0.8):
            x, y = pyautogui.locateCenterOnScreen(os.path.join(image_path, "The Final Shape.png"), confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.2)
            pyautogui.leftClick()
            time.sleep(0.2)
            keyboard.press_and_release("space")
            break

        # If internet error occurs during this waiting period, redo the internet error fix
        if is_internet_error():
            print('Internet error occured again in "Waiting for The Final Shape Screen"...Redoing the fix...')
            fix_internet_error(character_to_select)
            return

    print("Waiting to click on a character...")
    while True:
        if pyautogui.locateOnScreen(os.path.join(image_path, "Patch Notes Icon.png"), confidence=0.8, region=config["patch_notes_icon_region"]):
            time.sleep(0.3)
            pyautogui.moveTo(config[f"{character_to_select}_character_coord"][0], config[f"{character_to_select}_character_coord"][1])
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(6)  # Wait 6 seconds until in game
            break

        # If internet error occurs during this waiting period, redo the internet error fix
        if is_internet_error():
            print('Internet error occured again in "Waiting to click on a character"...Redoing the fix...')
            fix_internet_error(character_to_select)
            return
