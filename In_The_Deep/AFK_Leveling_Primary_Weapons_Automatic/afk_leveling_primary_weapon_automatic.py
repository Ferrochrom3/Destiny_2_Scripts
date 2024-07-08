import pyautogui
import time
import keyboard
import sys
import threading

"""
Location     : "In The Deep" - Shadowkeep Campaign - Step 10
Subclass     : Any Void Subclass
Abilities    : Any
Fragments    : Echo of Starvation, Echo of Persistance
Aspects      : Any
Weapons      : Kinetic - *Check "Additional Notes"
               Energy  - *Check "Additional Notes"
               Power   - Any
Exotic Armor : Any
Mods         : Helmet     - *Check "Additional Notes"
               Arms       - Any
               Chest      - Any
               Leg        - Any
               Class Item - Any
Stats        : Any
Reward       : XP

Additional Notes:
 - Use either a Kinetic or Energy automatic Primary weapon (Auto Rifles or Submachine Guns).
 - Use a Siphon mod cooresponding to your weapon's element on the helmet.
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")


def afk():
    while True:
        pyautogui.mouseDown(button="left")
        time.sleep(0.7)
        pyautogui.mouseUp(button="left")
        time.sleep(2)
        keyboard.press_and_release("s")
        time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=afk)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    sys.exit()
