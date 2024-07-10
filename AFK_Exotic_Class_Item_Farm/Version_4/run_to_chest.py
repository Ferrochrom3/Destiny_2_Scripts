import time
import keyboard
import win32api
import win32con


def run_to_chest_3():
    run_forward(2)
    win32api_move_mouse(700, 0)
    run_forward(3)
    win32api_move_mouse(-1200, 0)
    run_forward(4.9)
    win32api_move_mouse(-1770, 220)


def run_from_3_to_4():
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(2.35)
    win32api_move_mouse(-2600, 0)
    keyboard.press("shift+w")
    time.sleep(0.2)
    hunter_jump(0.2, 0.1)
    hunter_jump(0.3, 0.1)
    hunter_jump(0.2, 0.1)
    time.sleep(1.3)
    keyboard.release("shift+w")


def run_from_3_to_5():
    run_forward(1.8)
    win32api_move_mouse(-1400, 0)
    run_forward(2.5)
    win32api_move_mouse(3380, 0)
    keyboard.press("shift+w")
    time.sleep(0.2)
    hunter_jump(0.3, 0.3)
    hunter_jump(0.3, 0.3)
    hunter_jump(0.3, 0.3)
    time.sleep(2.05)
    keyboard.release("shift+w")


def run_from_3_to_6():
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(2.5)
    win32api_move_mouse(-300, 0)
    keyboard.press("shift+w")
    time.sleep(0.6)
    hunter_jump(0.4, 0.3)
    hunter_jump(0.4, 0.3)
    hunter_jump(0.4, 0.3)
    time.sleep(1.7)
    keyboard.release("shift+w")


def run_from_3_to_7():
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(3.5)
    win32api_move_mouse(650, 0)
    run_forward(5.7)


def run_from_3_to_8():
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(3.5)
    win32api_move_mouse(650, 0)
    run_forward(3)
    win32api_move_mouse(-1090, 0)
    run_forward(5.5)


def run_forward(running_duration: float, wait_time: float = 0.1):
    keyboard.press("shift+w")
    time.sleep(running_duration)
    keyboard.release("shift+w")
    time.sleep(wait_time)


def hunter_jump(jump_hold_time: float, time_before_next_jump: float):
    keyboard.press("space")
    time.sleep(jump_hold_time)
    keyboard.release("space")
    time.sleep(time_before_next_jump)


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)
