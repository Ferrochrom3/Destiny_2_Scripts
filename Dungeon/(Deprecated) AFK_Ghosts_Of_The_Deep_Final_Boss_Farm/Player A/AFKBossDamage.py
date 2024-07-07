import sys
import threading
import time
import keyboard
import pyautogui
import win32api
import win32con
from colorama import Fore, Style

pyautogui.FAILSAFE = False

is_master = False
boolean_value = input("1 for True, 0 for False \nIs this a Master run: ")
if boolean_value == '1':
    is_master = True
elif boolean_value == '0':
    is_master = False
else:
    print("Error!")
    time.sleep(2)
    sys.exit()

print("Press F6 to Execute Titan Script")
print("Press F7 to Execute Hunter Script")
print("Press F8 to Execute Warlock Script")
print("Press F9 to End Execution")
print("Press F10 to Display Status")

run = False
startTime = time.time()

is_invite_present = False
is_boss_killed = False

runtime = 0
afk_timer = 0
total_boss_killed = 0
failed_runs_at_waitingforempoweringriftbuff = 0
failed_runs_at_waitingforrevive = 0
failed_runs_at_startkillingboss = 0


def warlock():
    global run
    run = True

    global is_invite_present
    global is_boss_killed

    global runtime
    global afk_timer
    global total_boss_killed
    global failed_runs_at_waitingforempoweringriftbuff
    global failed_runs_at_waitingforrevive
    global failed_runs_at_startkillingboss

    global is_master

    while run:
        runtime = time.time()

        # if on "Fireteam Invites" page, then go to "Fireteam Invites" page
        if not pyautogui.locateOnScreen("Fireteam Invites Icon.png", confidence=0.8, grayscale=True):
            print(f"{Fore.MAGENTA}Opening \"Fireteam Invites\" page{Style.RESET_ALL}")
            keyboard.press_and_release('u')
            time.sleep(1)
            for x in range(2):
                keyboard.press_and_release('s')
                time.sleep(0.2)

        time.sleep(1)
        print(f"{Fore.MAGENTA}Looking For Invite{Style.RESET_ALL}")

        # =====
        # if on "Fireteam Invites" page and invite is present, join fireteam
        try:
            x, y = pyautogui.locateCenterOnScreen("Player Invite.png", confidence=0.8)
            print(f"{Fore.CYAN}Invite Found{Style.RESET_ALL}")
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.leftClick()
            time.sleep(1)

            print(f"{Fore.CYAN}Accept Invite{Style.RESET_ALL}")
            runtime = time.time()  # resets runtime
            pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
            pyautogui.leftClick()
            time.sleep(4)
            pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
            pyautogui.leftClick()
            is_invite_present = True
        except TypeError:
            is_invite_present = False
            pass
        # =====

        # now on "Fireteam Invites" page, if invite is not present, wait and look for invite
        print(f"{Fore.GREEN}Invite Not Found | Waiting For Invite{Style.RESET_ALL}")
        while not is_invite_present:
            print(f"{Fore.GREEN}Looking For Player Invitation{Style.RESET_ALL}")
            while True:
                if pyautogui.locateOnScreen("Player Invite.png", confidence=0.8):
                    print(f"{Fore.GREEN}Player Invitation Found | Ready to Join Fireteam{Style.RESET_ALL}")
                    pyautogui.moveTo(633, 568, duration=0.1)
                    pyautogui.leftClick()
                    time.sleep(1)

                    print(f"{Fore.GREEN}Accept Invite{Style.RESET_ALL}")
                    runtime = time.time()  # resets runtime
                    pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
                    pyautogui.leftClick()
                    time.sleep(4)
                    pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
                    pyautogui.leftClick()
                    break
            is_invite_present = False
            break

        print(f"{Fore.LIGHTYELLOW_EX}Joining Dungeon{Style.RESET_ALL}")
        while True:
            if pyautogui.locateOnScreen("Threading Grenade.png", confidence=0.8, grayscale=True):
                print(f"{Fore.LIGHTYELLOW_EX}Joined Dungeon{Style.RESET_ALL}")
                time.sleep(2)
                break

        print("Moving Towards Boss")
        keyboard.press('shift+w')
        time.sleep(2)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 600, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('shift+w')
        time.sleep(5.3)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1400, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('w')
        time.sleep(4)
        keyboard.release('w')
        time.sleep(1)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -600, 0, 0, 0)
        time.sleep(0.5)
        keyboard.press('w')
        time.sleep(0.11)
        keyboard.release('w')
        time.sleep(1)

        # clear heavy weapon
        print("Emptying Heavy Ammo")
        keyboard.press_and_release('f1')
        time.sleep(1.5)
        pyautogui.moveTo(703, 852)
        time.sleep(1)
        pyautogui.moveTo(553, 852)
        time.sleep(1)
        for x in range(4):
            pyautogui.leftClick()
            time.sleep(1)
        keyboard.press_and_release('f1')
        time.sleep(1.5)

        print(f"{Fore.LIGHTBLUE_EX}Waiting For Empowering Rift Buff{Style.RESET_ALL}")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Empowering Rift Buff Icon.png", confidence=0.9, grayscale=True):
                print(f"{Fore.LIGHTBLUE_EX}Buff Received{Style.RESET_ALL}")
                time.sleep(1)
                break

        print(f"{Fore.LIGHTMAGENTA_EX}Getting ready to suicide and apply DoT{Style.RESET_ALL}")
        keyboard.press_and_release('2')
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 6000, 0, 0)
        time.sleep(0.3)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(1.7)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(0.9)

        keyboard.press_and_release('1')
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()

        keyboard.press_and_release('0')  # charged melee
        keyboard.press_and_release('2')
        time.sleep(0.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(1)

        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for Revive{Style.RESET_ALL}")

        while True:
            if is_master:
                if time.time() - afk_timer > 800:
                    keyboard.press_and_release('a')
                    time.sleep(0.1)
                    keyboard.press_and_release('d')
                    time.sleep(0.1)
                    afk_timer = time.time()
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Threading Grenade.png", confidence=0.8, grayscale=True):
                print(f"{Fore.LIGHTMAGENTA_EX}Revived{Style.RESET_ALL}")
                time.sleep(1)
                break

        if time.time() - runtime < 900:
            keyboard.press_and_release('1')
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
            time.sleep(0.1)

        print("Start Killing Boss")
        afk_timer = time.time()
        while True:
            if is_master:
                if time.time() - afk_timer > 800:
                    keyboard.press_and_release('a')
                    time.sleep(0.1)
                    keyboard.press_and_release('d')
                    time.sleep(0.1)
                    afk_timer = time.time()
                if time.time() - runtime > 1800:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break
            else:
                if time.time() - runtime > 900:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break

            pyautogui.leftClick()
            keyboard.press_and_release('f1')
            time.sleep(0.8)

            if pyautogui.locateOnScreen("Epochal Integration.png", confidence=0.8):
                print(f"{Fore.RED}Epochal Itegration is on Hand. Swapping Off.")
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True
            else:
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.9)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True

            keyboard.press_and_release('f1')
            time.sleep(3)  # wait for weapon swap delay

            if pyautogui.locateOnScreen("Strand Empowering Rift.png", confidence=0.9):
                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True

                pyautogui.leftClick()
                time.sleep(0.1)
                keyboard.press_and_release('v')
                time.sleep(4.5)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)

            if is_boss_killed:
                print(f"{Fore.LIGHTYELLOW_EX}Boss is killed. Going for ghost finish{Style.RESET_ALL}")
                total_boss_killed += 1
                print(f"{Fore.LIGHTYELLOW_EX}Total Boss Killed: {total_boss_killed}{Style.RESET_ALL}")

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3500, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1000, 0, 0)
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1)
                keyboard.release('w')
                keyboard.press('g')
                keyboard.press_and_release('space')
                time.sleep(0.1)
                keyboard.press_and_release('space')
                time.sleep(2)
                keyboard.release('g')
                is_boss_killed = False
                break

            if pyautogui.locateOnScreen("Tab.png", confidence=0.8):
                break

        keyboard.press_and_release('alt+tab')
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("Collect Postmaster.png", confidence=0.9)
            print("Collect Armors From Postmaster")
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            time.sleep(1)
            pass
        keyboard.press_and_release('alt+tab')
        time.sleep(1)


