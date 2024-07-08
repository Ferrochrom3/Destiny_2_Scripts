import pyautogui
import time
import keyboard
import sys
import pydirectinput
import threading
import win32con
import win32api

activity_type = ""
activity_name = ""
startTime = time.time()
run = True
pyautogui.FAILSAFE = False

root_of_nightmare_boss_triggered = False


def begin_instruction():
    global activity_type
    global activity_name

    print("\nWhat type of activity are you trying to access?")
    print("1 For Dungeon")
    print("2 For Raid")
    activity_type = input()

    if activity_type == "1":  # dungeons
        print("\nWhat is the dungeon?")
        print("1 For Shattered Throne")
        print("2 For Pit of Heresy")
        print("3 For Prophecy")
        print("4 For Grasp of Avarice")
        print("5 For Duality")
        print("6 For Spire of the Watcher")
        activity_name = input()

        print("Press F7 to Start")
        print("Press F8 to Stop")
        print("Press F9 to Exit")

    elif activity_type == "2":  # raids
        print("\nWhat is the raid?")
        print("1 For Root of Nightmare")
        print("2 For Last Wish")
        activity_name = input()

        print("Press F7 to Start")
        print("Press F8 to Stop")
        print("Press F9 to Exit")

    else:
        print("===ERROR: Invalid Activity Type Number===")
        begin_instruction()


begin_instruction()


def afk():
    global run
    run = True

    while True:
        global activity_type
        global activity_name

        if activity_type == "1":  # if activity type is dungeon
            if activity_name == "1":
                player_joins()
                shattered_throne()

            elif activity_name == "2":
                player_joins()
                pit_of_heresy()

            elif activity_name == "3":
                player_joins()
                prophecy()

            elif activity_name == "4":
                player_joins()
                grasp_of_avarice()

            elif activity_name == "5":
                player_joins()
                duality()

            elif activity_name == "6":
                player_joins()
                spire_of_the_watcher()

            else:
                print("===ERROR: Invalid Activity Name Number===")
                stop_afk()
                begin_instruction()
                break

        elif activity_type == "2":  # if the activity type is raid
            if activity_name == "1":
                player_joins()
                root_of_nightmare()

            elif activity_name == "2":
                player_joins()
                last_wish()

            else:
                print("===ERROR: Invalid Activity Name Number===")
                stop_afk()
                begin_instruction()
                break


def start_afk():
    t = threading.Thread(target=afk)
    print("\nExecution Started")
    t.start()


def stop_afk():
    global run
    run = False
    print("Execution Stopped")


def player_joins():
    global root_of_nightmare_boss_triggered
    keyboard.press_and_release('alt')
    try:
        x, y = pyautogui.locateCenterOnScreen("Player Joined.png", confidence=0.8)
        root_of_nightmare_boss_triggered = False  # set trigger back to false once a play joins
        print("\nPlayer Joined")
        time.sleep(8)
        keyboard.press_and_release('esc')
        time.sleep(1)
        pyautogui.moveTo(682, 598)  # change character
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(745, 648)  # confirm
        pyautogui.click()
        time.sleep(6)
    except TypeError:
        print("---No Player Joined")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Titan.png", confidence=0.8)
        print("Select Titan")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
    except TypeError:
        print("---No Titan Found")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Open Director.png", confidence=0.8)
        print("Open Director")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.leftClick()
    except TypeError:
        print("---No Director Found")
        pass


def shattered_throne():
    try:
        x, y = pyautogui.locateCenterOnScreen("Dreaming City.png", confidence=0.8)
        print("Open Dreaming City")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pydirectinput.moveTo(None, -300)  # move mouse cursor up
        time.sleep(1)
    except TypeError:
        print("---No Dreaming City Found")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
        print("Open Shattered Throne Dungeon")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(1633, 897)  # launch
        pyautogui.click()
    except TypeError:
        print("---No Dungeon Icon Found")
        pass


