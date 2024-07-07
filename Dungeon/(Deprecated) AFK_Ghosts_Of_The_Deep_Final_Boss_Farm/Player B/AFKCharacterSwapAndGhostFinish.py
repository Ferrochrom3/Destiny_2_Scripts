import pyautogui
import time
import keyboard
import sys
import threading
import win32con
import win32api
from colorama import Fore, Style

pyautogui.FAILSAFE = False

is_master = False
player_id = input("Input the player ID you want to join. \nExample: Guardian#1234 \nPlayer ID: ")
boolean_value = input("1 for True, 0 for False \nIs this a Master run: ")
if boolean_value == '1':
    is_master = True
elif boolean_value == '0':
    is_master = False
else:
    print("Error!")
    time.sleep(2)
    sys.exit()

print("Press F7 to Start")
print("Press F9 to Exit\n")

startTime = time.time()

runtime = 0
afk_timer = 0
total_boss_killed = 0


def afk():
    global runtime
    global afk_timer
    global total_boss_killed
    global is_master
    global player_id

    while True:
        global is_master
        global afk_timer
        runtime = time.time()

        print(f"{Fore.GREEN}Trying to open director{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Open Director.png", confidence=0.8):
                time.sleep(1)
                keyboard.press_and_release('m')
                break

        print(f"{Fore.GREEN}Looking for HELM{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("HELM.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("HELM.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                pyautogui.leftClick()
                break

        print(f"{Fore.GREEN}Looking for dungeon icon{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Dungeon Icon.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("Dungeon Icon.png", confidence=0.8)
                time.sleep(1)
                pyautogui.moveTo(x, y)
                pyautogui.leftClick()
                break

        if is_master:
            time.sleep(1.5)
            pyautogui.moveTo(1466, 837, duration=0.1)
            pyautogui.leftClick()
            time.sleep(1.5)
            pyautogui.moveTo(212, 343, duration=0.1)
            pyautogui.leftClick()
            time.sleep(1.5)

        print(f"{Fore.GREEN}Proceeding to launch the mission{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Launch.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("Launch.png", confidence=0.8)
                time.sleep(1)
                pyautogui.moveTo(x, y)
                pyautogui.leftClick()
                break

        print(f"{Fore.LIGHTMAGENTA_EX}Inviting{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Strand Rally Barricade.png", confidence=0.9):
                time.sleep(2)
                keyboard.press_and_release('enter')
                time.sleep(0.5)
                keyboard.write(f"/invite {player_id}")
                time.sleep(0.5)
                keyboard.press_and_release('enter')
                break

        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for player to join{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Player Joined.png", confidence=0.8):
                runtime = time.time()
                time.sleep(8)
                keyboard.press_and_release('esc')
                time.sleep(1)
                pyautogui.moveTo(682, 598)  # change character
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(745, 648)  # confirm
                pyautogui.click()
                break

        if is_master:
            time.sleep(40)

        print(f"{Fore.BLUE}Switching to Warlock{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Warlock.png", confidence=0.8):
                x, y = pyautogui.locateCenterOnScreen("Warlock.png", confidence=0.8)
                pyautogui.moveTo(x, y, duration=0.1)
                time.sleep(0.1)
                pyautogui.leftClick()
                break

        print(f"{Fore.BLUE}Joining{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Open Director.png", confidence=0.8):
                time.sleep(2)
                keyboard.press_and_release('enter')
                time.sleep(0.5)
                keyboard.write(f"/join {player_id}")
                time.sleep(0.5)
                keyboard.press_and_release('enter')
                time.sleep(1)

                while True:
                    if pyautogui.locateOnScreen("Error Code Exclamation Mark.png", confidence=0.8, grayscale=True):
                        print("Can't Joint Yet")
                        keyboard.press_and_release('enter')
                        time.sleep(1)

                        keyboard.press_and_release('enter')
                        time.sleep(0.5)
                        keyboard.write(f"/join {player_id}")
                        time.sleep(0.5)
                        keyboard.press_and_release('enter')

                        time.sleep(1)
                    if pyautogui.locateOnScreen("Joining Fireteam.png", confidence=0.8, grayscale=True):
                        print("Joining...")
                        break
                break

        print(f"{Fore.BLUE}Joined{Style.RESET_ALL}")
        while True:
            keyboard.press_and_release("Alt")
            time.sleep(2)
            if pyautogui.locateOnScreen("Solar Empowering Rift.png", confidence=0.9):
                print("Moving to Position")
                time.sleep(2)

                keyboard.press('shift+w')
                time.sleep(2)
                keyboard.release('shift+w')

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 400, 0, 0, 0)
                time.sleep(0.2)

                keyboard.press('shift+w')
                time.sleep(5)
                keyboard.release('shift+w')

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1000, 0, 0, 0)
                time.sleep(0.2)

                keyboard.press('w')
                time.sleep(3.1)
                keyboard.release('w')
                break

        print(f"{Fore.LIGHTYELLOW_EX}Giving Empowering Rift buff{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Solar Empowering Rift.png", confidence=0.9):
                keyboard.press_and_release('v')
                time.sleep(3)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 200, 0, 0, 0)
                time.sleep(0.2)
                keyboard.press('s')
                time.sleep(0.7)
                keyboard.release('s')
                break

        time.sleep(5)
        keyboard.press('w')
        time.sleep(0.7)
        keyboard.release('w')
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -200, 0, 0, 0)

        print("Ready to Revive")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error in \"Ready to Revive\"{Style.RESET_ALL}")
                    break
            else:
                if time.time() - runtime > 900:
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error in \"Ready to Revive\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Alt.png", confidence=0.8, grayscale=True):
                time.sleep(1)
                keyboard.press('alt')
                time.sleep(2)
                keyboard.release('alt')

                keyboard.press('s')
                time.sleep(0.7)
                keyboard.release('s')
                time.sleep(1)
                break

        print("In position to finish ghost")
        afk_timer = time.time()
        while True:
            if is_master:
                if time.time() - afk_timer > 800:
                    time.sleep(0.1)
                    keyboard.press_and_release('a')
                    time.sleep(0.2)
                    keyboard.press_and_release('d')
                    time.sleep(0.1)
                    afk_timer = time.time()
                if time.time() - runtime > 1800:
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error in \"In position to finish ghost\"{Style.RESET_ALL}")
                    break
            else:
                if time.time() - runtime > 900:
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error in \"In position to finish ghost\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Tab.png", confidence=0.8):
                total_boss_killed += 1
                print(f"{Fore.LIGHTBLUE_EX}Total Boss Killed: {total_boss_killed}{Style.RESET_ALL}")
                break

            keyboard.press('g')
            keyboard.press_and_release('space')
            time.sleep(0.1)
            keyboard.press_and_release('space')
            time.sleep(6)
            keyboard.release('g')
            time.sleep(0.5)

        time.sleep(5)
        keyboard.press_and_release('esc')
        print(f"{Fore.CYAN}Open Game Options Menu{Style.RESET_ALL}")
        time.sleep(1)
        if pyautogui.locateOnScreen("Game Options.png", grayscale=True, confidence=0.8):
            print(f"{Fore.CYAN}Game Options Menu Opened | Changing Character{Style.RESET_ALL}")
            pyautogui.moveTo(682, 598)  # change character
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(745, 648)  # confirm
            pyautogui.click()
        else:
            print(f"{Fore.CYAN}Game Options Menu Not Opened | Opening Game Options Menu{Style.RESET_ALL}")
            keyboard.press_and_release('esc')
            time.sleep(1)
            print(f"{Fore.CYAN}Game Options Menu Opened | Changing Character{Style.RESET_ALL}")
            pyautogui.moveTo(682, 598)  # change character
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(745, 648)  # confirm
            pyautogui.click()

        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen("Titan.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                time.sleep(0.1)
                pyautogui.leftClick()
                break
            except TypeError:
                pass


def start_afk():
    t1 = threading.Thread(target=afk)
    print("\nExecution Started")
    t1.start()


while True:
    keyboard.add_hotkey('f7', start_afk)
    keyboard.wait('f9')
    keyboard.release('shift+w')
    keyboard.release('alt')
    keyboard.release('g')
    keyboard.release('s')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds = "
             + str(round((time.time() - startTime) / 60, 1)) + " minutes = "
             + str(round((time.time() - startTime) / 3600, 1)) + " hours")
