import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con


pyautogui.FAILSAFE = False
run = False

recoil = 3
delay = 0.019
key = ""


def instruction():
    global key
    print("\nWhich wish would you like the access?")
    print("1 For Riven")
    print("2 For Shuro Chi")
    print("3 For Morgeth")
    key = input()

    print("Press F7 to Start")
    print("Press F8 to Stop")
    print("Press F9 to End\n")


instruction()


def free():
    global run
    run = True
    while run:
        if key == "1":
            riven()
        elif key == "2":
            shuro_chi()
        elif key == "3":
            morgeth()
        else:
            print("===ERROR: INCORRECT NUMBER===")
            instruction()
        break


def shoot_wall(number):
    match number:
        case 1:
            move_and_shoot(-540, -310)
        case 2:
            move_and_shoot(-290, -340)
        case 3:
            move_and_shoot(0, -365)
        case 4:
            move_and_shoot(300, -340)
        case 5:
            move_and_shoot(535, -290)
        case 6:
            move_and_shoot(-560, -105)
        case 7:
            move_and_shoot(-300, -135)
        case 8:
            move_and_shoot(0, -150)
        case 9:
            move_and_shoot(300, -135)
        case 10:
            move_and_shoot(535, -105)
        case 11:
            move_and_shoot(-575, 160)
        case 12:
            move_and_shoot(-300, 145)
        case 13:
            move_and_shoot(0, 145)
        case 14:
            move_and_shoot(300, 155)
        case 15:
            move_and_shoot(535, 155)
        case 16:
            move_and_shoot(-575, 425)
        case 17:
            move_and_shoot(-300, 425)
        case 18:
            move_and_shoot(0, 425)
        case 19:
            move_and_shoot(300, 425)
        case 20:
            move_and_shoot(535, 425)


def move_and_shoot(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    click()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y + recoil, 0, 0)
    time.sleep(0.06)


def click():
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(delay)


def riven():
    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(6)
        shoot_wall(11)
        shoot_wall(9)

    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(6)
        shoot_wall(11)
        shoot_wall(14)

    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(6)
        shoot_wall(11)
        shoot_wall(5)

    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(9)
        shoot_wall(14)
        shoot_wall(20)

    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(5)
        shoot_wall(2)
        shoot_wall(17)

    for x in range(2):
        shoot_wall(1)
        shoot_wall(16)
        shoot_wall(10)
        shoot_wall(15)
        shoot_wall(13)
        shoot_wall(3)
        shoot_wall(18)
        shoot_wall(6)
        shoot_wall(11)
        shoot_wall(20)

    shoot_wall(1)
    shoot_wall(16)
    shoot_wall(10)
    shoot_wall(15)
    shoot_wall(13)
    shoot_wall(9)
    shoot_wall(14)
    shoot_wall(5)
    shoot_wall(2)
    shoot_wall(17)

    shoot_wall(1)
    shoot_wall(16)
    shoot_wall(10)
    shoot_wall(15)
    shoot_wall(9)
    shoot_wall(6)
    shoot_wall(11)
    shoot_wall(14)
    shoot_wall(20)
    shoot_wall(2)
    shoot_wall(17)

    shoot_wall(1)
    shoot_wall(16)
    shoot_wall(10)
    shoot_wall(15)
    shoot_wall(9)
    shoot_wall(14)
    shoot_wall(5)
    shoot_wall(13)
    shoot_wall(20)

    shoot_wall(1)
    shoot_wall(16)


