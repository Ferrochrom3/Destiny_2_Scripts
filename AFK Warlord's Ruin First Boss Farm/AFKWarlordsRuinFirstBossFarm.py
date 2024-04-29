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

invis_counter = 0
fail_counter = 0
total_failed_attempts = 0
total_success_attempts = 0
is_boss_killed = False


def my_function():
    global run
    global execution_stopped
    global invis_counter
    global fail_counter
    global is_boss_killed

    run = True
    execution_stopped = False
    fail_counter = 0
    invis_counter = 0
    is_boss_killed = False

    while run:
        waveframe()


def check_health_bar():
    time.sleep(1)
    if not pyautogui.locateOnScreen("Boss Health Bar.png", confidence=0.7, region=(842, 1273, 500, 500)):
        print("Boss is dead")
    elif pyautogui.locateOnScreen("Boss Health Bar.png", confidence=0.7, region=(842, 1273, 500, 500)):
        print("Boss is alive")


def waveframe():
    global invis_counter
    global fail_counter
    global is_boss_killed
    global total_failed_attempts
    global total_success_attempts

    if fail_counter >= 10:
        restart_dungeon_after_10_fails()
        fail_counter = 0

    if pyautogui.locateOnScreen("Smoke Bomb.png", confidence=0.9):
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

        keyboard.press_and_release('space')
        time.sleep(0.1)

        Controller().click(Button.x1)  # Smoke bomb
        time.sleep(1)

        keyboard.press_and_release("2")

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

        # Move away from finishing position
        time.sleep(1)
        keyboard.press('s')
        time.sleep(2)
        keyboard.release('s')

        # Stay invis for 8 iterations until player dies or XP bar shows up (cage will auto kill player to exit the loop)
        while invis_counter < 8:
            print("Checking cases")
            if pyautogui.locateOnScreen("Smoke Bomb.png", confidence=0.8):
                print("Case: Go invis")
                time.sleep(1)

                # Smoke bomb
                keyboard.press_and_release('space')
                time.sleep(0.1)
                Controller().click(Button.x1)
                time.sleep(1)

                # Move to a different position
                if invis_counter % 2 == 0:
                    keyboard.press('d')
                    keyboard.press('s')
                    time.sleep(1)
                    keyboard.release('s')
                    keyboard.release('d')
                else:
                    keyboard.press('a')
                    keyboard.press('w')
                    time.sleep(1)
                    keyboard.release('a')
                    keyboard.release('w')

                # Inc counter
                invis_counter += 1

            elif pyautogui.locateOnScreen("Guardian Down.png", confidence=0.8) or pyautogui.locateOnScreen(
                    "Your Light Fades Away.png", confidence=0.8) or pyautogui.locateOnScreen("Text Chat Icon.png", confidence=0.8):
                print("Case: Guardian Down")
                total_failed_attempts += 1
                fail_counter += 1
                break

            elif not pyautogui.locateOnScreen("Boss Health Bar.png", confidence=0.7, region=(842, 1273, 500, 500)):
                print("Case: Boss is killed")
                is_boss_killed = True
                break

        # Restart dungeon if boss is killed
        if is_boss_killed:
            restart_dungeon_after_boss_kill()
            total_success_attempts += 1
            fail_counter = 0

        invis_counter = 0  # Reset counter


def restart_dungeon_after_boss_kill():
    global is_boss_killed
    is_boss_killed = False

    print("Starting a new run...")

    keyboard.press_and_release('m')
    time.sleep(2)
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

    try:
        x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.7)
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
    except TypeError:
        print("Reset Icon Not Found")

    # Aim at boss and shoot to trigger encounter
    time.sleep(0.7)
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -150, -190, 0, 0)
    time.sleep(0.1)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Use heavy to suicide
    keyboard.press_and_release('3')
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
    time.sleep(1)
    pyautogui.leftClick()

    print("Waiting for respawn after suicide")
    while True:
        if pyautogui.locateOnScreen("In Dungeon Icon.png", confidence=0.8):
            print("Respawned")
            break


def func1():
    keyboard.press_and_release('3')
    time.sleep(1)

    # Run towards ledge
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -400, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(5.6)
    keyboard.release('shift')
    keyboard.release('w')

    # Turn and continue to run on ledge
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 900, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.5)
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(1)

    # Turn and run/jump up hill
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 700, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(2)

    # Move a little toward flag
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.release('w')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2000, 0, 0, 0)

    # Jump on rock
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.5)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(1)

    # Adjust position on rock
    keyboard.press('a')
    time.sleep(0.2)
    keyboard.release('a')
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')

    # Jump higher on rock
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    time.sleep(0.1)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    keyboard.release('w')
    time.sleep(1)

    # Jump toward large rock
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -120, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('s')
    time.sleep(0.1)
    keyboard.release('s')
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.press('space')
    time.sleep(0.7)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.8)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.8)
    keyboard.release('space')
    time.sleep(0.5)
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(1)

    # Turn 360 and jump to higher point
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -4500, 0, 0, 0)
    time.sleep(0.3)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.2)
    keyboard.release('space')
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(2)

    # Adjust position
    keyboard.press('s')
    keyboard.press('d')
    time.sleep(0.2)
    keyboard.release('s')
    time.sleep(0.3)
    keyboard.release('d')

    # Turn slight right and jump to higher point
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 400, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.3)
    keyboard.release('space')
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(1)

    # Turn slight left and jump to higher point
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1000, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(4)
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(2)

    # Turn left and jump across
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1000, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.6)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(1.3)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(0.7)
    keyboard.press('space')
    time.sleep(0.4)
    keyboard.release('space')
    time.sleep(0.6)
    keyboard.release('shift')
    keyboard.release('w')
    time.sleep(2)

    # Turn left and move toward ledge
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1200, 0, 0, 0)
    time.sleep(0.1)
    keyboard.press('shift')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.release('shift')
    keyboard.release('w')

    # Turn left and jump toward ledge
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -800, 0, 0, 0)
    time.sleep(0.1)


def restart_dungeon_after_10_fails():
    print("Too many failed attempts, relaunching the dungeon...")

    while True:
        if pyautogui.locateOnScreen("In Dungeon Icon.png", confidence=0.8):
            break

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
    except TypeError:
        print("Reset Icon Not Found")

    # Aim at boss and shoot to trigger encounter
    time.sleep(0.7)
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -150, -190, 0, 0)
    time.sleep(0.1)
    pyautogui.leftClick()
    pyautogui.mouseUp(button='right')

    # Use heavy to suicide
    keyboard.press_and_release('3')
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
    time.sleep(1)
    pyautogui.leftClick()

    print("Waiting for respawn after suicide")
    while True:
        if pyautogui.locateOnScreen("In Dungeon Icon.png", confidence=0.8):
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
    print("Total Failed Attempts: " + str(total_failed_attempts))
    print("Total Success Attempts: " + str(total_success_attempts))
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")