def hunter():
    global run
    run = True

    global is_invite_present
    global is_boss_killed

    global runtime
    global afk_timer
    global total_boss_killed
    global failed_runs_at_waitingforempoweringriftbuff
    global failed_runs_at_waitingforrevive
    global failed_runs_at_startkillingboss

    global is_master

    while run:
        runtime = time.time()

        # if on "Fireteam Invites" page, then go to "Fireteam Invites" page
        if not pyautogui.locateOnScreen("Fireteam Invites Icon.png", confidence=0.8, grayscale=True):
            print(f"{Fore.MAGENTA}Opening \"Fireteam Invites\" page{Style.RESET_ALL}")
            keyboard.press_and_release('u')
            time.sleep(1)
            for x in range(2):
                keyboard.press_and_release('s')
                time.sleep(0.2)

        time.sleep(1)
        print(f"{Fore.MAGENTA}Looking For Invite{Style.RESET_ALL}")

        # =====
        # if on "Fireteam Invites" page and invite is present, join fireteam
        try:
            x, y = pyautogui.locateCenterOnScreen("Player Invite.png", confidence=0.8)
            print(f"{Fore.CYAN}Invite Found{Style.RESET_ALL}")
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.leftClick()
            time.sleep(1)

            print(f"{Fore.CYAN}Accept Invite{Style.RESET_ALL}")
            runtime = time.time()  # resets runtime
            pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
            pyautogui.leftClick()
            time.sleep(4)
            pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
            pyautogui.leftClick()
            is_invite_present = True
        except TypeError:
            is_invite_present = False
            pass
        # =====

        # now on "Fireteam Invites" page, if invite is not present, wait and look for invite
        print(f"{Fore.GREEN}Invite Not Found | Waiting For Invite{Style.RESET_ALL}")
        while not is_invite_present:
            print(f"{Fore.GREEN}Looking For Player Invitation{Style.RESET_ALL}")
            while True:
                if pyautogui.locateOnScreen("Player Invite.png", confidence=0.8):
                    print(f"{Fore.GREEN}Player Invitation Found | Ready to Join Fireteam{Style.RESET_ALL}")
                    pyautogui.moveTo(633, 568, duration=0.1)
                    pyautogui.leftClick()
                    time.sleep(1)

                    print(f"{Fore.GREEN}Accept Invite{Style.RESET_ALL}")
                    runtime = time.time()  # resets runtime
                    pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
                    pyautogui.leftClick()
                    time.sleep(4)
                    pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
                    pyautogui.leftClick()
                    break
            is_invite_present = False
            break

        print("Joining Dungeon")
        while True:
            if pyautogui.locateOnScreen("Vortex Grenade.png", confidence=0.8, grayscale=True):
                print("Joined Dungeon")
                time.sleep(2)
                break

        print("Moving Towards Boss")
        keyboard.press('shift+w')
        time.sleep(2)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 600, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('shift+w')
        time.sleep(5.3)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1400, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('w')
        time.sleep(4)
        keyboard.release('w')
        time.sleep(1)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -600, 0, 0, 0)
        time.sleep(0.5)
        keyboard.press('w')
        time.sleep(0.09)
        keyboard.release('w')
        time.sleep(1)

        # clear heavy weapon
        print("Emptying Heavy Ammo")
        keyboard.press_and_release('f1')
        time.sleep(1.5)
        pyautogui.moveTo(703, 852)
        time.sleep(1)
        pyautogui.moveTo(553, 852)
        time.sleep(1)
        for x in range(4):
            pyautogui.leftClick()
            time.sleep(1)
        keyboard.press_and_release('f1')
        time.sleep(1.5)

        print(f"{Fore.LIGHTBLUE_EX}Waiting For Empowering Rift Buff{Style.RESET_ALL}")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Empowering Rift Buff Icon.png", confidence=0.9, grayscale=True):
                print(f"{Fore.LIGHTBLUE_EX}Buff Received{Style.RESET_ALL}")
                time.sleep(1)
                break

        print(f"{Fore.LIGHTMAGENTA_EX}Getting ready to suicide and apply DoT{Style.RESET_ALL}")
        keyboard.press_and_release('2')
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 6000, 0, 0)
        time.sleep(0.3)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(1.7)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(0.9)

        keyboard.press_and_release('1')
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()

        keyboard.press_and_release('2')
        time.sleep(0.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(1)

        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for Revive{Style.RESET_ALL}")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Vortex Grenade.png", confidence=0.8, grayscale=True):
                print(f"{Fore.LIGHTMAGENTA_EX}Revived{Style.RESET_ALL}")
                time.sleep(1)
                break

        if time.time() - runtime < 900:
            keyboard.press_and_release('1')
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
            time.sleep(0.1)

        print("Start Killing Boss")
        afk_timer = time.time()
        while True:
            if is_master:
                if time.time() - afk_timer > 800:
                    keyboard.press_and_release('a')
                    time.sleep(0.1)
                    keyboard.press_and_release('d')
                    time.sleep(0.1)
                    afk_timer = time.time()
                if time.time() - runtime > 1800:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break
            else:
                if time.time() - runtime > 900:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break

            pyautogui.leftClick()
            keyboard.press_and_release('f1')
            time.sleep(0.8)

            if pyautogui.locateOnScreen("Epochal Integration.png", confidence=0.8):
                print(f"{Fore.RED}Epochal Itegration is on Hand. Swapping Off.")
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True
            else:
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.9)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True

            keyboard.press_and_release('f1')
            time.sleep(3)  # wait for weapon swap delay

            if pyautogui.locateOnScreen("Smoke Bomb.png", confidence=0.9):
                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True

                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.5)
                keyboard.press_and_release('0')
                time.sleep(4.5)

            if is_boss_killed:
                print(f"{Fore.LIGHTYELLOW_EX}Boss is killed. Going for ghost finish{Style.RESET_ALL}")
                total_boss_killed += 1
                print(f"{Fore.LIGHTYELLOW_EX}Total Boss Killed: {total_boss_killed}{Style.RESET_ALL}")

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3500, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1000, 0, 0)
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1)
                keyboard.release('w')
                keyboard.press('g')
                keyboard.press_and_release('space')
                time.sleep(0.1)
                keyboard.press_and_release('space')
                time.sleep(2)
                keyboard.release('g')
                is_boss_killed = False
                break

        keyboard.press_and_release('alt+tab')
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("Collect Postmaster.png", confidence=0.9)
            print("Collect Armors From Postmaster")
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            time.sleep(1)
            pass
        keyboard.press_and_release('alt+tab')
        time.sleep(1)


