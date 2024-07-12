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
    win32api_move_mouse(-1770, 220, 0.2)


def run_from_3_to_4(character_class: str):
    """
    Run from Chest_3 to Chest_4. Since this requires abilities jumps, each class will be executed differently.

    Args:
        character_class (str): The class of the character that is currently running ("Hunter", "Warlock", or "Titan").
    """
    keyboard.press_and_release("3")
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(2.35)
    win32api_move_mouse(-2600, 0)

    match character_class:
        case "Hunter":
            keyboard.press("shift+w")
            time.sleep(0.2)
            hunter_jump(0.2, 0.1)
            hunter_jump(0.3, 0.1)
            hunter_jump(0.2, 0.1)
            time.sleep(1.5)
            keyboard.release("shift+w")

        case "Warlock":
            keyboard.press("shift+w")
            time.sleep(0.2)
            warlock_jump(0.05, 1.2)
            time.sleep(1.3)
            keyboard.release("shift+w")

        case "Titan":
            keyboard.press("shift+w")
            time.sleep(0.2)
            titan_jump(0.05, 1.4)
            time.sleep(1)
            keyboard.release("shift+w")

        case _:
            print("Not a proper character class")


def run_from_3_to_5(character_class: str):
    """
    Run from Chest_3 to Chest_5. Since this requires abilities jumps, each class will be executed differently.

    Args:
        character_class (str): The class of the character that is currently running ("Hunter", "Warlock", or "Titan").
    """
    keyboard.press_and_release("3")
    run_forward(1.8)
    win32api_move_mouse(-1400, 0)
    run_forward(2.5)
    win32api_move_mouse(3400, 0)

    match character_class:
        case "Hunter":
            keyboard.press("shift+w")
            time.sleep(0.2)
            hunter_jump(0.3, 0.3)
            hunter_jump(0.3, 0.3)
            hunter_jump(0.3, 0.3)
            time.sleep(2.4)
            keyboard.release("shift+w")

        case "Warlock":
            keyboard.press("shift+w")
            time.sleep(0.2)
            warlock_jump(0.05, 2)
            time.sleep(2.2)
            keyboard.release("shift+w")

        case "Titan":
            keyboard.press("shift+w")
            time.sleep(0.5)
            titan_jump(0.4, 1.4)
            time.sleep(1.9)
            keyboard.release("shift+w")

        case _:
            print("Not a proper character class")


def run_from_3_to_6(character_class: str):
    """
    Run from Chest_3 to Chest_6. Since this requires abilities jumps, each class will be executed differently.

    Args:
        character_class (str): The class of the character that is currently running ("Hunter", "Warlock", or "Titan").
    """
    keyboard.press_and_release("3")
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(2.5)
    win32api_move_mouse(-300, 0)

    match character_class:
        case "Hunter":
            keyboard.press("shift+w")
            time.sleep(0.6)
            hunter_jump(0.4, 0.3)
            hunter_jump(0.4, 0.3)
            hunter_jump(0.4, 0.3)
            time.sleep(1.9)
            keyboard.release("shift+w")

        case "Warlock":
            keyboard.press("shift+w")
            time.sleep(0.6)
            warlock_jump(0.05, 2.3)
            time.sleep(1.8)
            keyboard.release("shift+w")

        case "Titan":
            print("Work in Progress")
            keyboard.press("shift+w")
            time.sleep(0.8)
            warlock_jump(0.3, 1.3)
            time.sleep(2.3)
            keyboard.release("shift+w")

        case _:
            print("Not a proper character class")


def run_from_3_to_7():
    keyboard.press_and_release("3")
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(3.5)
    win32api_move_mouse(650, 0)
    run_forward(6.1)


def run_from_3_to_8():
    keyboard.press_and_release("3")
    run_forward(1.7)
    win32api_move_mouse(-1200, 0)
    run_forward(3.5)
    win32api_move_mouse(650, 0)
    run_forward(3)
    win32api_move_mouse(-1090, 0)
    run_forward(6)


def run_from_8_to_9():
    win32api_move_mouse(-1000, 0)
    run_forward(4.5)
    win32api_move_mouse(2000, 0)
    run_forward(1.8)


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


def warlock_jump(time_before_activate_glide: float, time_before_release_glide: float):
    keyboard.press_and_release("space")
    time.sleep(time_before_activate_glide)
    keyboard.press_and_release("space")
    time.sleep(time_before_release_glide)
    keyboard.press_and_release("space")


def titan_jump(time_before_activate_lift: float, time_before_release_lift: float):
    keyboard.press_and_release("space")
    time.sleep(time_before_activate_lift)
    keyboard.press_and_release("space")
    time.sleep(time_before_release_lift)
    keyboard.press_and_release("space")


def win32api_move_mouse(x: int, y: int, wait_time: float = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(wait_time)
