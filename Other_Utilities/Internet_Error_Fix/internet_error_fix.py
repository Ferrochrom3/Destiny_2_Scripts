import time
import pyautogui
import keyboard

image_path = "Destiny_2_Scripts/Other_Utilities/Internet Error Fix"


def is_internet_error():
    return bool(pyautogui.locateOnScreen(f"{image_path}/Error Code Icon.png", confidence=0.8))


def fix_internet_error():
    print("Internet error has occured...Trying to fix it...")

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
