import pyautogui
import time
import keyboard
import sys
import threading
import win32api
import win32con

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")

run = True
startTime = time.time()


def afk():
    global run
    run = True
    while run:
        # checks if weapon has ammo
        if pyautogui.locateCenterOnScreen("0 Ammo.png", confidence=0.9, region=(609, 1218, 707, 1280)):  # out of ammo
            keyboard.send('1')  # swap to primary
            time.sleep(1)

            if pyautogui.locateOnScreen("Rift.png", confidence=0.8, grayscale=True, region=(333, 1228, 427, 1312)):
                keyboard.send('v')  # place rift
                time.sleep(2.3)
                keyboard.send('\\')  # press to crouch
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 500, 0, 0)  # look down after using rift

            for x in range(10):  # shoot 10 times to get some ammo
                pyautogui.mouseDown(button='left')
                time.sleep(0.6)
                pyautogui.mouseUp(button='left')
                time.sleep(2)
                if not run:
                    break

            keyboard.send('2')  # swap back to energy
            time.sleep(2.5)

        # if weapon has ammo, shoot
        else:
            if not pyautogui.locateOnScreen("Path of Least Resistance Icon.png",
                                            confidence=0.9, grayscale=True, region=(429, 1222, 573, 1293)):
                keyboard.press_and_release('2')
                time.sleep(1.3)

            for x in range(10):
                pyautogui.mouseDown(button='left')
                time.sleep(0.2)
                pyautogui.mouseUp(button='left')
                time.sleep(0.5)

            keyboard.press_and_release('r')
            time.sleep(2)


def start_afk():
    t = threading.Thread(target=afk)
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
             + str(round((time.time() - startTime) / 60, 1)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 1)) + " hours")
