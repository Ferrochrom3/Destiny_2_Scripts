import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con


print("Press F7 to Start")
print("Press F8 to Exit\n")


def my_function():
    while True:
        if pyautogui.locateOnScreen("Witherhoard Icon.png", grayscale=True, confidence=0.8):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 0, 0, 0)
            keyboard.press_and_release("tab")
            time.sleep(1)

            if pyautogui.locateOnScreen("Heroic Patrol Icon 1.png", confidence=0.7, grayscale=True):
                print("Found Heroic Patrol 1")
                x, y = pyautogui.locateCenterOnScreen("Heroic Patrol Icon 1.png", confidence=0.7, grayscale=True)
                keyboard.press_and_release("esc")
                pyautogui.moveTo(x, y)
                break
            elif pyautogui.locateOnScreen("Heroic Patrol Icon 2.png", confidence=0.7, grayscale=True):
                print("Found Heroic Patrol 2")
                x, y = pyautogui.locateCenterOnScreen("Heroic Patrol Icon 2.png", confidence=0.7, grayscale=True)
                keyboard.press_and_release("esc")
                pyautogui.moveTo(x, y)
                break
            else:
                print("No Heroic Patrol Found")
                print("Opening Map")
                keyboard.press_and_release("m")
                time.sleep(1)

                pyautogui.moveRel(0, 2000)
                time.sleep(0.4)
                pyautogui.moveRel(0, -300)

        try:
            x, y = pyautogui.locateCenterOnScreen("Terminal Overload Icon.png", confidence=0.8)
            print("Move to Terminal Overload")
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
            time.sleep(0.8)
        except TypeError:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.8)
            print("Launch")
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
        except TypeError:
            pass


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    sys.exit()
