"""
Performance (out of ~42 minutes):
 - Total Attempts: 49
 - Success Attempts: 8
 - Fail Attempts: 41
 - Success Rate: 16.3%
 - Average Time Per Attempt: 51.6s
 - Average Time Per Success: ~5.3 minutes
"""

import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from pynput.mouse import Button, Controller

print("Press F7 to Start")
print("Press F8 to Stop")
print("Press F9 to End\n")

pyautogui.FAILSAFE = False

run = False
execution_stopped = False
startTime = time.time()

fail_counter = 0
total_failed_attempts = 0
total_success_attempts = 0
emote_elapsed_time = 0
is_boss_killed = False


def my_function():
    global run
    global execution_stopped

    global fail_counter
    global total_success_attempts
    global total_failed_attempts
    global emote_elapsed_time
    global is_boss_killed

    run = True
    execution_stopped = False

    while run:
        if total_success_attempts > 0 and total_success_attempts % 10 == 0:
            collect_items_from_DIM()

        if fail_counter >= 10:
            print("Too many failed attempts, relaunching the dungeon...")
            while True:
                if pyautogui.locateOnScreen("In Dungeon Icon.png", confidence=0.8):
                    break
            restart_dungeon()
            fail_counter = 0

        if pyautogui.locateOnScreen("Smoke Bomb.png", confidence=0.9):
            indebted_kindness()
            # waveframe()

            # Turn left and move to corner
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -670, 0, 0, 0)
            time.sleep(0.5)
            keyboard.press('shift')
            keyboard.press('w')
            time.sleep(5)
            keyboard.release('shift')
            keyboard.release('w')

            # Turn left and emote
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -600, 0, 0, 0)
            time.sleep(0.2)
            keyboard.press_and_release('left')
            emote_elapsed_time = time.time()

            while True:
                print("Checking cases")
                print("Time: " + str(time.time() - emote_elapsed_time))
                if pyautogui.locateOnScreen("Guardian Down.png", confidence=0.8) or \
                        pyautogui.locateOnScreen("Your Light Fades Away.png", confidence=0.8):
                    print("Case: Guardian Down")
                    total_failed_attempts += 1
                    fail_counter += 1
                    break

                elif not pyautogui.locateOnScreen("Boss Health Bar.png", confidence=0.7, region=(842, 1273, 500, 500)):
                    print("Case: Boss is killed")
                    is_boss_killed = True
                    break

                elif time.time() - emote_elapsed_time > 15:
                    print("Case: Boss is still alive, emoting for too long...")
                    keyboard.press_and_release('3')
                    time.sleep(1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
                    time.sleep(1)
                    pyautogui.leftClick()
                    total_failed_attempts += 1
                    fail_counter += 1
                    break

            # Restart dungeon if boss is killed
            if is_boss_killed:
                time.sleep(1)

                if pyautogui.locateOnScreen("Guardian Down.png", confidence=0.8) or \
                        pyautogui.locateOnScreen("Your Light Fades Away.png", confidence=0.8):
                    print("Actually no...")
                    is_boss_killed = False
                    total_failed_attempts += 1
                else:
                    print("Boss kill is confirmed...Restarting dungeon")
                    total_success_attempts += 1
                    fail_counter = 0

                    is_boss_killed = False
                    restart_dungeon()


def collect_items_from_DIM():
    keyboard.press_and_release("alt+tab")
    time.sleep(0.5)

    try:
        x, y = pyautogui.locateCenterOnScreen("DIM Collect Postmaster.png", confidence=0.7)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(1)
        keyboard.press_and_release("alt+tab")
    except TypeError:
        keyboard.press_and_release("alt+tab")
        print("DIM Collect Postmaster is not found")


def waveframe():
    # Swap to Kinetic
    keyboard.press_and_release("1")
    time.sleep(1)

    # Aim at boss and shoot to trigger encounter
    time.sleep(0.7)
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -150, -190, 0, 0)
    time.sleep(0.1)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Smoke bomb
    keyboard.press_and_release('space')
    time.sleep(0.1)
    Controller().click(Button.x1)
    time.sleep(1)

    # Swap to Waveframe GL
    keyboard.press_and_release("2")

    # Move to target position
    keyboard.press('a')
    time.sleep(0.8)
    keyboard.release('a')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 80, 20, 0, 0)
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')

    # Aim and shoot yellow bar behind boss
    pyautogui.mouseDown(button='right')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 310, 250, 0, 0)
    time.sleep(5.9)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Finisher
    keyboard.press('g')
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(3)
    keyboard.release('g')
    keyboard.release('shift')
    keyboard.release('w')


