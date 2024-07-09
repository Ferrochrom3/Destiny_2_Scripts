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

    print("Relaunching")
    number_of_relaunching += 1
    keyboard.press_and_release("m")

    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Campaign Mission Icon.png", confidence=0.8):
            time.sleep(0.2)
            break

    win32api_move_mouse(config["relaunch_the_landing_move_left"][0], config["relaunch_the_landing_move_left"][1], 2.2)
    win32api_move_mouse(config["relaunch_the_landing_move_right"][0], config["relaunch_the_landing_move_right"][1], 0.2)
    time.sleep(0.3)

    # If the mouse cursor did not move to the landing zone correctly, close the map and try again
    if not pyautogui.locateOnScreen(f"{image_path}/The Landing Landing Zone.png", confidence=0.8):
        print("Mouse cursor did not move to landing zone correctly while relaunching The Landing...Retrying...")
        number_of_relaunching -= 1
        keyboard.press_and_release("m")
        time.sleep(1)
        relaunch_the_landing()

    # Otherwise proceed to click the landing zone
    else:
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
            win32api_move_mouse(0, 100)  # Move mouse cursor slightly down so it's not on The Pale Heart so the destination icon doesn't change
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

    print("Waiting For The Pale Heart Map to Open")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Campaign Mission Icon.png", confidence=0.8):
            time.sleep(0.2)

            # Move to The Landing
            win32api_move_mouse(config["launch_into_the_pale_heart_move_left"][0], config["launch_into_the_pale_heart_move_left"][1], 2.2)
            win32api_move_mouse(config["launch_into_the_pale_heart_move_right"][0], config["launch_into_the_pale_heart_move_right"][1], 0.2)
            time.sleep(0.3)

            # If the mouse cursor did not move to the landing zone correctly, close the map and try again
            if not pyautogui.locateOnScreen(f"{image_path}/The Landing Landing Zone.png", confidence=0.8):
                print("Mouse cursor did not move to landing zone correctly while relaunching The Pale Heart...Retrying...")
                relaunch_into_the_pale_heart()

            # Otherwise click on landing zone and launch into The Pale Heart
            else:
                pyautogui.leftClick()
                time.sleep(1)
                pyautogui.moveTo(config["launch_button_coord"][0], config["launch_button_coord"][1])
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(1)

            break


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)
