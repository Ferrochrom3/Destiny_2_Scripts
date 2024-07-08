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

Additional Notes:
 - Use either a Kinetic or Energy single shot Primary weapon (Hand Cannon, Scout Rifle, Pulse Rifle, Sidearm, or Bow).
 - Use a Siphon mod cooresponding to your weapon's element on the helmet.
"""

print("Press F7 to Start")
print("Press F8 to Exit\n")


def my_function():
    while True:
        pyautogui.leftClick()
        time.sleep(0.8)
        keyboard.press_and_release("s")
        time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    sys.exit()
