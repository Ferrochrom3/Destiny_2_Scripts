import pyautogui
import time
import keyboard
import sys
import threading

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")

image_path = "Destiny_2_Scripts/Spam_Join"


def copy_and_paste():
    keyboard.press_and_release("enter")
    time.sleep(0.3)
    keyboard.press("ctrl + v")
    time.sleep(0.3)
    keyboard.press_and_release("enter")

    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Error Code Exclamation Mark.png", confidence=0.8, grayscale=True):
            keyboard.press_and_release("enter")
            time.sleep(1)
            break

        if pyautogui.locateOnScreen(f"{image_path}/Joining Fireteam.png", confidence=0.8, grayscale=True):
            print("Joining...")

            while True:
                if not pyautogui.locateOnScreen(f"{image_path}/Joining Fireteam.png", confidence=0.8, grayscale=True):
                    break


def afk():
    while True:
        print("============================")
        for _ in range(6):
            copy_and_paste()

        print("First Timer - 3 Seconds")
        time.sleep(3)

        print("============================")
        copy_and_paste()

        print("Second Timer - 8 Seconds")
        time.sleep(8)

        print("============================")
        copy_and_paste()

        print("Third Timer - 15 Seconds")
        time.sleep(15)

        print("============================")
        copy_and_paste()

        print("Fourth Timer - 31 Seconds")
        time.sleep(31)


def start_afk():
    t = threading.Thread(target=afk)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("ctrl+v")
    sys.exit()
