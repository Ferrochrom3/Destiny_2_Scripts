import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con

"""
Prerequisites: Strand Hunter
             : Tier 7 Mobility (exactly)
             : Gjallarhorn
             : 2560 x 1440 Resolution
             : All required Images
             : Solo Enabler
"""

print("Press F7 to Start")
print("Press F8 to Stop (only stops after current iteration)")
print("Press F9 to End\n")

run = False
startTime = time.time()


def my_function():
    global run
    run = True

    while run:
        while True:
            if pyautogui.locateOnScreen("Threaded Spike.png", confidence=0.8, grayscale=True):
                break

        breakneck_move()
        for x in range(5):
            breakneck_kill()

        keyboard.press_and_release('m')
        time.sleep(1.5)
        keyboard.press_and_release('a')
        time.sleep(1.5)

        try:
            x, y = pyautogui.locateCenterOnScreen("Platinum Cards-Neptune.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(0.5)
        except TypeError:
            print("Completed Bounty Not Found")
            pass

        keyboard.press_and_release('d')
        time.sleep(0.5)
        keyboard.press_and_release('d')
        time.sleep(1.5)

        try:
            x, y = pyautogui.locateCenterOnScreen("Tower.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
        except TypeError:
            print("Tower Not Found")
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen("Landing Zone.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
        except TypeError:
            print("Landing Zone Not Found")
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
        except TypeError:
            print("Launch Not Found")
            pass

        while True:
            if pyautogui.locateOnScreen("Courtyard.png", confidence=0.8, grayscale=True):
                break

        repurchase_card()

        keyboard.press_and_release('m')
        time.sleep(1.5)
        keyboard.press_and_release('d')
        time.sleep(1.5)

        try:
            x, y = pyautogui.locateCenterOnScreen("Neptune.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
        except TypeError:
            print("Neptune Not Found")
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen("Legendary Campaign.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
        except TypeError:
            print("Legendary Campaign Not Found")
            pass

        pyautogui.moveTo(1952, 1103)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1.5)
        pyautogui.moveTo(366, 617)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(2)
        pyautogui.moveTo(2107, 1191)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(25)


def breakneck_move():
    # platform
    keyboard.press('shift+w')
    time.sleep(3)
    keyboard.press_and_release('space')
    time.sleep(0.2)
    keyboard.press_and_release('space')
    time.sleep(0.2)
    keyboard.press_and_release('space')
    time.sleep(0.5)

    # door
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1300, 0, 0, 0)
    time.sleep(0.2)
    keyboard.release('shift+w')
    time.sleep(0.5)
    keyboard.press_and_release('space')
    time.sleep(0.2)
    keyboard.press('shift+w')
    keyboard.press_and_release('space')
    time.sleep(0.2)
    keyboard.press_and_release('space')
    time.sleep(3.9)
    keyboard.release('shift+w')
    time.sleep(0.2)

    # towards strand
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2500, 0, 0, 0)
    time.sleep(0.2)
    keyboard.press('shift+w')
    time.sleep(1.1)
    keyboard.press_and_release('space')
    time.sleep(0.1)
    keyboard.press_and_release('space')
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -800, 0, 0, 0)
    time.sleep(1.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -700, 0, 0, 0)
    time.sleep(2.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1200, 0, 0, 0)
    time.sleep(1.1)
    keyboard.release('shift+w')

    # acquire strand
    keyboard.press('alt')
    time.sleep(1)
    keyboard.release('alt')
    time.sleep(2)

    # turn around
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3900, 0, 0, 0)
    time.sleep(0.2)
    keyboard.press_and_release('q')  # grapple
    time.sleep(3)

    # grapple across
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 900, 0, 0, 0)
    time.sleep(0.2)
    keyboard.press('shift+w')
    time.sleep(0.2)
    keyboard.press_and_release('space')
    time.sleep(0.5)
    keyboard.press_and_release('space')
    time.sleep(0.5)
    keyboard.press_and_release('space')
    time.sleep(0.5)
    keyboard.press_and_release('q')
    keyboard.release('shift+w')
    time.sleep(3.5)

    # towards rally
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1500, 0, 0, 0)
    time.sleep(0.2)
    keyboard.press('shift+w')
    time.sleep(3.9)
    keyboard.release('shift+w')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -500, 0, 0, 0)
    time.sleep(0.2)
    keyboard.press('shift+w')
    time.sleep(1)
    keyboard.release('shift+w')

    # proper position
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -700, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1700, 0, 0, 0)
    time.sleep(0.5)


def breakneck_kill():
    keyboard.press_and_release('3')

    # centering
    keyboard.press('d')
    time.sleep(0.2)
    keyboard.release('d')
    keyboard.press('shift+w')
    time.sleep(1)
    keyboard.release('shift+w')

    # break door
    keyboard.press_and_release('c')
    time.sleep(1)

    # rally
    keyboard.press('w')
    time.sleep(0.5)
    keyboard.release('w')
    keyboard.press('alt')
    time.sleep(2)
    keyboard.release('alt')
    time.sleep(2)

    # move right
    keyboard.press('d')
    time.sleep(0.4)
    keyboard.release('d')

    # attack 1
    keyboard.press('shift+w')
    time.sleep(2.2)
    keyboard.release('shift+w')
    keyboard.press_and_release('f')
    time.sleep(1.7)
    pyautogui.rightClick()
    time.sleep(1)
    keyboard.press('shift+w')
    time.sleep(1.2)
    keyboard.release('shift+w')
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(0.5)

    # attack 2
    keyboard.press('shift+w')
    time.sleep(2.7)
    keyboard.release('shift+w')
    time.sleep(0.5)
    pyautogui.rightClick()

    # attack 3
    keyboard.press('shift+w')
    time.sleep(5)
    keyboard.release('shift+w')
    keyboard.press('a')
    time.sleep(1)
    keyboard.release('a')
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)

    # suicide
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 2000, 0, 0)
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(1)

    while True:
        if pyautogui.locateOnScreen("Threaded Spike.png", confidence=0.8, grayscale=True):
            break


def repurchase_card():
    # deposit medal
    keyboard.press('shift+w')
    time.sleep(5)
    keyboard.release('shift+w')
    keyboard.press('alt')
    time.sleep(1)
    keyboard.release('alt')
    time.sleep(2)

    # back to eva
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3400, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift+w')
    time.sleep(1.8)
    keyboard.release('shift+w')
    keyboard.press('alt')
    time.sleep(1.5)
    keyboard.release('alt')
    time.sleep(3)

    try:
        x, y = pyautogui.locateCenterOnScreen("Platinum Cards-Neptune.png", confidence=0.9)
        pyautogui.moveTo(x, y)
        time.sleep(1)
        pyautogui.leftClick()
    except TypeError:
        pass


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
    keyboard.release('shift+w')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('alt')
    keyboard.release('space')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
