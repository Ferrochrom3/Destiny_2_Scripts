import pyautogui
import keyboard
import time

"""
Additional Note
 - Destiny 2 Desktop Icon.png is with the "4K SCI-Fi Black Hole" wallpaper.
 - Require Adminstrator access to simulate events on Task Manager.
 - Currently works with The Final Shape intro screen.
 - Hunter Human is using a specific emblem.
"""

image_path = "Destiny_2_Scripts\Other_Utilities\Broccoli_Error_Fix"


def is_broccoli_error():
    """Check if there's a Broccoli error window.

    Returns:
        boolean: Whether or not Broccoli error window is showing.
    """
    return bool(pyautogui.locateOnScreen(f"{image_path}\Broccoli Error.png", confidence=0.8))


def fix_broccoli_error():
    """
    Shut down Destiny 2 in Task Manger, launch back to the game's character selection screen, and select Hunter Human to get back to the game after Broccoli error.
    """
    print("Broccoli has occurred...Trying to fix it...")

    # Close Destiny 2 and open Task Manager
    keyboard.press_and_release("alt+f4")
    time.sleep(2)
    keyboard.press_and_release("ctrl+shift+esc")
    time.sleep(6)
    pyautogui.moveTo(1192, 400)
    time.sleep(0.2)
    pyautogui.leftClick()

    # Look for Destiny 2 icon in task manager
    print("Looking for Destiny 2 icon in Task Manager...")
    while not pyautogui.locateOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8):
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Memory.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(2)
        pyautogui.scroll(-1200)
        time.sleep(1)

    # After the loop, Desiny 2 icon will be found, so end the program
    print("Found Destiny 2 In Task Manager")
    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.leftClick()

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\End Task.png", confidence=0.8)
    print("End Task")
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.leftClick()

    # Close Task Manager and return to desktop
    keyboard.press_and_release("alt+f4")
    time.sleep(2)
    keyboard.press_and_release("win+d")

    print("Opening Destiny 2 on Desktop...")
    time.sleep(2)
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 Desktop Icon.png", grayscale=True, confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.5)
        pyautogui.click(x, y, clicks=3)
    except TypeError:
        pass

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
