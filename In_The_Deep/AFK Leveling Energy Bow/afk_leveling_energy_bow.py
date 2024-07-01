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
Reward       : XP
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")
run = True
start_time = time.time()


def afk():
    run = True

    while run:
        pyautogui.leftClick()
        time.sleep(0.9)


def start_afk():
    t = threading.Thread(target=afk)
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
