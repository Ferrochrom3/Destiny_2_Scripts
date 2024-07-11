import os
import sys
import time
import pyautogui
import win32api
import win32con
import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS + "/Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_4/"
else:
    base_path = os.path.dirname(__file__)

image_path = os.path.join(base_path, f"Image_{current_monitor_resolution}")


chest_spawn_tracker = {}


def is_chest_3_spawned():
    """
    Check if Chest_3 has spawned. Used when scoped in with Still Hunt.

    Returns:
        bool: Whether or not Chest_3 has spawened.
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_3.png"), confidence=0.8, region=config["chest_3_region"]):
        chest_spawn_tracker["Chest_3"] = True
    else:
        chest_spawn_tracker["Chest_3"] = False

    return chest_spawn_tracker["Chest_3"]


def check_additional_chest_spawns():
    """
    Does Chest_4 to Chest_8 checks, all in a single function.
    """
    # Chest chests that does not require any camera turns
    check_chest_4_spawn()

    # Check chests that require scope in after a small camera turn
    win32api_move_mouse(600, -100)
    pyautogui.mouseDown(button="right")
    time.sleep(1)
    check_chest_6_spawn()
    check_chest_7_spawn()
    check_chest_8_spawn()
    pyautogui.mouseUp(button="right")
    time.sleep(0.6)

    # Check chests that does not require scope in after another camera turn after the previous
    win32api_move_mouse(1400, 0)
    check_chest_5_spawn()


# Check right after oepning Chest_3
def check_chest_4_spawn():
    """
    Check if Chest_4 has spawned. If so, update the chest key in "chest_spawn_tracker" dictionary to True, otherwise update the key to False
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_4.png"), confidence=0.8, region=config["chest_4_region"]):
        chest_spawn_tracker["Chest_4"] = True
    else:
        chest_spawn_tracker["Chest_4"] = False


# Check after checking Chest_6-8
def check_chest_5_spawn():
    """
    Check if Chest_5 has spawned. If so, update the chest key in "chest_spawn_tracker" dictionary to True, otherwise update the key to False
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_5.png"), confidence=0.8, region=config["chest_5_region"]):
        chest_spawn_tracker["Chest_5"] = True
    else:
        chest_spawn_tracker["Chest_5"] = False


# Check after checking Chest_4
def check_chest_6_spawn():
    """
    Check if Chest_6 has spawned. If so, update the chest key in "chest_spawn_tracker" dictionary to True, otherwise update the key to False
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_6.png"), confidence=0.8, region=config["chest_6_region"]):
        chest_spawn_tracker["Chest_6"] = True
    else:
        chest_spawn_tracker["Chest_6"] = False


def check_chest_7_spawn():
    """
    Check if Chest_7 has spawned. If so, update the chest key in "chest_spawn_tracker" dictionary to True, otherwise update the key to False
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_7.png"), confidence=0.8, region=config["chest_7_region"]):
        chest_spawn_tracker["Chest_7"] = True
    else:
        chest_spawn_tracker["Chest_7"] = False


def check_chest_8_spawn():
    """
    Check if Chest_8 has spawned. If so, update the chest key in "chest_spawn_tracker" dictionary to True, otherwise update the key to False
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_8.png"), confidence=0.8, region=config["chest_8_region"]):
        chest_spawn_tracker["Chest_8"] = True
    else:
        chest_spawn_tracker["Chest_8"] = False


def is_chest_9_spawned():
    """
    Check if Chest_9 has spawned after collecting Chest_8.

    Returns:
        bool: Whether or not Chest_9 has spawened.
    """
    if pyautogui.locateOnScreen(os.path.join(image_path, "Chest_9.png"), confidence=0.8, region=config["chest_9_region"]):
        chest_spawn_tracker["Chest_9"] = True
    else:
        chest_spawn_tracker["Chest_9"] = False

    return chest_spawn_tracker["Chest_9"]


def get_sorted_chest_spawn_tracker():
    """Gets a sorted chest spawn tracker

    Returns:
        dictionary: A sorted dictionary that shows which chests have spawned.
    """
    return {key: chest_spawn_tracker[key] for key in sorted(chest_spawn_tracker)}


def clear_chest_spawn_tracker():
    """
    Clear all key values pairs in chest spawn tracker.
    """
    chest_spawn_tracker.clear()


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)
