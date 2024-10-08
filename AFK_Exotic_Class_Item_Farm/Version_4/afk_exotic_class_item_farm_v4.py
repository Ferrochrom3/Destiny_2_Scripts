"""
Performance (pre drop rate nerf):
Total Time: 32124 seconds | 535.39 minutes | 8.92 hours
Number of Runs: 416
Number of Chests Obtained: 826
Number of Drops: 16
Number of Missed Chests: 1
Drop Rate: 1.93%
Missed Chest Rate: 0.12%
Average Chests Per Run: 1.98
Average Time Taken For One Chest: 38.89s
Average Time Per Drop: 2007.8 seconds | 33.46 minutes | 0.56 hours
Number of Missed The Landing Relaunch: 0
Number of Missed The Pale Heart Relaunch: 0
"""

import sys
import os
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error, fix_internet_error
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import collect_loot
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import efficiency_evaluation
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4 import resolution_config
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4.check_chest_spawns import (
    is_chest_3_spawned,
    check_chest_4_spawn,
    check_additional_chest_spawns,
    get_sorted_chest_spawn_tracker,
    clear_chest_spawn_tracker,
)
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4.run_to_chest import run_to_chest_3, run_from_3_to_4, run_from_3_to_5, run_from_3_to_6, run_from_3_to_7, run_from_3_to_8, run_from_8_to_9
from Destiny_2_Scripts.AFK_Exotic_Class_Item_Farm.Version_4.relaunch import relaunch_the_landing, relaunch_into_the_pale_heart


"""
Location     : The Pale Heart - The Landing
Subclass     : Any
Abilities    : Triple Jump (Hunter), Burst Glide (Warlock), Catapult Lift (Titan)
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any
               Energy  - Still Hunt
               Power   - Any Sword
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Tier 10 Mobility (Hunter), Tier 1 Mobility (Warlock/Titan)
Reward       : Exotic Class Items, Pale Heart Engrams, Ghost Reputations, Gunsmith Engrams

Setup:
 - After landing in "The Landing", start the script

Process:
 - Start at The Landing landing zone.
 - Runs down to the left and check when Chest_3 spawns using Still Hunt.
 - When Chest_3 spawns, run towards it and collec the chest.
 - Scope in with Still Hunt again to see if Chest_5-8 have spawned. If so, move to the closest chest (4 being closest, 8 being farthest)
    - If Chest_8 and Chest_9 both spawned, Chest_9 will be collected after running to Chest_8
 - At most 3 chests will be collected. Once done, relaunch The Landing.
 - Relaunch The Pale Heart after collecting 35 chests to reset the progress of Overthrow so it doesn't reach level 2.

Additional Notes:
 - Drop rates have been significantly reduced. This is no longer a efficient farm for exotic class items, but can still be used for other things.
 - 60+ FPS
 - Must plant the Luminescent Seed by the chest.
 - Chest spawn is manipulated by standing at a specific spot before other chests have spawned. Must execute the script shortly after landing.
 - Must equip Wombo Detector Ghost mod.
"""

# Resolution config and image path setup
screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


start_time: str = time.time()
character_class: str = ""
character_position: str = ""


def prompt_instruction():
    """
    Prompt the user to input the character class that is used and the position, from top to bottom, the class is located in the character selection screen.
    """
    global character_class
    global character_position

    character_class = input(f"Which character are you running? (Warlock, Hunter, Titan){Fore.GREEN}").strip().capitalize()
    character_position = input(f"{Style.RESET_ALL}From top to bottom, which position is your {character_class} in the character selection screen? (First, Second, Third){Fore.GREEN}").strip().capitalize()

    print(f"{Style.RESET_ALL}Running Class: {character_class}")
    print(f"Character Position: {character_position}")


