import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con

# ***Need all imports, opencv-python, and Pillow***

# print(pyautogui.position())                print current mouse cursor location
# time.sleep()                               delay x seconds

# pyautogui.click()                          click (x, y)
# pyautogui.click(clicks=3, interval=0.1)    click once every 0.1 seconds for 3 times
# pyautogui.mouseDown(button='left')         hold down left mouse button
# pyautogui.mouseUp(button='left')           release left mouse button
# pyautogui.moveTo(x, y, duration=1)         move mouse to (x, y) taking a total of 1 second
# pyautogui.moveRel(100, 100, duration=1)    move mouse by (x, y) from the current position taking a total of 1 second

# pyautogui.press()                          press a key like 'a'
# pyautogui.keyDown('ctrl')                  hold down ctrl
# pyautogui.keyUp('ctrl')                    release ctrl

# keyboard.is_pressed('a')                   check if 'a' is pressed
# keyboard.press('a')                        hold down 'a'
# keyboard.release('a')                      release 'a'
# keyboard.send('a')                         press a (infinite), can also be used to press multiple keys like "alt+a"
# keyboard.press_and_release('a')
# use keyboard.press('a') -> keyboard.release('a') to prevent infinite 'a' or have a time.sleep() on the next line

# win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 100, 0, 0)
# move 100 pixels to the right and 100 pixels down relative to your current mouse position

#

# pyautogui.FAILSAFE = False                 remove mouse movement restrictions


print("Testing")
print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

run = False
execution_stopped = False
startTime = time.time()


def my_function():
    global run
    global execution_stopped
    run = True
    execution_stopped = False

    while run:
        print(pyautogui.position())
        break


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
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
    keyboard.release('shift')
    keyboard.release('w')
    keyboard.release('s')
    keyboard.release('ctrl')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
