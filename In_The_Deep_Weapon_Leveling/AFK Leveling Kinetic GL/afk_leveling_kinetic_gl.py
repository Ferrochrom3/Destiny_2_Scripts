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
Weapons      : Kinetic - Grenade Launcher (with Disorenting Grenade)
               Energy  - Sunshot
               Power   - Any
Exotic Armor : Sanguine Alchemy
Mods         : Helmet     - Special Ammo Finder
               Arms       - Any
               Chest      - Melee Resist
               Leg        - Kinetic Scavenger
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
            use_grenade_launcher()


def use_primary():
    keyboard.press_and_release("2")  # Swap to Energy
    time.sleep(1)
    keyboard.press_and_release("v")  # Place rift
    time.sleep(2.3)
    keyboard.press_and_release("e")  # Press to crouch
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 510, 0, 0)  # Look down slightly after using a rift

    # Shoot 30 Sunshot shots to get some special ammo
    for _ in range(30):
        pyautogui.leftClick()
        time.sleep(3)

    keyboard.press_and_release("1")  # Swap back to Kinetic
    time.sleep(4.5)


def use_grenade_launcher():
    pyautogui.leftClick()
    time.sleep(1)
    keyboard.press_and_release("s")
    time.sleep(0.1)
    keyboard.press_and_release("r")  # Reload
    time.sleep(5)


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
