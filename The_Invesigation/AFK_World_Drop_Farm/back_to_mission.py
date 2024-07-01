import time
import keyboard
import pyautogui
import win32api
import win32con

image_path = "Destiny 2 Scripts/Investigation Mission/AFK World Drop Farm"


def return_to_mission():
    print("Returning to the mission")
    keyboard.press_and_release("m")
    time.sleep(1.5)
    keyboard.press_and_release("d")
    time.sleep(1.5)

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Throne World.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1.5)

    # Select normal campaign difficulty
    turn_camera(500, 0)
    turn_camera(0, 500)
    time.sleep(0.5)
    turn_camera(0, -500)
    select_campaign_mission()

    # Run towards enemy spawning area and suicide to get ready
    run_towards_suicide_zone()


def select_campaign_mission():
    x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Normal Campaign Icon.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1.5)

    # Click on mission
    pyautogui.moveTo(2077, 1107)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on "The Investigation" mission
    pyautogui.moveTo(392, 456)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on launch
    pyautogui.moveTo(2163, 1210)
    time.sleep(0.3)
    pyautogui.leftClick()

    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Grapple Grenade.png", confidence=0.9):
            break


def run_towards_suicide_zone():
    # Run towards the gate
    turn_camera(100, 0)
    keyboard.press("shift+w")
    time.sleep(7)
    keyboard.release("shift+w")

    # Run pass the gate
    turn_camera(-480, 0)
    keyboard.press("shift+w")
    time.sleep(7.5)
    keyboard.release("shift+w")

    # Run down the slope
    turn_camera(640, 0)
    keyboard.press("shift+w")
    time.sleep(15)
    keyboard.release("shift+w")

    # Run down the ramp
    turn_camera(-850, 0)
    keyboard.press("shift+w")
    time.sleep(5)
    keyboard.release("shift+w")

    # Run towards suicide zone
    turn_camera(400, 0)
    keyboard.press("shift+w")
    time.sleep(3)
    turn_camera(400, 0)
    time.sleep(5)
    keyboard.release("shift+w")

    keyboard.press_and_release("2")
    turn_camera(0, 3000)
    time.sleep(1)
    for _ in range(4):
        pyautogui.leftClick()
        time.sleep(0.5)

    # elapsed_time = time.time()
    # while True:
    #     if pyautogui.locateOnScreen(f"{image_path}/Objective Icon.png", confidence=0.8):
    #         print("FOJ:ASLKFJSD")
    #         break
    #     elif time.time() - elapsed_time > 30:
    #         print("Did not reach destination correctly...Restarting")

    #         keyboard.press_and_release("m")
    #         time.sleep(1.5)
    #         turn_camera(0, 1000)
    #         time.sleep(0.8)
    #         turn_camera(0, -500)
    #         select_campaign_mission()
    #         break


def turn_camera(x: int, y: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(0.1)
