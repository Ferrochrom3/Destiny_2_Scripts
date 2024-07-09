import time
import pyautogui
import keyboard
import resolution_config

"""
Additional Note
 - Currently works with The Final Shape intro screen.
"""

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/Other_Utilities/Internet_Error_Fix/Image_{current_monitor_resolution}"


def is_internet_error():
    """Check if an internet error code has occured or if the player is in the intro screen.

    Returns:
        boolean: Whether or not an error code has occured.
    """

    # Error may occur during execution, which takes you to the intro screen when checking for error code screen hit, add intro screen check to get out of the loop if that happens.
    if pyautogui.locateOnScreen(f"{image_path}/Error Code Icon.png", confidence=0.8) or pyautogui.locateOnScreen(f"{image_path}/The Final Shape.png", confidence=0.8):
        return True

    return False


def fix_internet_error(character_order: str):
    """
    Exit the error code screen (which takes you to the main intro screen) and continue to character selection screen and click Hunter Human.

    Args:
        character_order (str): From top to bottom, the character to select (first, second, or third)
    """
    print("Internet error has occured...Trying to fix it...")
    if pyautogui.locateOnScreen(f"{image_path}/Error Code Icon.png", confidence=0.8):
        keyboard.press_and_release("space")

    print("Waiting for The Final Shape Screen...")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\The Final Shape.png", confidence=0.8):
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\The Final Shape.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.2)
            pyautogui.leftClick()
            time.sleep(0.2)
            keyboard.press_and_release("space")
            break

    print("Waiting to click on a character...")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Patch Notes Icon.png", confidence=0.8, region=config["patch_notes_icon_region"]):
            time.sleep(0.3)
            pyautogui.moveTo(config[f"{character_order}_character_coord"][0], config[f"{character_order}_character_coord"][1])
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(6)  # Wait 6 seconds until in game
            break


fix_internet_error("first")
