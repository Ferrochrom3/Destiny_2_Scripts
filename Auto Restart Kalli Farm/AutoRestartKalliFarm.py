import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
startTime = time.time()


def my_function():
    global run
    run = True

    while run:
        if pyautogui.locateOnScreen("Season Rank Progress.png", confidence=0.8):
            keyboard.press_and_release('m')
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
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen("launch.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                time.sleep(0.2)
                pyautogui.leftClick()
            except TypeError:
                print("No Launch Found")
                pass

            time.sleep(3)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


def stop_afk():
    global run
    run = False
    print("Execution Stopped")


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.add_hotkey('f8', stop_afk)
    keyboard.wait('f9')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
