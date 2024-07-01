import pyautogui
import time
import keyboard
import sys
import threading
import win32api
import win32con

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Void Warlock
Abilities    : Healing Rift
Fragments    : Echo of Persistence
Aspects      : Feed the Void
Weapons      : Kinetic - Sniper
               Energy  - Under Your Skin (Explosive Payload)
               Power   - Any
Exotic Armor : Sanguine Alchemy
Mods         : Helmet     - Sniper Finder
               Arms       - Any
               Chest      - Melee Resist
               Leg        - Sniper Scavenger
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
        if pyautogui.locateCenterOnScreen("0 Ammo.png", confidence=0.9, grayscale=True, region=(609, 1218, 707, 1280)):
            use_primary()

        else:
            use_succession()


def use_primary():
    keyboard.press_and_release("2")  # Swap to Energy
    time.sleep(1)
    print("Place a rift")
    keyboard.press_and_release("v")  # Place rift
    time.sleep(2.3)
    print("Crouch")
    keyboard.press_and_release("e")  # Press to crouch
    print("Look down slightly")
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 510, 0, 0)

    # Shoot 50 arrows to get some special ammo
    for _ in range(50):
        pyautogui.leftClick()
        time.sleep(0.9)

    keyboard.press_and_release("1")  # Swap back to Kinetic
    time.sleep(4.5)


def use_succession():
    for _ in range(3):
        pyautogui.leftClick()
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 85, 0, 0)  # Look down slightly to combat the sniper kick
        keyboard.press_and_release("s")
        time.sleep(0.1)

    keyboard.press_and_release("r")
    time.sleep(3.5)


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
