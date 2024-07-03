import time
import pyautogui
import keyboard

"""
Additional Note
 - Currently works with The Final Shape intro screen.
 - Hunter Human is using a specific emblem.
"""

image_path = "Destiny_2_Scripts/Other_Utilities/Internet_Error_Fix"


def is_internet_error():
    """Check if an internet error code has occured or if the player is in the intro screen.

    Returns:
        boolean: Whether or not an error code has occured.
    """

    # Error may occur during execution, which takes you to the intro screen when checking for error code screen hit, add intro screen check to get out of the loop if that happens.
    if pyautogui.locateOnScreen(f"{image_path}/Error Code Icon.png", confidence=0.8) or pyautogui.locateOnScreen(f"{image_path}/The Final Shape.png", confidence=0.8):
        return True

    return False


def fix_internet_error():
    """
    Exit the error code screen (which takes you to the main intro screen) and continue to character selection screen and click Hunter Human.
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

    print("Waiting to click on Hunter Human...")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Hunter Human.png", confidence=0.8):
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Hunter Human.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(6)  # Wait 6 seconds until in game
            break
