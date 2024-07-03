import sys
import time
import keyboard
import pyautogui
import win32api
import win32con
import numpy

sys.path.insert(0, "D:\\Visual Studio Code Projects\\")
from Destiny_2_Scripts.Other_Utilities.Broccoli_Error_Fix.broccoli_error_fix import is_broccoli_error
from Destiny_2_Scripts.Other_Utilities.Internet_Error_Fix.internet_error_fix import is_internet_error

image_path = "Destiny_2_Scripts/The_Invesigation/AFK_World_Drop_Farm"

kinetic_slot_position = 700, 520
energy_slot_position = 700, 690
power_slot_position = 700, 860

helmet_slot_position = 1860, 360
arm_slot_position = 1860, 520
chest_slot_position = 1860, 690
leg_slot_position = 1860, 860
class_item_slot_position = 1860, 1020

horizontal_offset = 150, 0
vertical_offset = 140, 0

total_engramed_collected = 0


def go_to_helm_and_collect_loot():
    global total_engramed_collected  # pylint: disable=W0603

    print("Going back to the HELM")
    keyboard.press_and_release("m")
    time.sleep(1.5)
    keyboard.press_and_release("d")
    time.sleep(1.5)

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Helm Icon.png", confidence=0.9)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1.5)

    x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Landing Zone.png", confidence=0.9)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.5)

    # Click "Launch"
    pyautogui.moveTo(2163, 1210)
    time.sleep(0.3)
    pyautogui.leftClick()

    # Wait until loaded into the HELM and don't let errors hold the loop forever
    while True:
        if pyautogui.locateOnScreen(f"{image_path}/Echos Icon.png", confidence=0.8) or is_broccoli_error() or is_internet_error():
            time.sleep(3)
            break

    # Run towards Post Box
    turn_camera(-130, 0)
    time.sleep(0.1)
    keyboard.press("shift+w")
    time.sleep(3.4)
    keyboard.release("shift+w")
    time.sleep(1)
    keyboard.press("Alt")
    time.sleep(1)
    keyboard.release("Alt")
    time.sleep(1.5)

    # Start collecting engrams
    while pyautogui.locateOnScreen(f"{image_path}/Legendary Engram.png", confidence=0.9):
        x, y = pyautogui.locateCenterOnScreen(f"{image_path}/Legendary Engram.png", confidence=0.9)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)
        pyautogui.leftClick()
        pyautogui.moveTo(765, 731)  # A random position to the left of the screen to prevent engram description popup
        time.sleep(0.5)

        total_engramed_collected += 1

    time.sleep(1)
    keyboard.press_and_release("esc")
    time.sleep(1.5)

    # Run towards vault
    turn_camera(-2400, 0)
    keyboard.press("shift+w")
    time.sleep(1.55)
    keyboard.release("shift+w")

    # Open vault then inventory
    keyboard.press("Alt")
    time.sleep(1.3)
    keyboard.release("Alt")
    time.sleep(0.5)
    keyboard.press_and_release("f1")
    time.sleep(1.5)

    dismantle_kinetic_slot()
    dismantle_energy_slot()
    dismantle_power_slot()
    dismantle_helmet_slot()
    dismantle_arm_slot()
    dismantle_chest_slot()
    dismantle_leg_slot()
    dismantle_class_item_slot()


def dismantle_kinetic_slot():
    print("Dismantling Kinetic slot")
    pyautogui.moveTo(kinetic_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(subtract_tuples(kinetic_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_energy_slot():
    print("Dismantling Energy slot")
    pyautogui.moveTo(energy_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(subtract_tuples(energy_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_power_slot():
    print("Dismantling Power slot")
    pyautogui.moveTo(power_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(subtract_tuples(power_slot_position, horizontal_offset))

    # Dismantle 9 times
    for _ in range(10):
        pyautogui.leftClick()
        time.sleep(1.5)
        # # Send the weapon to vault if found
        # if pyautogui.locateOnScreen(f"{image_path}\Crux Termination IV.png", confidence=0.7):
        #     pyautogui.leftClick()
        #     time.sleep(1)
        #     continue

        # keyboard.press_and_release("f")
        # time.sleep(0.1)
        # keyboard.press("f")
        # time.sleep(1.3)
        # keyboard.release("f")
        # time.sleep(1.3)

    time.sleep(0.5)


def dismantle_helmet_slot():
    print("Dismantling Helmet slot")
    pyautogui.moveTo(helmet_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(add_tuples(helmet_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_arm_slot():
    print("Dismantling Arm slot")
    pyautogui.moveTo(arm_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(add_tuples(arm_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_chest_slot():
    print("Dismantling Chest slot")
    pyautogui.moveTo(chest_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(add_tuples(chest_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_leg_slot():
    print("Dismantling Leg slot")
    pyautogui.moveTo(leg_slot_position)
    pyautogui.moveTo(add_tuples(leg_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_class_item_slot():
    print("Dismantling Class Item slot")
    pyautogui.moveTo(class_item_slot_position)
    time.sleep(0.1)
    pyautogui.moveTo(add_tuples(class_item_slot_position, horizontal_offset))

    dismantle_items()
    time.sleep(0.5)


def dismantle_items():
    # Dismantle 9 times
    for _ in range(9):
        keyboard.press_and_release("f")
        time.sleep(0.1)
        keyboard.press("f")
        time.sleep(1.3)
        keyboard.release("f")
        time.sleep(1.5)

        # if not pyautogui.locateOnScreen(f"{image_path}/Armor Side Options.png", confidence=0.9):
        #     print("No more items to dismantle...Break...")
        #     break


def subtract_tuples(t1, t2):
    array1 = numpy.array(t1)
    array2 = numpy.array(t2)

    return tuple(array1 - array2)


def add_tuples(t1, t2):
    array1 = numpy.array(t1)
    array2 = numpy.array(t2)

    return tuple(array1 + array2)


def turn_camera(x: int, y: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
    time.sleep(0.2)