def titan():
    global run
    run = True

    global is_invite_present
    global is_boss_killed

    global runtime
    global afk_timer
    global total_boss_killed
    global failed_runs_at_waitingforempoweringriftbuff
    global failed_runs_at_waitingforrevive
    global failed_runs_at_startkillingboss

    global is_master

    while run:
        runtime = time.time()

        # if on "Fireteam Invites" page, then go to "Fireteam Invites" page
        if not pyautogui.locateOnScreen("Fireteam Invites Icon.png", confidence=0.8, grayscale=True):
            print(f"{Fore.MAGENTA}Opening \"Fireteam Invites\" page{Style.RESET_ALL}")
            keyboard.press_and_release('u')
            time.sleep(1)
            for x in range(2):
                keyboard.press_and_release('s')
                time.sleep(0.2)

        time.sleep(1)
        print(f"{Fore.MAGENTA}Looking For Invite{Style.RESET_ALL}")

        # =====
        # if on "Fireteam Invites" page and invite is present, join fireteam
        try:
            x, y = pyautogui.locateCenterOnScreen("Player Invite.png", confidence=0.8)
            print(f"{Fore.CYAN}Invite Found{Style.RESET_ALL}")
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.leftClick()
            time.sleep(1)

            print(f"{Fore.CYAN}Accept Invite{Style.RESET_ALL}")
            runtime = time.time()  # resets runtime
            pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
            pyautogui.leftClick()
            time.sleep(4)
            pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
            pyautogui.leftClick()
            is_invite_present = True
        except TypeError:
            is_invite_present = False
            pass
        # =====

        # now on "Fireteam Invites" page, if invite is not present, wait and look for invite
        print(f"{Fore.GREEN}Invite Not Found | Waiting For Invite{Style.RESET_ALL}")
        while not is_invite_present:
            print(f"{Fore.GREEN}Looking For Player Invitation{Style.RESET_ALL}")
            while True:
                if pyautogui.locateOnScreen("Player Invite.png", confidence=0.8):
                    print(f"{Fore.GREEN}Player Invitation Found | Ready to Join Fireteam{Style.RESET_ALL}")
                    pyautogui.moveTo(633, 568, duration=0.1)
                    pyautogui.leftClick()
                    time.sleep(1)

                    print(f"{Fore.GREEN}Accept Invite{Style.RESET_ALL}")
                    runtime = time.time()  # resets runtime
                    pyautogui.moveTo(560, 349, duration=0.1)  # accept fireteam invite
                    pyautogui.leftClick()
                    time.sleep(4)
                    pyautogui.moveTo(946, 866, duration=0.1)  # confirm joining
                    pyautogui.leftClick()
                    break
            is_invite_present = False
            break

        print("Joining Dungeon")
        while True:
            if pyautogui.locateOnScreen("Stasis Barricade.png", confidence=0.8, grayscale=True):
                print("Joined Dungeon")
                time.sleep(2)
                break

        print("Moving Towards Boss")
        keyboard.press('shift+w')
        time.sleep(2)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 600, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('shift+w')
        time.sleep(5.3)
        keyboard.release('shift+w')

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1400, 0, 0, 0)
        time.sleep(0.2)

        keyboard.press('w')
        time.sleep(4)
        keyboard.release('w')
        time.sleep(1)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -600, 0, 0, 0)
        time.sleep(0.5)
        keyboard.press('w')
        time.sleep(0.09)
        keyboard.release('w')
        time.sleep(1)

        # clear heavy weapon
        print("Emptying Heavy Ammo")
        keyboard.press_and_release('f1')
        time.sleep(1.5)
        pyautogui.moveTo(703, 852)
        time.sleep(1)
        pyautogui.moveTo(553, 852)
        time.sleep(1)
        for x in range(4):
            pyautogui.leftClick()
            time.sleep(1)
        keyboard.press_and_release('f1')
        time.sleep(1.5)

        print(f"{Fore.LIGHTBLUE_EX}Waiting For Empowering Rift Buff{Style.RESET_ALL}")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforempoweringriftbuff += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Empowering Rift Buff\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Empowering Rift Buff Icon.png", confidence=0.9, grayscale=True):
                print(f"{Fore.LIGHTBLUE_EX}Buff Received{Style.RESET_ALL}")
                time.sleep(1)
                break

        print(f"{Fore.LIGHTMAGENTA_EX}Getting ready to suicide and apply DoT{Style.RESET_ALL}")
        keyboard.press_and_release('2')
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 6000, 0, 0)
        time.sleep(0.3)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(1.7)

        pyautogui.leftClick()
        keyboard.press_and_release('r')
        time.sleep(0.9)

        keyboard.press_and_release('1')
        time.sleep(0.4)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()

        keyboard.press_and_release('2')
        time.sleep(0.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 4000, 0, 0)
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(1)

        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for Revive{Style.RESET_ALL}")
        while True:
            if is_master:
                if time.time() - runtime > 1800:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break
            elif not is_master:
                if time.time() - runtime > 900:
                    failed_runs_at_waitingforrevive += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Waiting For Revive\"{Style.RESET_ALL}")
                    break

            if pyautogui.locateOnScreen("Vortex Grenade.png", confidence=0.8, grayscale=True):
                print(f"{Fore.LIGHTMAGENTA_EX}Revived{Style.RESET_ALL}")
                time.sleep(1)
                break

        if time.time() - runtime < 900:
            keyboard.press_and_release('1')
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -6000, 0, 0)
            time.sleep(0.1)

        print("Start Killing Boss")
        afk_timer = time.time()
        while True:
            if is_master:
                if time.time() - afk_timer > 800:
                    keyboard.press_and_release('a')
                    time.sleep(0.1)
                    keyboard.press_and_release('d')
                    time.sleep(0.1)
                    afk_timer = time.time()
                if time.time() - runtime > 1800:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 1800 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break
            else:
                if time.time() - runtime > 900:
                    failed_runs_at_startkillingboss += 1
                    print(f"{Fore.RED}Current Time: {str(round(time.time() - runtime))}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}Current dungeon run is over 900 seconds. Proceeding for a new run. | Error In \"Start Killing Boss\"{Style.RESET_ALL}")
                    break

            pyautogui.leftClick()
            keyboard.press_and_release('f1')
            time.sleep(0.8)

            if pyautogui.locateOnScreen("Epochal Integration.png", confidence=0.8):
                print(f"{Fore.RED}Epochal Itegration is on Hand. Swapping Off.")
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True
            else:
                pyautogui.moveTo(700, 685)  # empty energy weapon
                time.sleep(0.1)
                pyautogui.moveTo(549, 685)
                time.sleep(0.1)
                pyautogui.leftClick()
                time.sleep(0.9)
                pyautogui.leftClick()
                time.sleep(0.1)

                if pyautogui.locateOnScreen("Glimmer.png", confidence=0.8):
                    is_boss_killed = True

            keyboard.press_and_release('f1')
            time.sleep(3)  # wait for weapon swap delay

            if is_boss_killed:
                print(f"{Fore.LIGHTYELLOW_EX}Boss is killed. Going for ghost finish{Style.RESET_ALL}")
                total_boss_killed += 1
                print(f"{Fore.LIGHTYELLOW_EX}Total Boss Killed: {total_boss_killed}{Style.RESET_ALL}")

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3500, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1000, 0, 0)
                time.sleep(1)
                keyboard.press('w')
                time.sleep(1)
                keyboard.release('w')
                keyboard.press('g')
                keyboard.press_and_release('space')
                time.sleep(0.1)
                keyboard.press_and_release('space')
                time.sleep(2)
                keyboard.release('g')
                is_boss_killed = False
                break

        keyboard.press_and_release('alt+tab')
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("Collect Postmaster.png", confidence=0.9)
            print("Collect Armors From Postmaster")
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick()
            time.sleep(1)
        except TypeError:
            time.sleep(1)
            pass
        keyboard.press_and_release('alt+tab')
        time.sleep(1)


