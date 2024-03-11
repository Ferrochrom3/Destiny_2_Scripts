import pyautogui
import time
import keyboard
import sys
import threading

print("Press F7 to Start")
print("Press F8 to Stop (Only After the Current Iteration)")
print("Press F9 to Exit\n")
run = True
startTime = time.time()

pyautogui.FAILSAFE = False

adjustment_value = 156  # Adjust this coord accordingly

ikora_x_pos = 1541  # Adjust this coord accordingly
ikora_y_pos = 1006  # Adjust this coord accordingly

x_pos = 1856  # Adjust this coord accordingly
y_pos = 853  # Adjust this coord accordingly


def afk():
    global run
    run = True
    while run:
        pyautogui.moveTo(ikora_x_pos, ikora_y_pos)
        for x in range(9):
            pyautogui.leftClick()
            time.sleep(1.5)

        keyboard.press_and_release('f1')
        time.sleep(1)
        pyautogui.moveTo(x_pos, y_pos)
        time.sleep(1)

        pyautogui.moveTo(x_pos + adjustment_value, y_pos)
        time.sleep(1)
        for x in range(9):
            keyboard.press_and_release('f')
            keyboard.press('f')
            time.sleep(4.2)
            keyboard.release('f')
            time.sleep(0.5)

        keyboard.press_and_release('esc')
        time.sleep(4)


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
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds = "
             + str(round((time.time() - startTime) / 60, 1)) + " minutes = "
             + str(round((time.time() - startTime) / 3600, 1)) + " hours")