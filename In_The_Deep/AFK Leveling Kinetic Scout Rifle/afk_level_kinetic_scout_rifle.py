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
print("Press F8 to Exit\n")

run = False
start_time = time.time()


def my_function():
    run = True

    while run:
        pyautogui.leftClick()
        time.sleep(1)
        keyboard.press_and_release("s")
        time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    f"Elapsed Time: {round(time.time() - start_time)} seconds"
    f"\n{round((time.time() - start_time) / 60, 2)} minutes"
    f"\n{round((time.time() - start_time) / 3600, 2)} hours")
    # fmt: on