def indebted_kindness():
    # Swap to Indebted Kindness
    keyboard.press_and_release("2")
    time.sleep(1)

    # Start encounter
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -90, -100, 0, 0)
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(0.2)

    # Smoke bomb
    keyboard.press_and_release("space")
    time.sleep(0.2)
    Controller().click(Button.x1)
    time.sleep(1)

    # Move to target position
    keyboard.press("d")
    time.sleep(1)
    keyboard.release('d')
    keyboard.press("w")
    time.sleep(1.3)
    keyboard.release('w')

    # Shoot yellow bar
    pyautogui.mouseDown(button='right')
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -580, 390, 0, 0)
    time.sleep(5.9)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Finisher
    keyboard.press('shift+w')
    keyboard.press('g')
    time.sleep(1.7)
    keyboard.release('g')
    keyboard.release('shift+w')
    time.sleep(1.3)


def restart_dungeon():
    keyboard.press_and_release('m')
    time.sleep(1)
    pyautogui.moveTo(4000, 1000)
    time.sleep(0.5)
    pyautogui.moveTo(2000, 1000)

    time.sleep(0.5)

    try:
        x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("Dungeon Icon Not Found")

    time.sleep(1)

    # Click on Normal Difficulty
    pyautogui.moveTo(1948, 1115)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on Master
    pyautogui.moveTo(261, 450)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    try:
        x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("Launch Not Found")

    print("Waiting to Load In")
    while True:
        if pyautogui.locateOnScreen("In Dungeon Icon.png", confidence=0.8):
            print("Loaded into Dungeon")
            break

    # Start resetting checkpoint
    keyboard.press_and_release('m')
    time.sleep(1)
    pyautogui.moveTo(4000, 1000)
    time.sleep(1)
    pyautogui.moveTo(2000, 1000)

    time.sleep(1)

    try:
        x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
    except TypeError:
        print("Dungeon Icon Not Found")

    time.sleep(1)

    # Click on Normal Difficulty
    pyautogui.moveTo(1948, 1115)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Click on Master
    pyautogui.moveTo(261, 450)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

    # Reset checkpoint
    try:
        x, y = pyautogui.locateCenterOnScreen("Reset Icon.png", confidence=0.8)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        keyboard.press('f')
        time.sleep(3)
        keyboard.release('f')
        time.sleep(0.1)
        keyboard.press_and_release('esc')
        time.sleep(0.5)
        keyboard.press_and_release('esc')
        time.sleep(1)
    except TypeError:
        print("Reset Icon Not Found")

    # Aim at boss and shoot to trigger encounter
    keyboard.press_and_release('2')
    time.sleep(1.7)
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -150, -190, 0, 0)
    time.sleep(0.1)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Use heavy to suicide
    keyboard.press_and_release('3')
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
    time.sleep(1)
    pyautogui.leftClick()

    print("Waiting for respawn after suicide")
    while True:
        if pyautogui.locateOnScreen("Dungeon Mission Objective Icon.png", confidence=0.8):
            print("Respawned")
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
    keyboard.release('a')
    keyboard.release('s')
    keyboard.release('d')
    keyboard.release('ctrl')
    keyboard.release("alt")
    keyboard.release("tab")
    print(f"Total Failed Attempts: ", total_failed_attempts)
    print(f"Total Success Attempts: ", total_success_attempts)
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")