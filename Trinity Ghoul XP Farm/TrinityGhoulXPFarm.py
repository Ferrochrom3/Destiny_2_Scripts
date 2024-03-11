import pyautogui
import time
import keyboard
import sys
import threading

pyautogui.FAILSAFE = False

"""
Location     : 
Subclass     : 
Abilities    : 
Fragments    : 
Aspects      : 
Weapons      : Kinetic - 
               Energy  - 
               Power   - 
Exotic Armor : 
Mods         : Helmet     - 
               Arms       - 
               Chest      - 
               Leg        - 
               Class Item - 
Stats        : 
Reward       :

"""

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")
run = True
startTime = time.time()


def afk():
    global run
    run = True
    while run:
        pyautogui.leftClick()
        time.sleep(4)
        keyboard.press_and_release('s')


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
