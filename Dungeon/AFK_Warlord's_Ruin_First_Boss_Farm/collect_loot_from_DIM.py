import time
import keyboard
import pyautogui
import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/Dungeon/AFK_Warlord's_Ruin_First_Boss_Farm/Image_{current_monitor_resolution}"


def collect_loot_from_DIM():
    keyboard.press_and_release("alt+tab")
    time.sleep(1)

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\DIM Collect Postmaster.png", confidence=0.7)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        keyboard.press_and_release("alt+tab")
    except TypeError:
        keyboard.press_and_release("alt+tab")
        print("DIM Collect Postmaster is not found")
