import pyautogui
import time
import keyboard
import sys
import threading

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Void
Abilities    : Any
Fragments    : Echo of Starvation, Echo of Persistance
Aspects      : Any
Weapons      : Kinetic - Any
               Energy  - Bow
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - An elemental Siphon that matches your weapon type
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : Some XP, some Neutral Elements
"""

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")
run = True


def afk():
    global run
    run = True
    x = 1
    while run:
        print("Shoot", x)
        pyautogui.leftClick()
        time.sleep(0.9)
        x = x + 1


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
    sys.exit()
