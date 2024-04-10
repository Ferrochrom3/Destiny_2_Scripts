import pyautogui
import time
import keyboard
import sys
import threading

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Any Void Subclass
Abilities    : Any
Fragments    : Echo of Starvation, Echo of Persistance
Aspects      : Any
Weapons      : Kinetic - Osteo Striga
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
print("Press F9 to Exit\n")
run = False
execution_stopped = False
startTime = time.time()


def afk():
    global run
    global execution_stopped
    run = True
    execution_stopped = False

    while run:
        pyautogui.mouseDown(button='left')
        time.sleep(0.7)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        keyboard.send('s')
        time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=afk)
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
