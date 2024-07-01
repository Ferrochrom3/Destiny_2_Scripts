import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style
from Destiny_2_Scripts.The_Invesigation.AFK_World_Drop_Farm.shoot_enemies import shoot_enemy
from Destiny_2_Scripts.The_Invesigation.AFK_World_Drop_Farm.helm_collect_loot import go_to_helm_and_collect_loot
from Destiny_2_Scripts.The_Invesigation.AFK_World_Drop_Farm.back_to_mission import return_to_mission
from Destiny_2_Scripts.Other_Utilities.Broccoli_Error_Fix.broccoli_error_fix import is_error, fix_error


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
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

pyautogui.FAILSAFE = False
start_time = time.time()


def my_function():
    while True:
        if is_error():
            fix_error()
            return_to_mission()

        else:
            for _ in range(80):
                shoot_enemy()

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
    from Destiny_2_Scripts.The_Invesigation.AFK_World_Drop_Farm.helm_collect_loot import total_engramed_collected  # pylint: disable=C0412
    print(f"Total Loot Collected: {total_engramed_collected}")

    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
