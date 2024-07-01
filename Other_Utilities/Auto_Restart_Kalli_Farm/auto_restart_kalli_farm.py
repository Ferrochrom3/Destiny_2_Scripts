import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con

print("Press F7 to Start")
print("Press F8 to Exit\n")

start_time = time.time()


def my_function():
    while True:
        if pyautogui.locateOnScreen("Season Rank Progress.png", confidence=0.8):
            keyboard.press_and_release("m")
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -2000, 0, 0)
            time.sleep(0.3)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 300, 0, 0)

            try:
                x, y = pyautogui.locateCenterOnScreen("Last Wish.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                time.sleep(0.2)
                pyautogui.leftClick()
            except TypeError:
                print("No Last Wish Found")

            try:
                x, y = pyautogui.locateCenterOnScreen("launch.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                time.sleep(0.2)
                pyautogui.leftClick()
            except TypeError:
                print("No Launch Found")

            time.sleep(3)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    f"Elapsed Time: {round(time.time() - start_time)} seconds"
    f"\n{round((time.time() - start_time) / 60, 2)} minutes"
    f"\n{round((time.time() - start_time) / 3600, 2)} hours")
    # fmt: on
