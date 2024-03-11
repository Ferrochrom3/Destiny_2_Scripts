import sys
import threading
import time
import keyboard
import pyautogui

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
execution_stopped = False
startTime = time.time()


def my_function():
    global run
    global execution_stopped
    run = True
    execution_stopped = False

    while run:
        print("Checking GameHeader")
        while True:
            check_for_error()
            if pyautogui.locateOnScreen("GameHeader.png", confidence=0.8):
                print("GameHeader Found")
                time.sleep(1.1)
                x, y = pyautogui.locateCenterOnScreen("GameHeader.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        print("Checking CheckmarkButton")
        while True:
            if pyautogui.locateOnScreen("CheckmarkButton.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("CheckmarkButton.png", confidence=0.8)
                print("CheckmarkButton Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(1.1)
                pyautogui.leftClick()
                break

        print("Checking Map")
        while True:
            check_for_error()
            if pyautogui.locateOnScreen("Map.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("Map.png", confidence=0.8)
                print("Map Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        print("Checking Exit")
        while True:
            if pyautogui.locateOnScreen("Exit.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("Exit.png", confidence=0.8)
                print("Exit Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        keyboard.press('a')
        time.sleep(0.3)
        keyboard.release('a')

        print("Checking ShieldThrowAbility")
        while True:
            if pyautogui.locateOnScreen("ShieldThrowAbility.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("ShieldThrowAbility.png", confidence=0.8)
                print("ShieldThrowAbility Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                for x in range(10):
                    if pyautogui.locateOnScreen("Coin.png", confidence=0.8):
                        print("Coin Found, Exiting...")
                        break
                    pyautogui.leftClick()
                    time.sleep(0.5)
                break

        print("Checking WarliegeClass")
        while True:
            if pyautogui.locateOnScreen("WarliegeClass.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("WarliegeClass.png", confidence=0.8)
                print("WarliegeClass Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        print("Checking Setting")
        while True:
            if pyautogui.locateOnScreen("Setting.png", confidence=0.9):
                x, y = pyautogui.locateCenterOnScreen("Setting.png", confidence=0.9)
                print("Setting Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        print("Checking BackToMain")
        while True:
            if pyautogui.locateOnScreen("BackToMain.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("BackToMain.png", confidence=0.8)
                print("BackToMain Found")
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break


def check_for_error():
    if pyautogui.locateOnScreen("ErrorMessage.png", confidence=0.8):
        print("ErrorMessage")
        pyautogui.moveTo(1115, 839)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(2)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


def stop_afk():
    global run
    global execution_stopped
    run = False
    execution_stopped = True
    print("Execution will stop after the current iteration")


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.add_hotkey('f8', stop_afk)
    keyboard.wait('f9')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")