import sys
import threading
import time
import keyboard
import pyautogui

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
startTime = time.time()


def my_function():
    global run
    run = True

    while run:
        for x in range(50):
            acquire_and_dismantle()

        keyboard.press_and_release('esc')
        time.sleep(2.8)

        pyautogui.moveTo(1544, 231)
        time.sleep(0.5)
        pyautogui.leftClick()

        for x in range(24):
            pyautogui.leftClick()
            time.sleep(0.8)

        keyboard.press_and_release('f1')
        time.sleep(0.7)


def acquire_and_dismantle():
    keyboard.press_and_release('a')
    time.sleep(0.5)
    keyboard.press_and_release('a')
    time.sleep(0.7)

    try:
        x, y = pyautogui.locateCenterOnScreen("Collections Armor.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()
    except TypeError:
        pass

    time.sleep(0.5)

    try:
        x, y = pyautogui.locateCenterOnScreen("Events.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()
    except TypeError:
        pass

    time.sleep(0.5)
    pyautogui.moveTo(2405, 762)
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(958, 493)  # Cunning Rivalry Cloak

    for x in range(9):
        pyautogui.leftClick()
        pyautogui.mouseDown(button='left')
        time.sleep(3.6)
        pyautogui.mouseUp(button='left')

    keyboard.press_and_release('esc')
    time.sleep(0.7)
    keyboard.press_and_release('d')
    time.sleep(0.5)
    keyboard.press_and_release('d')
    time.sleep(0.5)

    pyautogui.moveTo(1848, 1011)
    time.sleep(0.3)
    pyautogui.moveTo(2007, 1017)

    for x in range(9):
        keyboard.press_and_release('f')
        keyboard.press('f')
        time.sleep(1.5)
        keyboard.release('f')
        time.sleep(0.1)


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