def verify_user_input(character_class: str, character_position: str):
    """
    Verify the user character class and position input.

    Args:
        character_class (str): The class of the character that is used (Warlock, Hunter, Titan).
        character_position (str): The position, from top to bottom, the class is located in the character selection screen (First, Second, Third).

    Returns:
        bool: Whether or not both inputs are valid.
    """
    valid_classes = {"Warlock", "Hunter", "Titan"}
    valid_positions = {"First", "Second", "Third"}

    class_valid = character_class in valid_classes
    position_valid = character_position in valid_positions

    if not class_valid:
        print(f'{Fore.RED}Your character class "{character_class}" is invalid. Please check spelling.{Style.RESET_ALL}')

    if not position_valid:
        print(f'{Fore.RED}Your character position "{character_position}" is invalid. Please check spelling.{Style.RESET_ALL}')

    print()
    return class_valid and position_valid


prompt_instruction()

while not verify_user_input(character_class, character_position):
    prompt_instruction()


def my_function():
    global start_time
    start_time = time.time()

    while True:
        if is_internet_error():
            fix_internet_error(character_position)
            relaunch_into_the_pale_heart(True)

        elif pyautogui.locateOnScreen(os.path.join(image_path, "Overthrow The Landing Icon.png"), confidence=0.8):
            # Reset Overthrow progress by go to orbit and relaunch The Pale Heart
            if efficiency_evaluation.number_of_chests_before_reset <= 0:
                efficiency_evaluation.number_of_chests_before_reset = 35
                time.sleep(0.5)
                relaunch_into_the_pale_heart()

            # Proceed normall to collect chests
            else:
                efficiency_evaluation.number_of_runs += 1
                time.sleep(0.5)

                # Swap to Still Hunt and run to corner
                keyboard.press_and_release("2")
                win32api_move_mouse(-800, 0)
                run_forward(3.5)
                win32api_move_mouse(200, 0)
                run_forward(3.5)
                win32api_move_mouse(2600, 0)

                # Check for Chest_3 spawn
                time.sleep(1)
                pyautogui.mouseDown(button="right")
                elapsed_time = time.time()
                while True:
                    if is_chest_3_spawned():
                        break
                    if time.time() - elapsed_time >= 30:
                        break
                pyautogui.mouseUp(button="right")

                # Run to Chest_3, collect if chest spawned
                run_to_chest_3()
                time.sleep(0.1)
                check_chest_4_spawn()
                collect_loot.collect_loot("Titan", "3", True)

                # Check additional chest spawns to collect a second chest before relaunching
                check_additional_chest_spawns()
                chest_spawns = get_sorted_chest_spawn_tracker()
                print(chest_spawns)

                if chest_spawns["Chest_4"]:
                    run_from_3_to_4(character_class)
                    collect_loot.collect_loot(character_class, "4")
                elif chest_spawns["Chest_5"]:
                    run_from_3_to_5(character_class)
                    collect_loot.collect_loot(character_class, "5")
                elif chest_spawns["Chest_6"]:
                    run_from_3_to_6(character_class)
                    collect_loot.collect_loot(character_class, "6")
                elif chest_spawns["Chest_7"]:
                    run_from_3_to_7()
                    collect_loot.collect_loot(character_class, "7")
                elif chest_spawns["Chest_8"] and chest_spawns["Chest_9"]:
                    run_from_3_to_8()
                    collect_loot.collect_loot(character_class, "8")
                    run_from_8_to_9()
                    collect_loot.collect_loot(character_class, "9")
                elif chest_spawns["Chest_8"]:
                    run_from_3_to_8()
                    collect_loot.collect_loot(character_class, "8")

                clear_chest_spawn_tracker()

                relaunch_the_landing()


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def run_forward(running_duration: float, wait_time: float = 0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def start_afk():
    afk_thread = threading.Thread(target=my_function)
    afk_thread.start()
    print("Execution Started")

    # fmt: off
    status_thread = threading.Thread(target=efficiency_evaluation.display_status,args=(start_time,1000,))
    status_thread.start()
    # fmt: on


print("Press F7 to Start")
print("Press F8 to Exit\n")

while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("shift+w")
    keyboard.release("alt")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    print(efficiency_evaluation.create_status(start_time))

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
