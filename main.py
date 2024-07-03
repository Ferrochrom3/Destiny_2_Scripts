import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style
from pynput.mouse import Button, Controller

"""
***Need all imports, opencv-python, and Pillow***

print(pyautogui.position())                                       Print current mouse cursor location
time.sleep(x)                                                     Delay x seconds

pyautogui.click()                                                 Click (x, y)
pyautogui.click(clicks=3, interval=0.1)                           Click once every 0.1 seconds for 3 times
pyautogui.mouseDown(button='left')                                Hold down left mouse button
pyautogui.mouseUp(button='left')                                  Release left mouse button
pyautogui.moveTo(x, y, duration=1)                                Move mouse to (x, y) taking a total of 1 second
pyautogui.moveRel(100, 100, duration=1)                           Move mouse by (x, y) from the current position taking a total of 1 second

pyautogui.press()                                                 Press a key like 'a'
pyautogui.keyDown('ctrl')                                         Hold down ctrl
pyautogui.keyUp('ctrl')                                           Release ctrl

keyboard.is_pressed('a')                                          Check if 'a' is pressed
keyboard.press('a')                                               Hold down 'a'
keyboard.release('a')                                             Release 'a'
keyboard.press_and_release('a')           

win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 100, 0, 0)   Move 100 pixels to the right and 100 pixels down relative to your current mouse position

Controller().click(Button.x1)                                     Click mouse button 4 (x2 is 5)

pyautogui.FAILSAFE = False                                        Remove mouse movement restrictions

region = (x, y, w, h)                                             (x-coord of the top-left corner, y-coordof the top-left corner, Width of the region, Height of the region)
"""


print("Testing")
print("Press F7 to Start")
print("Press F8 to Exit\n")

start_time = time.time()


def my_function():
    while True:
        print(pyautogui.mouseInfo())
        break


def turn_camera(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


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
