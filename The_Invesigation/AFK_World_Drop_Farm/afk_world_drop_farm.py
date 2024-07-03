import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style
from shoot_enemies import shoot_enemy
from helm_collect_loot import go_to_helm_and_collect_loot
from back_to_mission import return_to_mission

sys.path.insert(0, "D:\\Visual Studio Code Projects\\")
from Destiny_2_Scripts.Other_Utilities.Broccoli_Error_Fix.broccoli_error_fix import is_broccoli_error, fix_broccoli_error
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error, fix_internet_error


"""
Location     : "The Investigation" - Witch Queen Campaign - 2nd Mission
Subclass     : Any
Abilities    : Any
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any Non-Lightweight weapons
               Energy  - Indebted Kindness
               Power   - Gjallarhorn (with catalyst)
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Solar Reloader x1
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : T8 Mobility
Reward       : World Drops, XP

Additional Notes
 - Clear all items in inventory.
 - Gjallarhorn must have ammo loaded initially.
 - Must be using Grapple Grenade.
 - HELM structure and respawn are based on Episode: Echoes where Fail Safe is in the center of the old spawn.
 - Check broccoli_error_fix.py and internet_error_fix.py for more Additional Notes
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

pyautogui.FAILSAFE = False
start_time = time.time()


def my_function():
    while True:
        # Check if there's broccoli error. If so, fix the error and return to the mission
        if is_broccoli_error():
            fix_broccoli_error()
            return_to_mission()

        # Check if there's an internet error. If so, fix the error and return to the mission
        elif is_internet_error():
            fix_internet_error()
            return_to_mission()

        # If there are no errors, procced to shoot enemies
        else:
            print("Shooting Enemies")
            for _ in range(70):
                shoot_enemy()
                if is_broccoli_error() or is_internet_error():
                    break

            # After 70 iterations, go back to the HELM and collect and return back to the mission if there are no errors
            if not is_broccoli_error() and not is_internet_error():
                go_to_helm_and_collect_loot()
                return_to_mission()


def turn_camera(x: int, y: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("a")
    keyboard.release("d")
    keyboard.release("shift+w")
    keyboard.release("alt")
    keyboard.release("f")
    pyautogui.mouseUp(button="right")

    # fmt: off
    from helm_collect_loot import total_engramed_collected  # pylint: disable=C0412 | ungrouped-imports
    print(f"Total Loot Collected: {total_engramed_collected}")

    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
