import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style

"""
Location     : The Pale Heart
Subclass     : Strand Titan
Abilities    : Towering Barricade
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any Non-Lightweight weapon
               Energy  - Still Hunt
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : T1 Mobility
Reward       : Exotic Class Items, Pale Heart Engrams, Ghost Reputations, Gunsmith Engrams

Additional Notes:
 - Work in progress for 1440p
"""

print("Press F7 to Start")
print("Press F8 to End\n")

start_time = time.time()

number_of_attempts = 0
number_of_chests_opened = 0
elapsed_waiting_time = 0


def my_function():
    global number_of_attempts  # pylint: disable=w0603

    while True:
        if pyautogui.locateOnScreen("Pathfinder Icon.png", confidence=0.8):
            keyboard.press_and_release("m")
            time.sleep(1)
            relaunch_the_landing()

        if pyautogui.locateOnScreen("Strand Barricade.png", confidence=0.9):
            number_of_attempts += 1

            # Swap to energy Sniper and scope in
            keyboard.press_and_release("2")
            time.sleep(0.5)
            pyautogui.mouseDown(button="right")

            elapsed_waiting_time = time.time()

            while True:
                if pyautogui.locateOnScreen("Chest Icon.png", confidence=0.8, region=(0, 559, 210, 180)):
                    print("Chest Icon Found")

                    # Unscope
                    time.sleep(0.1)
                    pyautogui.mouseUp(button="right")

                    run_towards_chest()
                    break

                elif time.time() - elapsed_waiting_time >= 50:
                    print("Chest Icon Not Found")

                    # Unscope
                    time.sleep(0.1)
                    pyautogui.mouseUp(button="right")
                    break

            relaunch_the_landing()


def relaunch_the_landing():
    print("Relaunching...")
    time.sleep(0.1)
    pyautogui.mouseUp(button="right")
    keyboard.press_and_release("m")

    while True:
        if pyautogui.locateOnScreen("Legendary Campaign Icon.png", confidence=0.8):
            time.sleep(0.2)
            break

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1000, 0, 0, 0)
    time.sleep(1.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 500, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, -30, 0, 0)
    pyautogui.mouseDown(button="left")
    time.sleep(1)
    pyautogui.mouseUp(button="left")
    time.sleep(1)


def run_towards_chest():
    global number_of_chests_opened  # pylint: disable=w0603

    # Turn and run forward
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -800, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press("a")
    time.sleep(0.3)
    keyboard.release("a")
    keyboard.press("shift+w")
    time.sleep(9.3)

    # Jump up (Titan)
    keyboard.press("space")  # Initial Jump
    time.sleep(0.1)
    keyboard.release("space")
    time.sleep(0.1)
    keyboard.press("space")  # Ability jump
    time.sleep(0.4)
    keyboard.release("space")
    time.sleep(0.1)
    keyboard.press("space")  # Deactivate ability jump
    time.sleep(0.1)
    keyboard.release("space")
    time.sleep(2.83)

    keyboard.release("shift+w")
    time.sleep(0.2)

    keyboard.press("a")
    time.sleep(0.24)
    keyboard.release("a")
    time.sleep(0.2)

    if pyautogui.locateOnScreen("Alt Button.png", confidence=0.8, region=(834, 705, 200, 80)):
        print("Alt Button Found")
        number_of_chests_opened += 1
        keyboard.press("alt")
        time.sleep(1.5)
        keyboard.release("alt")
    else:
        print("Alt Button Not Found")


def display_status():
    rate_of_success = round((number_of_chests_opened / number_of_attempts) * 100)
    average_time_per_success = round(time.time() - start_time) / number_of_chests_opened

    # fmt: off
    print(f"=====================" f"Number of Attempts: {number_of_attempts}"
          f"\nNumber of Chests Opened: {number_of_chests_opened}"
          f"\nRate of Success: {rate_of_success}%"
          f"\nAverage Time Per Success: {average_time_per_success}s"
          f"=====================")
    # fmt: on


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("shift+w")
    keyboard.release("alt")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    display_status()

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
