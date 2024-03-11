import pyautogui
import time
import keyboard
import sys
import threading

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to Exit\n")
run = True
startTime = time.time()


def copy_and_paste():
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press('ctrl + v')
    time.sleep(0.3)
    keyboard.press_and_release('enter')

    while True:
        if pyautogui.locateOnScreen("Error Code Exclamation Mark.png", confidence=0.8, grayscale=True):
            keyboard.press_and_release('enter')
            time.sleep(1)
            break
        if pyautogui.locateOnScreen("Joining Fireteam.png", confidence=0.8, grayscale=True):
            print("Joining...")

            while True:
                if not pyautogui.locateOnScreen("Joining Fireteam.png", confidence=0.8, grayscale=True):
                    break


def afk():
    global run
    run = True
    while run:
        print("============================")
        for x in range(6):
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


def stop_afk():
    global run
    run = False
    print("Execution Stopped")


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.add_hotkey('f8', stop_afk)
    keyboard.wait('f9')
    keyboard.release('ctrl + v')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