def shuro_chi():
    for x in range(5):
        shoot_wall(2)
        shoot_wall(3)
        shoot_wall(4)
        shoot_wall(1)
        shoot_wall(7)
        shoot_wall(14)
        shoot_wall(20)
        shoot_wall(5)
        shoot_wall(9)
        shoot_wall(12)
        shoot_wall(16)

    for x in range(3):
        shoot_wall(2)
        shoot_wall(3)
        shoot_wall(4)
        shoot_wall(1)
        shoot_wall(7)
        shoot_wall(14)
        shoot_wall(20)
        shoot_wall(5)
        shoot_wall(9)
        shoot_wall(12)

    shoot_wall(2)
    shoot_wall(3)
    shoot_wall(4)
    shoot_wall(16)
    shoot_wall(8)
    shoot_wall(6)
    shoot_wall(10)
    shoot_wall(11)
    shoot_wall(15)
    shoot_wall(17)
    shoot_wall(18)
    shoot_wall(19)

    shoot_wall(2)
    shoot_wall(3)
    shoot_wall(4)
    shoot_wall(1)
    shoot_wall(7)
    shoot_wall(14)
    shoot_wall(20)
    shoot_wall(16)
    shoot_wall(8)
    shoot_wall(6)
    shoot_wall(10)
    shoot_wall(11)
    shoot_wall(15)

    keyboard.press_and_release('r')
    time.sleep(2.3)

    for x in range(5):
        shoot_wall(2)
        shoot_wall(3)
        shoot_wall(4)
        shoot_wall(1)
        shoot_wall(7)
        shoot_wall(14)
        shoot_wall(20)
        shoot_wall(5)
        shoot_wall(9)
        shoot_wall(12)
        shoot_wall(16)
        shoot_wall(8)
        shoot_wall(6)
        shoot_wall(10)
        shoot_wall(11)
        shoot_wall(15)
        shoot_wall(17)
        shoot_wall(18)
        shoot_wall(19)

    shoot_wall(2)
    shoot_wall(3)
    shoot_wall(4)
    shoot_wall(1)
    shoot_wall(7)
    shoot_wall(14)
    shoot_wall(20)
    shoot_wall(16)
    shoot_wall(8)


def morgeth():
    for x in range(5):
        shoot_wall(8)
        shoot_wall(3)
        shoot_wall(13)
        shoot_wall(18)
        shoot_wall(2)
        shoot_wall(4)
        shoot_wall(17)
        shoot_wall(19)
        shoot_wall(7)
        shoot_wall(9)

    for x in range(4):
        shoot_wall(8)
        shoot_wall(3)
        shoot_wall(13)
        shoot_wall(18)
        shoot_wall(2)
        shoot_wall(4)
        shoot_wall(17)
        shoot_wall(19)
        shoot_wall(12)
        shoot_wall(14)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(7)
    shoot_wall(9)
    shoot_wall(1)
    shoot_wall(5)
    shoot_wall(16)
    shoot_wall(20)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(2)
    shoot_wall(4)
    shoot_wall(17)
    shoot_wall(9)
    shoot_wall(12)
    shoot_wall(14)
    shoot_wall(1)
    shoot_wall(5)
    shoot_wall(16)
    shoot_wall(20)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(19)
    shoot_wall(7)
    shoot_wall(9)
    shoot_wall(12)
    shoot_wall(14)
    shoot_wall(1)
    shoot_wall(5)
    shoot_wall(16)
    shoot_wall(20)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(2)
    shoot_wall(4)
    shoot_wall(17)
    shoot_wall(12)
    shoot_wall(14)
    shoot_wall(1)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(19)
    shoot_wall(7)
    shoot_wall(9)
    shoot_wall(12)
    shoot_wall(14)
    shoot_wall(5)
    shoot_wall(16)
    shoot_wall(20)

    shoot_wall(8)
    shoot_wall(3)
    shoot_wall(13)
    shoot_wall(18)
    shoot_wall(2)
    shoot_wall(4)
    shoot_wall(17)
    shoot_wall(19)
    shoot_wall(7)
    shoot_wall(12)
    shoot_wall(14)
    shoot_wall(1)
    shoot_wall(5)
    shoot_wall(16)
    shoot_wall(20)

    shoot_wall(8)


def start_afk():
    t = threading.Thread(target=free)
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
    sys.exit()
