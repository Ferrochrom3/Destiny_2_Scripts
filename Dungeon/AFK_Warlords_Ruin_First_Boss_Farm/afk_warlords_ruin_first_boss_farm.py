"""
Performance (out of 79.46 minutes):
 - Total Attempts: 83
 - Fail Attempts: 70
 - Success Attempts: 13
 - Success Rate: 15.66%
 - Average Time Per Attempt: 57s
 - Average Time Per Success: 6.1 minutes
"""

import os
import sys
import threading
import time
import keyboard
import pyautogui
import efficiency_evaluation
from colorama import Fore, Style
from boss_yeet_exeuction import indebted_kindness, emote_at_corner, check_cases
from dungeon_restart_and_reset import relaunch_into_master, reset_checkpoint, reenter_dungeon_after_internet_error

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error, fix_internet_error


"""
Location     : Warlord's Ruin - First Encounter
Subclass     : Void Hunter
Abilities    : Snare Bomb
Fragments    : Echo of Persistance, Echo of Obscurity
Aspects      : Trapper's Ambush
Weapons      : Kinetic - Any
               Energy  - Indebted Kindness (with any Champion mod)
               Power   - Any Grenade Launcher
Exotic Armor : Graviton Forefeit
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Proximity Ward
Stats        : T9 Mobility
Reward       : XP, Master Dungeon Loot (first boss loot table)

Additional Notes:
 - Cap FPS to 120
 - Use "Censered" Finisher and "Anniversary Pose" Emote (emote must be binded to "left").
 - DIM must be one Alt+Tab away from the game for loot collectiong to work.
 - Strength stats has no requirements but higher strength allows quicker restart when melee did not regen back after initial use.
"""

pyautogui.FAILSAFE = False

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/Dungeon/AFK_Warlords_Ruin_First_Boss_Farm/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


start_time = time.time()


def my_function():
    while True:
        if is_internet_error():
            fix_internet_error("first")
            reenter_dungeon_after_internet_error()
            reset_checkpoint()

        if pyautogui.locateOnScreen(os.path.join(image_path, "Smoke Bomb.png"), confidence=0.9):
            if efficiency_evaluation.total_failed_attempts > 0 and efficiency_evaluation.total_failed_attempts % 10 == 0:
                print("Too many failed attempts, relaunching the dungeon...")
                relaunch_into_master()
                reset_checkpoint()
            else:
                print("======================New attempt======================")
                indebted_kindness()
                emote_at_corner()
                check_cases()


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


print("Press F7 to Start")
print("Press F8 to Exit\n")

while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("shift")
    keyboard.release("w")
    keyboard.release("a")
    keyboard.release("s")
    keyboard.release("d")
    keyboard.release("ctrl")
    keyboard.release("alt")
    keyboard.release("tab")
    keyboard.release("left")
    pyautogui.mouseUp(button="right")
    efficiency_evaluation.display_status(start_time)

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
