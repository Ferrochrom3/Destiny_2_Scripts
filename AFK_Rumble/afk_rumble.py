import pyautogui
import keyboard
import sys
import threading
import time
from colorama import Fore, Style

"""
Location     : Crucible Rumble
Subclass     : Stasis Warlock
Abilities    : Coldsnap Grenade
Fragments    : Whisper of Durance
Aspects      : Bleak Watcher
Weapons      : Kinetic - Witherhoard
               Energy  - Any Primary
               Power   - Any
Exotic Armor : Osmiomancy Gloves
Mods         : Helmet     - Any
               Arms       - 2x Bolstering Detonation
               Chest      - Any
               Leg        - Any
               Class Item - 2x Bomber
Stats        : Max Discipline
Reward       : Some Crucible reputations, some legendary gears
"""

print("Minimum of 1 assist is needed to gain reputation")
print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

start_time = time.time()
image_path = "Destiny 2 Scripts/AFK Rumble"


def afk():
    while True:
        if pyautogui.locateOnScreen(f"{image_path}\Broccoli Error.png", confidence=0.8):
            broccoli_error_solution()

        if pyautogui.locateOnScreen(f"{image_path}\Match Results.png", confidence=0.6):
            relaunch_after_match_completed()

        if pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 Desktop Icon.png", grayscale=True, confidence=0.8):
            broccoli_error_solution()
            print("Wait 60 Second For Destiny 2 to Launch")
            time.sleep(60)

        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Warlock.png", confidence=0.6)
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
            time.sleep(3.5)
        except TypeError:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Open Director.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Crucible.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Rumble.png", confidence=0.7)
            pyautogui.moveTo(x, y)
            time.sleep(1)
            pyautogui.leftClick()
            time.sleep(1.2)
        except TypeError:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Launch.png", confidence=0.7)
            pyautogui.moveTo(x, y)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            pass

        if pyautogui.locateOnScreen(f"{image_path}\Coldsnap Grenade.png", confidence=0.8):
            keyboard.press("q")
            time.sleep(2.3)
            keyboard.release("q")
            time.sleep(1)

        if pyautogui.locateOnScreen(f"{image_path}\Rift.png", confidence=0.8):
            keyboard.send("v")
            time.sleep(2.5)

        if pyautogui.locateOnScreen(f"{image_path}\Witherhoard Icon.png", grayscale=True, confidence=0.8):
            pyautogui.leftClick(200, 200)
            time.sleep(2.3)
            keyboard.send("s")  # move back to prevent inactivity
            time.sleep(0.1)
            keyboard.send("c")  # melee
            time.sleep(1.3)

        keyboard.press_and_release("enter")
        time.sleep(0.1)
        keyboard.press_and_release("enter")
        time.sleep(0.1)
        keyboard.press_and_release("l")
        time.sleep(0.1)
        keyboard.press_and_release("1")
        time.sleep(2)
        pyautogui.leftClick()


def relaunch_after_match_completed():
    keyboard.send("m")
    time.sleep(2)

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Crucible.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()
        time.sleep(1.5)
    except TypeError:
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Rumble.png", confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()
        time.sleep(1.5)
    except TypeError:
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Launch.png", confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()
        time.sleep(1.5)
    except TypeError:
        pass


def broccoli_error_solution():
    print("Broccoli Error")
    time.sleep(0.1)
    keyboard.send("alt+f4")  # close destiny 2
    time.sleep(2)
    keyboard.send("ctrl+shift+esc")  # open task manager
    time.sleep(6)

    if pyautogui.locateOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8):
        end_destiny2()
    else:
        print("No Destiny 2 Found In Task Manager")
        print("Finding Destiny 2")
        try:
            x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Memory.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            time.sleep(2)
            for x in range(25):
                pyautogui.scroll(-1200)
                time.sleep(1)
                if pyautogui.locateOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8):
                    end_destiny2()
                    time.sleep(0.5)
        except TypeError:
            pass

    keyboard.send("alt+f4")  # close task manager
    time.sleep(2)
    keyboard.send("win+d")
    print("Open Destiny 2 on Desktop")
    time.sleep(2)
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 Desktop Icon.png", grayscale=True, confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(0.5)
        pyautogui.click(x, y, clicks=3)
    except TypeError:
        pass


def end_destiny2():
    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\Destiny 2 In Task Manager.png", confidence=0.8)
    print("Found Destiny 2 In Task Manager")
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}\End Task.png", confidence=0.8)
    print("End Task")
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()


def start_afk():
    t = threading.Thread(target=afk)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    Fore.RED +
    f"Elapsed Time: {round(time.time() - start_time)} seconds | "
    f"{round((time.time() - start_time) / 60, 2)} minutes | "
    f"{round((time.time() - start_time) / 3600, 2)} hours" + Style.RESET_ALL)
    # fmt: on
