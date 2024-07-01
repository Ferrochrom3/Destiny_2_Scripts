import sys
import threading
import time
import keyboard


print("Press F7 to Start")
print("Press F8 to Exit\n")

run = False
start_time = time.time()


def my_function():
    run = True

    while run:
        keyboard.press_and_release("q")
        time.sleep(3.4)
        keyboard.press_and_release("s")
        time.sleep(0.1)


def start_afk():
    t = threading.Thread(target=my_function)
    print("\nExecution Started")
    t.start()


while True:
    keyboard.add_hotkey("f7", start_afk)
    keyboard.wait("f8")

    # fmt: off
    sys.exit(
    f"Elapsed Time: {round(time.time() - start_time)} seconds"
    f"\n{round((time.time() - start_time) / 60, 2)} minutes"
    f"\n{round((time.time() - start_time) / 3600, 2)} hours")
    # fmt: on
