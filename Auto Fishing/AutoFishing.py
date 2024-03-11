import sys
import threading
import time
import keyboard
import pyautogui

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
execution_stopped = False
startTime = time.time()

perfect_catch = 0
total_fish = 0
total_time = 0


def my_function():
    global run
    global execution_stopped
    global perfect_catch
    global total_fish
    global total_time
    run = True
    execution_stopped = False

    while run:
        if pyautogui.locateOnScreen("Alt.png", grayscale=True, confidence=0.7, region=(893, 830, 1751, 1134)):
            keyboard.press('alt')
            time.sleep(1)
            keyboard.release('alt')
            total_time += 1

            while True:
                if pyautogui.locateOnScreen("Alt.png", grayscale=True, confidence=0.7):  # region=(893, 830, 1751, 1134)
                    keyboard.press('alt')
                    keyboard.release('alt')
                    time.sleep(2)
                    print("You Fished " + str(total_time) + " Times")
                    break
        else:
            time.sleep(1)
            keyboard.press_and_release('w')
            time.sleep(0.5)
            keyboard.press_and_release('s')

        if execution_stopped:
            print("Execution Stopped")


def start_afk():
    t = threading.Thread(target=my_function)
    print("Execution Started")
    t.start()


def stop_afk():
    global run
    global execution_stopped
    run = False
    execution_stopped = True
    print("Execution will stop after the current iteration")


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.add_hotkey('f8', stop_afk)
    keyboard.wait('f9')
    keyboard.release('alt')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
