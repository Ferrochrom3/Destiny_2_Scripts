import os
import sys
import time
import keyboard
import pyautogui
import win32api
import win32con
from collect_loot_from_DIM import collect_loot_from_DIM

destiny_2_scripts_path = os.path.abspath("Destiny_2_Scripts")
folder_path = os.path.dirname(destiny_2_scripts_path)
sys.path.insert(0, folder_path)
from Destiny_2_Scripts.Dungeon.AFK_Warlords_Ruin_First_Boss_Farm import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/Dungeon/AFK_Warlord's_Ruin_First_Boss_Farm/Image_{current_monitor_resolution}"


def relaunch_into_master():
    """
    Open up the map and move mouse to the right side of the map, then move back. Find the dungeon icon, click on it, navigate to Master difficulty, and click "Launch". Wait until "In Dungeon Icon" shows up.
    """
    keyboard.press_and_release("m")
    time.sleep(1)
    win32api_move_mouse(config["relaunch_into_master_move_right"][0], config["relaunch_into_master_move_right"][1])
    time.sleep(1)
    win32api_move_mouse(config["relaunch_into_master_move_left"][0], config["relaunch_into_master_move_left"][1])

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Dungeon Icon.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("Dungeon Icon Not Found")

    time.sleep(1)

    # Click on Change Activity Difficulty
    pyautogui.moveTo(config["change_difficulty_coord"][0], config["change_difficulty_coord"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on Master
    pyautogui.moveTo(config["select_mode_master_coord"][0], config["select_mode_master_coord"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on Launch
    pyautogui.moveTo(config["launch_button_coord"][0], config["launch_button_coord"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    print("Waiting to Load In")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/In Dungeon Icon.png", confidence=0.8):
            print("Loaded into Dungeon")
            break


def reset_checkpoint():
    """
    Open up the map and move mouse to the right side of the map, then move back. Find the dungeon icon, click on it, navigate to Master difficulty, hover over dungeon checkpoint, and reset it. Then, use heavy to suicide and wait until respawn.
    """
    keyboard.press_and_release("m")
    time.sleep(1)
    win32api_move_mouse(config["relaunch_into_master_move_right"][0], config["relaunch_into_master_move_right"][1])
    time.sleep(1)
    win32api_move_mouse(config["relaunch_into_master_move_left"][0], config["relaunch_into_master_move_left"][1])

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Dungeon Icon.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("Dungeon Icon Not Found")

    time.sleep(1)

    # Click on Change Activity Difficulty
    pyautogui.moveTo(config["change_difficulty_coord"][0], config["change_difficulty_coord"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on Master
    pyautogui.moveTo(config["select_mode_master_coord"][0], config["select_mode_master_coord"][1])
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Reset checkpoint
    pyautogui.moveTo(config["checkpoint_coord"][0], config["checkpoint_coord"][1])
    time.sleep(0.1)
    keyboard.press("f")
    time.sleep(3)
    keyboard.release("f")
    time.sleep(0.1)
    keyboard.press_and_release("esc")
    time.sleep(0.5)
    keyboard.press_and_release("esc")
    time.sleep(1)

    # Aim at boss and shoot to trigger encounter
    keyboard.press_and_release("2")
    time.sleep(1.7)
    pyautogui.mouseDown(button="right")
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -150, -190, 0, 0)
    time.sleep(0.1)
    pyautogui.leftClick()
    pyautogui.mouseUp(button="right")

    # Use heavy to suicide
    keyboard.press_and_release("3")
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)

    collect_loot_from_DIM()

    print("Waiting for respawn after suicide")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Smoke Bomb.png", confidence=0.8):
            time.sleep(1)
            print("Respawned")
            break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)
