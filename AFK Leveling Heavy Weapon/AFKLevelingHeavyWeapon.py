import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con

"""
Location     : "Investigation Mission" - Witch Queen Campaign - 2nd Mission
Subclass     : Any
Abilities    : Any
Fragments    : Any
Aspects      : Any
Weapons      : Kinetic - Mountain Top
               Energy  - Any
               Power   - Any weapon to level up, Eyes of Tomorrow
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : small XP, small Neutral Elements, some engrams
"""

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
pyautogui.FAILSAFE = False
startTime = time.time()


def afk():
    global run
    run = True

    while run:
        if pyautogui.locateCenterOnScreen("Grenade Launcher Icon.png", grayscale=True, confidence=0.8):
            keyboard.press_and_release('3')
            time.sleep(2)

        if not pyautogui.locateCenterOnScreen("Eyes of Tomorrow Icon.png", grayscale=True, confidence=0.8):
            equip_eyes_of_tomorrow()

        keyboard.press('a')  # move left
        time.sleep(0.5)
        keyboard.release('a')

        keyboard.press('left shift+w')  # sprint forward
        time.sleep(2.6)
        keyboard.release('left shift+w')

        keyboard.press('alt')  # place down rally banner
        time.sleep(1.1)
        keyboard.release('alt')
        time.sleep(2.2)

        keyboard.press('w')  # walk forward slightly
        time.sleep(0.3)
        keyboard.release('w')

        keyboard.send('r')  # reload
        time.sleep(2.3)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 100, 0, 0)
        pyautogui.mouseDown(button='right')  # aim eyes of tomorrow at enemies
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1000, 0, 0)  # look all the way up
        pyautogui.leftClick()  # shoot
        time.sleep(1)
        pyautogui.mouseUp(button='right')

        keyboard.press_and_release('f1')  # open inventory
        time.sleep(1.5)
        x, y = pyautogui.locateCenterOnScreen("Eyes of Tomorrow.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        pyautogui.moveTo(555, 845)  # move to 1st weapon on the left
        pyautogui.leftClick()  # swap weapon
        keyboard.press_and_release('f1')  # close inventory
        time.sleep(2)

        keyboard.press_and_release('1')  # pull out mountain top
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 2000, 0, 0)  # look all the way down
        time.sleep(3)
        pyautogui.leftClick()  # shoot
        keyboard.press_and_release('r')  # reload
        time.sleep(2.5)
        pyautogui.leftClick()  # shoot a second shot to kill

        keyboard.press_and_release('f1')  # open inventory
        time.sleep(1.5)
        pyautogui.moveTo(x, y)  # move to heavy weapon slot
        pyautogui.moveTo(555, 845)  # move to 1st weapon on the left
        pyautogui.leftClick()  # swap back to eyes of tomorrow
        keyboard.press_and_release('f1')  # close inventory

        while True:
            if pyautogui.locateCenterOnScreen("Grenade Launcher Icon.png", grayscale=True, confidence=0.8) or \
                    pyautogui.locateCenterOnScreen("Eyes of Tomorrow Icon.png", grayscale=True, confidence=0.8):
                break


def equip_eyes_of_tomorrow():
    keyboard.press_and_release('f1')  # open inventory
    time.sleep(2)

    if not pyautogui.locateOnScreen("Eyes of Tomorrow.png", confidence=0.8):
        pyautogui.moveTo(694, 845)  # move to heavy weapon slot
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen("Eyes of Tomorrow.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()

    keyboard.press_and_release('f1')  # close inventory
    time.sleep(1.2)
    keyboard.press_and_release('3')  # swap to heavy
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
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
