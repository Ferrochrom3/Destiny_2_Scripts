import sys
import threading
import time
import keyboard


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
        keyboard.press_and_release('q')
        time.sleep(3.4)
        keyboard.press_and_release('s')
        time.sleep(0.1)


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
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
