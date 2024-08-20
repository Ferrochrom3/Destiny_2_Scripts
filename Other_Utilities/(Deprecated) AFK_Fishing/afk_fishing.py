import sys
import threading
import time
import keyboard
import pyautogui

print("Press F7 to Start")
print("Press F8 to Exit\n")


def my_function():
    total_time = 0

    while True:
        # Cast a pole if "Alt" button shows up on screen
        if pyautogui.locateOnScreen("Alt.png", grayscale=True, confidence=0.7, region=(893, 830, 1751, 1134)):
            keyboard.press("alt")
            time.sleep(1)
            keyboard.release("alt")
            total_time += 1

            # Waiting for a fishing to get caught
            while True:
                if pyautogui.locateOnScreen("Alt.png", grayscale=True, confidence=0.7):  # region=(893, 830, 1751, 1134)
                    keyboard.press("alt")
                    keyboard.release("alt")
                    time.sleep(2)
                    print("You Fished " + str(total_time) + " Times")
                    break

        # Otherwise move forward and back slightly to prevent afk kick
        else:
            time.sleep(1)
            keyboard.press_and_release("w")
            time.sleep(0.5)
            keyboard.press_and_release("s")


def start_afk():
    t = threading.Thread(target=my_function)
    print("Execution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    sys.exit()
