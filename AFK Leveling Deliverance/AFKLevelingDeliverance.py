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
Weapons      : Kinetic - Fusion Rifle
               Energy  - Under Your Skin (Explosive Head)
               Power   - Any
Exotic Armor : Sanguine Alchemy
Mods         : Helmet     - Fusion Rifle Finder
               Arms       - Any
               Chest      - Heavy Handed (Secondary Perk Active)
               Leg        - Fusion Rifle Scavenger
               Class Item - Any
Stats        : Any
Reward       : small XP, small Neutral Element
         
"""

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")
run = True


def afk():
    global run
    run = True
    while run:
        a = 1
        for x in range(100):  # shoot_wall( 100 fusion shots
            if not run:
                break
            if a == 1:
                print(a, "Fusion Shot")
            else:
                print(a, "Fusion Shots")
            pyautogui.mouseDown(button='left')
            if not run:
                break
            time.sleep(0.9)
            if not run:
                break
            pyautogui.mouseUp(button='left')
            if not run:
                break
            time.sleep(4)
            if not run:
                break
            print("Move one step back")
            if not run:
                break
            keyboard.send('s')  # move a step back to prevent inactivity
            if not run:
                break
            time.sleep(0.1)
            if not run:
                break
            a = a + 1

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
        autoit.mouse_move(0, 500, 1)
        if not run:
            break


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