def display_status():
    if is_master:
        print(f"{Fore.RED}Current AFK Timer: {round(time.time() - afk_timer)}{Style.RESET_ALL}")
    print(f"{Fore.RED}Current Runtime: {round(time.time() - runtime)}{Style.RESET_ALL}")
    print(f"{Fore.RED}Total Bosses Killed: {total_boss_killed}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed Runs at \"Waiting For Empowering Rift Buff\": {failed_runs_at_waitingforempoweringriftbuff}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed Runs at \"Waiting For Revive\": {failed_runs_at_waitingforrevive}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed Runs at \"Start Killing Boss\": {failed_runs_at_startkillingboss}{Style.RESET_ALL}")


def execute_warlock():
    t = threading.Thread(target=warlock)
    print("You're currently executing Warlock script")
    t.start()


def execute_hunter():
    t = threading.Thread(target=hunter)
    print("You're currently executing Hunter script")
    t.start()


def execute_titan():
    t = threading.Thread(target=titan)
    print("You're currently executing Titan script")
    t.start()


while True:
    keyboard.add_hotkey('f6', execute_titan)
    keyboard.add_hotkey('f7', execute_hunter)
    keyboard.add_hotkey('f8', execute_warlock)
    keyboard.add_hotkey('f10', display_status)
    keyboard.wait('f9')
    keyboard.release('space')
    keyboard.release('shift+w')
    keyboard.release('alt+tab')
    sys.exit("Elapsed Time: " + str(round(time.time() - startTime)) + " seconds | "
             + str(round((time.time() - startTime) / 60, 2)) + " minutes | "
             + str(round((time.time() - startTime) / 3600, 2)) + " hours")
