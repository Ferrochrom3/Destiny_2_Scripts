import time
import keyboard
import pyautogui
import win32api
import win32con
import resolution_config
import efficiency_evaluation
from pynput.mouse import Button, Controller
from dungeon_restart_and_reset import relaunch_into_master, reset_checkpoint

screen_width, screen_height = pyautogui.size()
current_monitor_resolution = f"{screen_width}x{screen_height}"
config = resolution_config.values_by_resolution[current_monitor_resolution]

image_path = f"Destiny_2_Scripts/Dungeon/AFK_Warlord's_Ruin_First_Boss_Farm/Image_{current_monitor_resolution}"


def indebted_kindness():
    """
    Start the encounter with Indebted Kindness and go invis and move to position. Then, shoot the yellow bar and go for a finisher.
    """
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
    keyboard.release("d")
    keyboard.press("w")
    time.sleep(1.3)
    keyboard.release("w")

    # Shoot yellow bar
    pyautogui.mouseDown(button="right")
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -580, 390, 0, 0)
    time.sleep(6.1)
    pyautogui.leftClick()

    # Finisher
    keyboard.press("shift+w")
    keyboard.press("g")
    pyautogui.mouseUp(button="right")
    time.sleep(1.7)
    keyboard.release("g")
    keyboard.release("shift+w")
    time.sleep(1.3)


def emote_at_corner():
    """
    After performing a finisher, turn left and emote at the corner.
    """
    # Turn left and move to corner
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -670, 0, 0, 0)
    time.sleep(0.5)
    keyboard.press("shift")
    keyboard.press("w")
    time.sleep(4.5)
    keyboard.release("shift")
    keyboard.release("w")

    # Turn left and emote
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -640, 0, 0, 0)
    time.sleep(0.5)
    keyboard.press("left")
    time.sleep(0.1)
    keyboard.release("left")
    time.sleep(1)


def check_cases():
    """
    Check for the following 3 cases after moved to corner and started emoting:
        1. Player is killed
        2. Emoting time is too long, meaning the boss is still alive
        3. Boss is killed
    """
    emote_elapsed_time = time.time()
    print("Checking cases")
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Guardian Down.png", confidence=0.8) or pyautogui.locateOnScreen(f"{image_path}/Your Light Fades Away.png", confidence=0.8):
            print("Case: Guardian Down")
            efficiency_evaluation.total_failed_attempts += 1
            break

        if time.time() - emote_elapsed_time > 17:
            print("Case: Boss is still alive, emoting for too long...")
            keyboard.press_and_release("3")
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 5000, 0, 0)
            time.sleep(1)
            pyautogui.leftClick()
            efficiency_evaluation.total_failed_attempts += 1
            break

        # fmt: off
        if not pyautogui.locateOnScreen(f"{image_path}/Boss Health Bar.png", confidence=0.7, region=config["boss_health_bar_region"]) \
            and pyautogui.locateOnScreen(f"{image_path}/Player Health Bar.png", confidence=0.7, region=config["player_health_bar_region"]):
        # fmt: on
            time.sleep(1)  # Add some delay so relaunch is not too early
            print("Case: Boss is killed")
            efficiency_evaluation.total_success_attempts += 1
            relaunch_into_master()
            reset_checkpoint()
            break
