import pyautogui
import keyboard
import time

"""
Additional Note
 - Destiny 2 Desktop Icon.png is with the "4K SCI-Fi Black Hole" wallpaper
"""
image_path = "Destiny 2 Scripts/Other Utilities/Broccoli Error Fix"


def check_and_fix_broccoli_error():
    """
    Check if there's a Broccoli Error window. \n
    If window is found, continue to shut down Destiny 2 in Task Manger, launch back to the game's character selection screen, and select Hunter Human.
    """
    if is_broccoli_error():
        fix_broccoli_error()


def is_broccoli_error():
    return bool(pyautogui.locateOnScreen(f"{image_path}\Broccoli Error.png", confidence=0.8))


def fix_broccoli_error():
    print("Broccoli has occurred...")

    # Close Destiny 2 and open Task Manager
    keyboard.press_and_release("alt+f4")
    time.sleep(2)
    keyboard.press_and_release("ctrl+shift+esc")
    time.sleep(6)

    # Look for Destiny 2 icon in task manager
    print("Looking for Destiny 2 icon in Task Manager...")
    while not pyautogui.locateOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8):
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Memory.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(2)
        pyautogui.scroll(-1200)
        time.sleep(1)

    # After the loop, Desiny 2 icon will be found, so end the program
    end_destiny2()

    # Close Task Manager and return to desktop
    keyboard.press_and_release("alt+f4")
    time.sleep(2)
    keyboard.press_and_release("win+d")

    print("Open Destiny 2 on Desktop")
    time.sleep(2)
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 Desktop Icon.png", grayscale=True, confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.5)
        pyautogui.click(x, y, clicks=3)
    except TypeError:
        pass

    # Wait 60 seconds and hit space to go into character selection screen
    time.sleep(60)
    keyboard.press_and_release("space")

    print("Click on Hunter Human")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Hunter Human.png", confidence=0.8):
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Hunter Human.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(4)


def end_destiny2():
    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8)
    print("Found Destiny 2 In Task Manager")
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\End Task.png", confidence=0.8)
    print("End Task")
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()
