import os
import sys
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

from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import status_display
from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import prompt_instructions
from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import resolution_config
from Destiny_2_Scripts.Other_Utilities.Wait_For_Joins import dreaming_city

"""
Location     : Any
Subclass     : Any
Abilities    : Any
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Any
               Energy  - Any
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : None

Setup:
 - Follow the instruction prompts to choose character, type of the activity, and the actual activity.
 - Load into the activity that is chosen in the instruction prompt.
 - After landing, start the script.
 
Process:
 - User will wait inside of the chosen activity until another player joins.
 - After a player join is detected, go back to Character Selection screen and select the chosen character.
 - Then, load in to the chosen activity to repeat the cycle.

Additional Notes:
 - None
"""

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


start_time = time.time()


def my_function():
    global start_time
    start_time = time.time()

    while True:
        if pyautogui.locateOnScreen(os.path.join(image_path, "Player Joined.png"), confidence=0.8, region=config["player_joined_region"]):
            swap_character()

            # Opens map
            keyboard.press_and_release("m")
            time.sleep(2)

            match (prompt_instructions.activity_name):
                case "The Shattered Throne":
                    dreaming_city.launch_shattered_throne()

                case _:
                    print("Something went wrong...")

        else:
            status_display.current_status = "Waiting For Joins"
            keyboard.press_and_release("a")
            time.sleep(1)
            keyboard.press_and_release("d")
            time.sleep(1)


def swap_character():
    """Swap character by opening the "Game Options" menu with "Esc" and go to the character selection menu to select a character

    Args:
        character_to_select (str): First, second, or third. The string will automatically be converted to lower case.
    """

    status_display.current_status = "Swapping Character"

    time.sleep(8)
    keyboard.press_and_release("esc")
    time.sleep(1)
    pyautogui.moveTo(config["change_character"][0], config["change_character"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(config["confirm_change_character"][0], config["confirm_change_character"][1])
    time.sleep(0.1)
    pyautogui.leftClick()

    status_display.current_status = "Waiting to Select Character"
    while True:
        if pyautogui.locateOnScreen(os.path.join(image_path, "Patch Notes Icon.png"), confidence=0.8, region=config["patch_notes_icon_region"]):
            pyautogui.moveTo(config[f"{prompt_instructions.character_to_select}_character"][0], config[f"{prompt_instructions.character_to_select}_character"][1])
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(2)
            break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def start_afk():
    afk_thread = threading.Thread(target=my_function)
    afk_thread.start()

    # fmt: off
    status_thread = threading.Thread(target=status_display.display_status,args=(start_time,1000,))
    status_thread.start()
    # fmt: on

    print("Execution Started")


prompt_instructions.prompt_character_selection_instruction()
prompt_instructions.prompt_activity_type_instruction()
prompt_instructions.prompt_activity_name_instruction()
prompt_instructions.show_final_results()

print("Press F7 to Start")
print("Press F8 to Exit\n")

while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
