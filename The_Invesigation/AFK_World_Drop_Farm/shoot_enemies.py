import sys
import time
import keyboard
import pyautogui
import win32api
import win32con

sys.path.insert(0, "D:\\Visual Studio Code Projects\\")
from Destiny_2_Scripts.Other_Utilities.Broccoli_Error_Fix.broccoli_error_fix import is_error

image_path = "Destiny_2_Scripts/The_Invesigation/AFK_World_Drop_Farm"


def shoot_enemy():
    keyboard.press_and_release("3")  # Swap to Power weapon

    keyboard.press("a")  # Move left
    time.sleep(0.4)
    keyboard.release("a")

    keyboard.press("shift+w")  # Sprint forward
    time.sleep(2.6)
    keyboard.release("shift+w")

    keyboard.press("alt")  # Place down Rally Banner
    time.sleep(1.1)
    keyboard.release("alt")
    time.sleep(2.2)

    keyboard.press("shift+w")  # Run down the ramp to spawn more enemies
    time.sleep(5)
    keyboard.release("shift+w")

    # Aim and shoot Gjallarhorn
    pyautogui.mouseDown(button="right")
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 110, 60, 0, 0)
    time.sleep(1.2)
    pyautogui.leftClick()
    pyautogui.mouseUp(button="right")

    # Reload and shoot again
    keyboard.press_and_release("r")
    time.sleep(2.5)
    pyautogui.mouseDown(button="right")
    time.sleep(0.5)
    pyautogui.leftClick()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 200, 0, 0)
    time.sleep(1.2)
    pyautogui.leftClick()
    pyautogui.mouseUp(button="right")

    # Swap to Indebted Kindness, look all the way down and suicide
    keyboard.press_and_release("2")
    time.sleep(0.8)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 3000, 0, 0)
    time.sleep(0.2)

    for _ in range(4):
        pyautogui.leftClick()
        time.sleep(0.5)

    # Wait until respawn
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Grapple Grenade.png", confidence=0.8) or is_error():
            time.sleep(0.5)
            break
