"""
Performance (out of 505.99 minutes):
Number of Attempts: 2025
Number of Chests Obtained: 355
Rate of Success: 17.53%
Average Time Per Success: 85.52s
"""

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
               Energy  - Ergo Sum (Waveframe)
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : T1 Mobility
Reward       : Exotic Class Items, Pale Heart Engrams, Ghost Reputations, Gunsmith Engrams
"""

print("Press F7 to Start")
print("Press F8 to End\n")

start_time = time.time()
image_path = "Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_2"

collect_loot_attempts = 0
number_of_chests_obtained = 0
number_of_relaunching = 0
max_number_of_relaunching = 15


def my_function():
    global number_of_relaunching  # pylint: disable=w0603

    while True:
        # Redo relaunching due to mouse cursor did not move to landing zone correctly
        if pyautogui.locateOnScreen(f"{image_path}/Pathfinder Icon.png", confidence=0.8):
            print("Mouse cursor did not move to landing zone correctly...")
            keyboard.press_and_release("m")
            time.sleep(1)
            relaunch_the_landing()

        # Reentering the map when relaunching is over max_number_of_relaunching
        elif pyautogui.locateOnScreen(f"{image_path}/Strand Barricade.png", confidence=0.9) and number_of_relaunching >= max_number_of_relaunching:
            number_of_relaunching = 0
            reset()

        elif pyautogui.locateOnScreen(f"{image_path}/Strand Barricade.png", confidence=0.9):
            time.sleep(30)
            keyboard.press_and_release("1")

            # First chest
            turn_camera(-800, 0)
            run_forward(4)
            single_key_press("a", 0.3)  # 0.3s for T1 mob | 0.27 for T9 mob
            run_forward(4.5)
            turn_camera(-2000, 0)
            run_forward(0.7)
            collect_loot()

            # Second chest
            turn_camera(2850, 0)
            run_forward(5.5)
            turn_camera(-2500, 0)
            run_forward(2.8)
            collect_loot()

            # Third chest
            turn_camera(-2730, 0)
            # use_ergo_sum()  # Change to 5s rather than 4.3s on the next line if use Ergo Sum
            run_forward(5)
            turn_camera(200, 0)
            run_forward(6.3)
            keyboard.press_and_release("1")
            turn_camera(-1330, 0)
            run_forward(4.7)
            turn_camera(-1700, 0)
            collect_loot()

            # Fourth Chest
            turn_camera(-2500, 0)
            run_forward(2.5)
            turn_camera(-2000, 0)
            run_forward(1)
            turn_camera(-1500, 0)
            # use_ergo_sum() # Change to 2.6s on the next line if use Ergo Sum
            run_forward(3.1)
            turn_camera(-2000, 0)
            run_forward(3.5)
            collect_loot()

            # Fifth chest
            keyboard.press_and_release("1")
            turn_camera(3800, 0)
            run_forward(3)
            turn_camera(-2100, 0)
            run_forward(1.3)
            turn_camera(2100, 0)
            run_forward(1)
            collect_loot()

            # Sixth chest
            turn_camera(-2500, 0)
            run_forward(3.5)
            turn_camera(-1300, 0)
            run_forward(2)
            use_ergo_sum()
            run_forward(3)
            turn_camera(1500, 0)
            run_forward(0.3)
            collect_loot()

            # Seventh chest
            turn_camera(1000, 0)
            use_ergo_sum()
            run_forward(3.9)
            keyboard.press_and_release("1")
            turn_camera(-1000, 0)
            collect_loot()

            # Eighth chest
            turn_camera(-2500, 0)
            run_forward(2.3)
            turn_camera(1500, 0)
            run_forward(3.3)
            collect_loot()

            # Ninth chest
            turn_camera(-950, 0)
            run_forward(4.7)
            turn_camera(2000, 0)
            run_forward(1.65)
            turn_camera(-100, 300)
            collect_loot()

            relaunch_the_landing()


def turn_camera(x, y, wait_time=0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def run_forward(running_duration, wait_time=0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def single_key_press(key, duration, wait_time=0.1):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
    time.sleep(wait_time)


def use_ergo_sum():
    keyboard.press_and_release("2")
    time.sleep(0.8)
    pyautogui.click(button="right")
    time.sleep(1.5)


def reset():
    keyboard.press_and_release("tab")
    time.sleep(1.5)
    keyboard.press_and_release("o")
    time.sleep(0.3)
    keyboard.press("o")
    time.sleep(3)
    keyboard.release("0")

    print("Waiting to Open Director")
    launch_into_the_pale_heart()


def launch_into_the_pale_heart():
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Open Director.png", confidence=0.8):
            keyboard.press_and_release("m")
            time.sleep(1)
            break

    print("Waiting to Open The Pale Heart Destination")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/The Pale Heart.png", confidence=0.8):
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}/The Pale Heart.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            break

    print("Waiting For Destination Map to Open")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Legendary Campaign Icon.png", confidence=0.8):
            time.sleep(0.2)

            # Move to The Landing
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1200, 0, 0, 0)
            time.sleep(2.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 675, 0, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 35, 0, 0)
            time.sleep(0.2)
            pyautogui.leftClick()
            time.sleep(1)

            # Click on Launch
            pyautogui.moveTo(2160, 1196)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
            break


def relaunch_the_landing():
    global number_of_relaunching  # pylint: disable=w0603

    print("Relaunching...")
    number_of_relaunching += 1
    keyboard.press_and_release("m")

    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Legendary Campaign Icon.png", confidence=0.8) or pyautogui.locateOnScreen(f"{image_path}/Campaign Mission Icon.png", confidence=0.8):
            time.sleep(0.2)
            break

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1200, 0, 0, 0)
    time.sleep(2.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 680, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 10, -30, 0, 0)
    time.sleep(0.2)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.mouseDown(button="left")
    time.sleep(1.3)
    pyautogui.mouseUp(button="left")
    time.sleep(1)


def collect_loot():
    global collect_loot_attempts  # pylint: disable=w0603
    global number_of_chests_obtained  # pylint: disable=w0603

    collect_loot_attempts += 1
    time.sleep(0.5)

    if pyautogui.locateOnScreen(f"{image_path}/Alt Button.png", confidence=0.8, region=(1112, 896, 400, 160)):
        number_of_chests_obtained += 1
        keyboard.press("alt")
        time.sleep(1.5)
        keyboard.release("alt")


def display_status():
    rate_of_success = round((number_of_chests_obtained / collect_loot_attempts) * 100, 2)
    average_time_per_success = round(time.time() - start_time) / number_of_chests_obtained

    # fmt: off
    print(f"Number of Attempts: {collect_loot_attempts}"
          f"\nNumber of Chests Obtained: {number_of_chests_obtained}"
          f"\nRate of Success: {rate_of_success}%"
          f"\nAverage Time Per Success: {average_time_per_success}s")
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
    keyboard.release("o")
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
