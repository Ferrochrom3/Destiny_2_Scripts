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
Weapons      : Kinetic - Any
               Energy  - Indebted Kindness
               Power   - Parasite
Exotic Armor : Any
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : small XP, some engrams
"""

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
        # Wait until respawned
        while True:
            if pyautogui.locateOnScreen("Grapple Grenade.png", confidence=0.8):
                time.sleep(1)
                keyboard.press_and_release('3')
                break

        # Move left
        keyboard.press('a')
        time.sleep(0.4)
        keyboard.release('a')

        # Sprint forward
        keyboard.press('left shift+w')
        time.sleep(2.6)
        keyboard.release('left shift+w')

        # Place down rally banner
        keyboard.press('alt')
        time.sleep(1.1)
        keyboard.release('alt')
        time.sleep(2.2)

        # Sprint forward
        keyboard.press('left shift+w')
        time.sleep(3.2)
        keyboard.release('left shift+w')

        # Look up and shoot parasite
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -900, 0, 0)
        time.sleep(0.2)
        for i in range(3):
            pyautogui.leftClick()
            time.sleep(0.2)
            keyboard.press_and_release('r')
            time.sleep(3.5)

        # Suicide
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 4000, 0, 0)
        time.sleep(0.3)
        pyautogui.leftClick()  # Shoot Parasite
        time.sleep(0.2)
        keyboard.press_and_release('2')  # Swap to Indebted Kindness
        time.sleep(0.8)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()

        break


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
    keyboard.release('shift')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('ctrl')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")