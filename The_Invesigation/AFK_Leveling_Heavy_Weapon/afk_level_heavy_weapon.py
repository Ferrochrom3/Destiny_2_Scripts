import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style

"""
Location     : "The Investigation" - Witch Queen Campaign - 2nd Mission
Subclass     : Any
Abilities    : Any
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Mountain Top
               Energy  - Any
               Power   - Any weapon to level up, Eyes of Tomorrow
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : World Drops, XP
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

pyautogui.FAILSAFE = False
start_time = time.time()

image_path = "Destiny 2 Scripts\Investigation Mission\AFK Leveling Heavy Weapon"


def my_function():
    while True:
        wait_until_respawn()

        keyboard.press("a")  # Move left
        time.sleep(0.5)
        keyboard.release("a")

        keyboard.press("shift+w")  # Sprint forward
        time.sleep(2.6)
        keyboard.release("shift+w")

        keyboard.press("alt")  # Place down Rally Banner
        time.sleep(1.1)
        keyboard.release("alt")
        time.sleep(2.2)

        keyboard.press("w")  # Walk forward slightly
        time.sleep(0.3)
        keyboard.release("w")

        keyboard.press_and_release("r")  # Reload
        time.sleep(2.3)

        # Aim eyes of tomorrow at enemies
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 100, 0, 0)
        pyautogui.mouseDown(button="right")
        time.sleep(1)

        # Look all the way up and shoot
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1000, 0, 0)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.mouseUp(button="right")

        # Open inventory and swap to first weapon on the left in the heavy slot
        keyboard.press_and_release("f1")
        time.sleep(1)
        pyautogui.moveTo(699, 847)  # Heavy slot
        time.sleep(0.2)
        pyautogui.moveTo(555, 845)  # First weapon to the left of the heavy slot
        pyautogui.leftClick()
        time.sleep(0.1)
        keyboard.press_and_release("f1")
        time.sleep(2)

        # Swap to Indebted Kindness, look all the way down and suicide
        keyboard.press_and_release("2")
        time.sleep(0.8)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 3000, 0, 0)
        time.sleep(0.2)

        for _ in range(4):
            pyautogui.leftClick()  # shoot
            time.sleep(0.5)

        # Open inventory and swap back to Eyes of Tomorrow
        keyboard.press_and_release("f1")  # open inventory
        time.sleep(1.5)
        pyautogui.moveTo(699, 847)  # Heavy slot
        time.sleep(0.2)
        pyautogui.moveTo(555, 845)  # First weapon to the left of the heavy slot
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        keyboard.press_and_release("f1")


def wait_until_respawn():
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Grapple Grenade.png", confidence=0.8):
            time.sleep(1)
            keyboard.press_and_release("3")
            break


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("a")
    keyboard.release("shift+w")
    keyboard.release("alt")

    sys.exit(
        f"{Fore.RED}\
            {round(time.time() - start_time)} seconds \
            | {round((time.time() - start_time) / 60, 2)} minutes \
            | {round((time.time() - start_time) / 3600, 2)} hours {Style.RESET_ALL}"
    )
