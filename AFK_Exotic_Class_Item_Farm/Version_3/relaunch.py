import time
import keyboard
import pyautogui
import win32api
import win32con
import resolution_config

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_3/Image_{current_monitor_resolution}"

number_of_relaunching = 0
max_number_of_relaunching = 35


def relaunch_the_landing():
    global number_of_relaunching

    print("Relaunching...")
    number_of_relaunching += 1
    keyboard.press_and_release("m")

    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Campaign Mission Icon.png", confidence=0.8):
            time.sleep(0.2)
            break

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, config["relaunch_the_landing_move_left"][0], config["relaunch_the_landing_move_left"][1], 0, 0)
    time.sleep(2.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, config["relaunch_the_landing_move_right"][0], config["relaunch_the_landing_move_right"][1], 0, 0)
    time.sleep(0.2)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.mouseDown(button="left")
    time.sleep(1.3)
    pyautogui.mouseUp(button="left")
    time.sleep(1)


def relaunch_into_the_pale_heart():
    keyboard.press_and_release("tab")
    time.sleep(1.5)
    keyboard.press_and_release("o")
    time.sleep(0.3)
    keyboard.press("o")
    time.sleep(3)
    keyboard.release("0")

    print("Waiting to Open Director")
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
        if pyautogui.locateOnScreen(f"{image_path}/Campaign Mission Icon.png", confidence=0.8):
            time.sleep(0.2)

            # Move to The Landing
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, config["launch_into_the_pale_heart_move_left"][0], config["launch_into_the_pale_heart_move_left"][1], 0, 0)
            time.sleep(2.2)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, config["launch_into_the_pale_heart_move_right"][0], config["launch_into_the_pale_heart_move_right"][1], 0, 0)
            time.sleep(0.2)
            pyautogui.leftClick()
            time.sleep(1)

            # Click on Launch
            pyautogui.moveTo(config["launch_button_coord"][0], config["launch_button_coord"][1])
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
            break
