import time
import keyboard
import pyautogui
import resolution_config

image_path = "Destiny_2_Scripts/AFK_Exotic_Class_Item_Farm/Version_3"

collect_loot_attempts = 0
number_of_chests_obtained = 0


def collect_loot():
    global number_of_chests_obtained  # pylint: disable=w0603

    time.sleep(0.5)

    if pyautogui.locateOnScreen(f"{image_path}/Alt Button.png", confidence=0.8, region=resolution_config.chest_collection_region):
        number_of_chests_obtained += 1
        keyboard.press("alt")
        time.sleep(1.5)
        keyboard.release("alt")
