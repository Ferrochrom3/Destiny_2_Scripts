import sys
import time
import keyboard
import pyautogui
import win32api
import win32con

sys.path.insert(0, "D:\\Visual Studio Code Projects\\")
from Destiny_2_Scripts.Other_Utilities.Broccoli_Error_Fix.broccoli_error_fix import is_broccoli_error
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error

image_path = "Destiny_2_Scripts/The_Invesigation/AFK_World_Drop_Farm"


def return_to_mission():
    print("Returning to the mission")
    keyboard.press_and_release("m")
    time.sleep(1.5)

    # If opening map shows Savathun's Throne World already, no need to hit "d"
    # This allows returning to mission from both Broccoli error and after collecting loot at HELM
    if not pyautogui.locateOnScreen(f"{image_path}/Throne World.png", confidence=0.8):
        keyboard.press_and_release("d")
        time.sleep(1.5)

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Throne World.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1.5)

    # Select normal campaign difficulty
    turn_camera(500, 0)
    turn_camera(0, 500)
    time.sleep(0.5)
    turn_camera(0, -500)
    select_campaign_mission()

    # Run towards enemy spawning area and suicide to get ready
    run_towards_suicide_zone()


def select_campaign_mission():
    x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Normal Campaign Icon.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1.5)

    # Click on mission
    pyautogui.moveTo(2077, 1107)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on "The Investigation" mission
    pyautogui.moveTo(392, 456)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on launch
    pyautogui.moveTo(2163, 1210)
    time.sleep(0.3)
    pyautogui.leftClick()

    # Wait until spawned in and don't let errors hold the loop forever
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Grapple Grenade.png", confidence=0.9) or is_broccoli_error() or is_internet_error():
            break


def run_towards_suicide_zone():
    # Run towards the gate
    turn_camera(100, 0)
    keyboard.press("shift+w")
    time.sleep(7)
    keyboard.release("shift+w")

    # Run pass the gate
    turn_camera(-480, 0)
    keyboard.press("shift+w")
    time.sleep(7.5)
    keyboard.release("shift+w")

    # Run down the slope
    turn_camera(640, 0)
    keyboard.press("shift+w")
    time.sleep(15)
    keyboard.release("shift+w")

    # Run down the ramp
    turn_camera(-850, 0)
    keyboard.press("shift+w")
    time.sleep(5)
    keyboard.release("shift+w")

    # Run towards suicide zone
    turn_camera(400, 0)
    keyboard.press("shift+w")
    time.sleep(3)
    turn_camera(400, 0)
    time.sleep(5)
    keyboard.release("shift+w")

    # Swap to Indebted Kindness to suicide
    keyboard.press_and_release("2")
    turn_camera(0, 3000)
    time.sleep(1)
    for _ in range(4):
        pyautogui.leftClick()
        time.sleep(0.5)

    # Wait until respawn and don't let errors hold the loop forever
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Grapple Grenade.png", confidence=0.8) or is_broccoli_error() or is_internet_error():
            time.sleep(0.5)
            break


def turn_camera(x: int, y: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(0.1)
