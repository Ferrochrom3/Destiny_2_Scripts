import pyautogui
import time
import keyboard
import sys
import threading

pyautogui.FAILSAFE = False

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Void Warlock
Abilities    : Healing Rift
Fragments    : Echo of Persistence
Aspects      : Feed the Void
Weapons      : Kinetic - Any
               Energy  - Trinity Ghoul
               Power   - Any
Exotic Armor : Sanguine Alchemy
Mods         : Helmet     - Any
               Arms       - Any
               Chest      - Melee Resist
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
        time.sleep(4)
        keyboard.press_and_release("s")


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