def pit_of_heresy():
    try:
        x, y = pyautogui.locateCenterOnScreen("Moon.png", confidence=0.8)
        print("Open The Moon")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        pyautogui.moveTo(917, 779)
        time.sleep(1)
        pydirectinput.moveTo(None, -300)  # move mouse cursor up
        time.sleep(1)
    except TypeError:
        print("---No Moon Found")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
        print("Open Pit of Heresy Dungeon")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(1633, 897)  # launch
        pyautogui.click()
    except TypeError:
        print("---No Dungeon Icon Found")
        pass


def prophecy():
    try:
        print("Work in Progress")
    except TypeError:
        pass


def grasp_of_avarice():
    try:
        print("Work in Progress")
    except TypeError:
        pass


def duality():
    try:
        x, y = pyautogui.locateCenterOnScreen("Moon.png", confidence=0.8)
        print("Open The Moon")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        pyautogui.moveTo(917, 779)
        time.sleep(1)
        pydirectinput.moveTo(-500, 2000)  # move mouse cursor left
        time.sleep(1)
        pydirectinput.moveTo(0, 500)  # move mouse cursor down
        time.sleep(1)
    except TypeError:
        print("---No Moon Found")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
        print("Open Duality Dungeon")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)

        # pyautogui.moveTo(1468, 832)  # move to difficulty
        # time.sleep(0.1)
        # pyautogui.leftClick()
        # time.sleep(1.5)
        #
        # pyautogui.moveTo(216, 344)  # move to master
        # time.sleep(0.1)
        # pyautogui.leftClick()
        # time.sleep(0.5)

        pyautogui.moveTo(1633, 897)  # launch
        time.sleep(0.1)
        pyautogui.click()
    except TypeError:
        print("---No Dungeon Icon Found")
        pass


def spire_of_the_watcher():
    try:
        print("Work in Progress")
    except TypeError:
        pass


def root_of_nightmare():
    global root_of_nightmare_boss_triggered

    try:
        x, y = pyautogui.locateCenterOnScreen("Neptune.png", confidence=0.8)
        print("Open Neptune")
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1.2)
    except TypeError:
        print("---No Neptune Found")
        pass

    pyautogui.moveTo(0, 0)
    time.sleep(1)

    try:
        x, y = pyautogui.locateCenterOnScreen("Root of Nightmare.png", confidence=0.8)
        print("Open Root of Nightmare")
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("---No Root of Nightmare Found")
        pass

    time.sleep(0.7)

    try:
        x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.8, grayscale=True)
        print("Launch")
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("---No Launch Button Found")
        pass

    if pyautogui.locateOnScreen("In Root of Nightmare.png", confidence=0.7, grayscale=True) \
            and not root_of_nightmare_boss_triggered:
        print("Run toward Nesarec")
        keyboard.press('d')
        time.sleep(1.3)
        keyboard.release('d')
        keyboard.press('left shift+w')
        time.sleep(6)
        keyboard.release('left shift+w')
        root_of_nightmare_boss_triggered = True


def last_wish():
    try:
        x, y = pyautogui.locateCenterOnScreen("Dreaming City.png", confidence=0.8)
        print("Open Dreaming City")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pydirectinput.moveTo(None, -300)  # move mouse cursor up
        time.sleep(1)
    except TypeError:
        print("---No Dreaming City Found")
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen("Last Wish.png", confidence=0.8)
        print("Open Last Wish")
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(1633, 897)  # launch
        pyautogui.click()
    except TypeError:
        print("---No Last Wish Found Icon Found")
        pass


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.add_hotkey('f8', stop_afk)
    keyboard.wait('f9')
    keyboard.release('d')
    keyboard.release('left shift+w')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds = "
             + str(round((time.time() - startTime) / 60, 1)) + " minutes = "
             + str(round((time.time() - startTime) / 3600, 1)) + " hours")
