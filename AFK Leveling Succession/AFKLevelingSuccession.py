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
Reward       : small XP, small Neutral Element
"""

print("Execution will not stop until for loop is finished looping")
print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")
run = True
sniperShotsCounter = 1


def afk():
    global run
    run = True
    while run:
        if pyautogui.locateCenterOnScreen("0 Ammo.png", confidence=0.9, grayscale=True, region=(609, 1218, 707, 1280)):
            print("Out of Sniper Ammo")
            keyboard.send('2')  # swap to energy
            time.sleep(1)
            print("Place a rift")
            keyboard.send('v')  # place rift
            time.sleep(2.3)
            print("Crouch")
            keyboard.send('\\')  # press to crouch
            print("Look down slightly")
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 510, 0, 0)

            for x in range(50):  # shoot 50 arrows to get some special ammo
                pyautogui.leftClick()
                time.sleep(0.9)

            keyboard.send('1')  # swap back to kinetic
            time.sleep(4.5)

        else:
            for x in range(3):
                pyautogui.leftClick()
                time.sleep(1)
                print("Look down slightly to combat the sniper kick")
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 30, 0, 0)
                print("Move a step back to prevent inactivity")
                keyboard.send('s')  # have time.sleep() on the next line to prevent infinite press
                time.sleep(0.1)

            keyboard.send('r')
            print("Reload")
            time.sleep(3.5)
            pass


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
