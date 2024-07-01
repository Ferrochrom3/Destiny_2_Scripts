import pyautogui
import time
import keyboard
import threading

print("Press F7 to Start")
print("Press F8 to Exit\n")


def my_function():
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


def copy_and_paste():
    keyboard.press_and_release("enter")
    time.sleep(0.1)
    keyboard.press("ctrl+v")
    time.sleep(0.3)
    keyboard.press_and_release("enter")

    while True:
        if pyautogui.locateOnScreen("Error Code Exclamation Mark.png", confidence=0.8, grayscale=True):
            keyboard.press_and_release("enter")
            time.sleep(1)
            break

        if pyautogui.locateOnScreen("Joining Fireteam.png", confidence=0.8, grayscale=True):
            print("Joining...")

            while True:
                if not pyautogui.locateOnScreen("Joining Fireteam.png", confidence=0.8, grayscale=True):
                    break


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")
    keyboard.release("ctrl + v")
