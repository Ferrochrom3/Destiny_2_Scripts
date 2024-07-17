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
Weapons      : Kinetic - Any
               Energy  - Indebted Kindness
               Power   - Parasite
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : World Drops, XP

Additional Notes
 - Must be on Strand using Grapple Grenade.
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

start_time = time.time()
image_path = "Destiny 2 Scripts/Investigation Mission/AFK Parasite Kills Farm"


def my_function():
    while True:
        wait_until_respawn()

        # Move left
        keyboard.press("a")
        time.sleep(0.4)
        keyboard.release("a")

        # Sprint forward
        keyboard.press("shift+w")
        time.sleep(2.6)
        keyboard.release("shift+w")

        # Place down rally banner
        keyboard.press("alt")
        time.sleep(1.1)
        keyboard.release("alt")
        time.sleep(2.2)

        # Sprint forward
        keyboard.press("left shift+w")
        time.sleep(3.2)
        keyboard.release("left shift+w")

        # Look up and shoot parasite
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -900, 0, 0)
        time.sleep(0.2)
        for _ in range(3):
            pyautogui.leftClick()
            time.sleep(0.2)
            keyboard.press_and_release("r")
            time.sleep(3.5)

        # Suicide
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 4000, 0, 0)
        time.sleep(0.3)
        pyautogui.leftClick()  # Shoot Parasite
        time.sleep(0.2)
        keyboard.press_and_release("2")  # Swap to Indebted Kindness
        time.sleep(0.8)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()


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
    keyboard.release("shift")
    keyboard.release("w")
    keyboard.release("s")
    keyboard.release("ctrl")

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
