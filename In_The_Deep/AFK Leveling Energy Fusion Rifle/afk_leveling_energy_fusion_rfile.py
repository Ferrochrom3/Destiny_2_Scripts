import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con


"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Void Warlock
Abilities    : Healing Rift
Fragments    : Echo of Persistence
Aspects      : Feed the Void
Weapons      : Kinetic - Osteo Striga
               Energy  - Any Fusion Rifle
               Power   - Any
Exotic Armor : Sanguine Alchemy
Mods         : Helmet     - Special Ammo Finders
               Arms       - Any
               Chest      - Melee Resist
               Leg        - Scavenger, Holster
               Class Item - Any
Stats        : Any
Reward       : XP
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")

pyautogui.FAILSAFE = False

run = False
start_time = time.time()

fusion_rifle_charge_time = 0.6  # In seconds


def my_function():
    run = True

    while run:
        # If the weapon has 0 ammo, swap use primary to get some ammo
        if pyautogui.locateCenterOnScreen("0 Ammo.png", confidence=0.9, grayscale=True, region=(609, 1218, 707, 1280)):
            use_primary()

        # Other wise shoot fusion rilfe shots
        else:
            use_fusion_rifle()


def use_primary():
    keyboard.press_and_release("1")
    time.sleep(1)

    if pyautogui.locateOnScreen("Rift.png", confidence=0.8, grayscale=True, region=(333, 1228, 427, 1312)):
        keyboard.press_and_release("v")  # Place rift
        time.sleep(2.3)
        keyboard.press_and_release("\\")  # Press to crouch
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 500, 0, 0)  # Look down after placing a rift

    # Shoot 10 times to get some special ammo
    for _ in range(10):
        pyautogui.mouseDown(button="left")
        time.sleep(0.6)  # Hold Osteo down for 0.6s
        pyautogui.mouseUp(button="left")
        time.sleep(2)

    keyboard.press_and_release("2")
    time.sleep(2.5)


def use_fusion_rifle():
    if not pyautogui.locateOnScreen("Fusion Rifle Icon.png", confidence=0.9, grayscale=True, region=(429, 1222, 573, 1293)):
        keyboard.press_and_release("2")
        time.sleep(1.3)

    pyautogui.mouseDown(button="left")
    time.sleep(fusion_rifle_charge_time)
    pyautogui.mouseUp(button="left")
    time.sleep(1)
    keyboard.press_and_release("s")
    keyboard.press_and_release("r")
    time.sleep(2)


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
