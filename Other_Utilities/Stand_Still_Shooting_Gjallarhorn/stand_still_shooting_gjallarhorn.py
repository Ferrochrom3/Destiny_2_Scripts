import pyautogui
import time
import keyboard
import sys
import threading
import win32con
import win32api

print("Press F7 to Start")
print("Press F8 to Exit\n")

pyautogui.FAILSAFE = False


def afk():
    while True:
        keyboard.press_and_release("f")
        time.sleep(3)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1000, 0, 0)
        for _ in range(7):
            pyautogui.leftClick()
            time.sleep(5)
        break


def start_afk():
    t = threading.Thread(target=afk)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    sys.exit()
