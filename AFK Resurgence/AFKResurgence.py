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

is_in_game = False
game_counter = 0
match_making_timer = 0


def my_function():
    global run
    global execution_stopped
    run = True
    execution_stopped = False

    while run:
        global game_counter
        global match_making_timer
        global is_in_game

        if pyautogui.locateOnScreen("Play Again.png", confidence=0.8):
            is_in_game = False
            game_counter += 1
            print(f"Games Restarted: {game_counter}")

            try_except_block("Play Again.png", 1)
            try_except_block("Yes.png", 5)

            match_making_timer = time.time()  # restart match making timer after starting a new match

        if pyautogui.locateOnScreen("Custom Loadout 1.png", confidence=0.8) and not is_in_game:
            print(f"Match Making Took: {str(round(time.time() - match_making_timer))}s")
            is_in_game = True

        if pyautogui.locateOnScreen("Choose A Landing Zone.png", confidence=0.8, grayscale=True):
            keyboard.press_and_release('space')

        if pyautogui.locateOnScreen("DirectX Error.png", confidence=0.8):
            print("DirectX Error Found")
            directx_error()


def try_except_block(image_name, wait_duration):
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{image_name}", confidence=0.8)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.leftClick()
        time.sleep(wait_duration)
    except TypeError:
        pass


def directx_error():
    print("Close Error Window 1")
    try_except_block("Close.png", 2)

    print("Close Error Window 2")
    try_except_block("Close.png", 2)

    print("Reopening Game")
    try_except_block("Game Icon.png", 1)
    for x in range(2):
        pyautogui.leftClick()
        time.sleep(0.1)

    print("Waiting For \"Run In Safe Mode\" Window")
    while True:
        if pyautogui.locateOnScreen("Run In Safe Mode.png", confidence=0.8):
            try_except_block("No.png", 1)
            break

    print("Waiting For Game to Launch")
    while True:
        if pyautogui.locateOnScreen("Skip.png", confidence=0.8):
            try_except_block("Skip.png", 1)
            break

    print("Launch Resurgence")
    try_except_block("Resurgence Icon.png", 3)
    print("Start Game")
    try_except_block("Start.png", 3)


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
