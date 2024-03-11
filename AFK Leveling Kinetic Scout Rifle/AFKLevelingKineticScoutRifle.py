import sys
import threading
import time
import keyboard
import pyautogui

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Any Void Subclass
Abilities    : Any
Fragments    : Echo of Starvation, Echo of Persistance
Aspects      : Any
Weapons      : Kinetic - Any Scout Rifle
               Energy  - Any
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - Kinetic Siphon
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
"""

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
startTime = time.time()


def my_function():
    global run
    run = True

    while run:
        pyautogui.leftClick()
        time.sleep(1)
        keyboard.send('s')
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
