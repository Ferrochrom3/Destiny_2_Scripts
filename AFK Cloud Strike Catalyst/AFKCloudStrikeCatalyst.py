import pyautogui
import time
import keyboard
import autoit
import sys
import threading

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Void Warlock
Abilities    : Healing Rift
Fragments    : Echo of Persistence
Aspects      : Feed the Void
Weapons      : Kinetic - Any SMG
               Energy  - Sniper
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
        try:
            x, y = pyautogui.locateCenterOnScreen("0 Ammo.png", confidence=0.8,
                                                  region=(408, 1180, 812, 1377))
            print("Out of Sniper Ammo")
            if not run:
                break
            keyboard.send('1')  # swap to kinetic
            if not run:
                break
            time.sleep(1)
            if not run:
                break
            print("Place a rift")
            if not run:
                break
            keyboard.send('v')  # place rift
            if not run:
                break
            time.sleep(2.3)
            if not run:
                break
            print("Crouch")
            if not run:
                break
            keyboard.send('\\')  # press to crouch
            if not run:
                break
            print("Look down slightly")
            if not run:
                break
            autoit.mouse_move(0, 0, 1)
            if not run:
                break
            time.sleep(0.01)
            if not run:
                break
            autoit.mouse_move(0, 510, 1)
            if not run:
                break

            for x in range(25):  # repeat SMG firing for 50 times to get some special ammo
                pyautogui.mouseDown(button='left')
                time.sleep(0.7)
                pyautogui.mouseUp(button='left')
                if not run:
                    break
                time.sleep(2)
                if not run:
                    break
                keyboard.send('s')
                time.sleep(0.1)

            keyboard.send('2')  # swap back to energy
            if not run:
                break
            time.sleep(4.5)
            if not run:
                break

        except TypeError:
            for x in range(3):
                if not run:
                    break
                global sniperShotsCounter
                print("Shoot Sniper", sniperShotsCounter)
                if not run:
                    break
                pyautogui.leftClick()
                if not run:
                    break
                time.sleep(1)
                if not run:
                    break
                print("Look down slightly to combat the sniper kick")
                if not run:
                    break
                autoit.mouse_move(0, 100, 1)
                if not run:
                    break
                time.sleep(0.01)
                if not run:
                    break
                autoit.mouse_move(0, 265, 1)
                if not run:
                    break
                print("Move a step back to prevent inactivity")
                if not run:
                    break
                keyboard.send('s')
                time.sleep(0.1)
                if not run:
                    break
                sniperShotsCounter = sniperShotsCounter + 1
                if not run:
                    break
            keyboard.send('r')
            if not run:
                break
            print("Reload")
            if not run:
                break
            time.sleep(3.5)
            if not run:
                break
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

