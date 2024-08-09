import sys
import time
from colorama import Fore, Style

character_to_select = ""
activity_type = ""
activity_name = ""


def prompt_character_selection_instruction():
    global character_to_select

    acceptable_inputs = {"1", "2", "3"}
    character_to_select_dictionary = {
        "1": "First",
        "2": "Second",
        "3": "Third",
    }

    # Black Formatter formats these to a single line if printed in input(), which looks kinda. So, it's staying this way for now
    print("Which character would you like to use to hold checkpoints?")
    print(" - First (1)")
    print(" - Second (2)")
    print(" - Third (3)")
    character_to_select = input(f"{Fore.GREEN}")

    # If input is accetable, convert the number input to words wit the dictionary
    if character_to_select in acceptable_inputs:
        character_to_select = character_to_select_dictionary[character_to_select]
        print(f"You have selected: {character_to_select}")

    # Otherwise reprompt the user
    else:
        print(f"{Fore.RED}Invalid! Your input is: {character_to_select}{Style.RESET_ALL}")
        prompt_character_selection_instruction()
        return

    print(f"{Style.RESET_ALL}")


def prompt_activity_type_instruction():
    global activity_type

    acceptable_activity_types = {"1", "2"}
    activity_type_dictionary = {
        "1": "Raid",
        "2": "Dungeon",
    }

    print("Which of the following activity type would you like to access?")
    print(" - Raid (1)")
    print(" - Dungeon (2)")
    activity_type = input(f"{Fore.GREEN}")

    # If input is accetable, convert the number input to words wit the dictionary
    if activity_type in acceptable_activity_types:
        activity_type = activity_type_dictionary[activity_type]
        print(f"You have selected: {activity_type}")

    # Otherwise reprompt the user
    else:
        print(f"{Fore.RED}Invalid! Your input is: {activity_type}{Style.RESET_ALL}")
        prompt_activity_type_instruction()
        return

    print(f"{Style.RESET_ALL}")


def prompt_activity_name_instruction():
    global activity_name

    if activity_type == "Raid":
        print("There are no Raids available currently.")
        time.sleep(3)
        sys.exit()

    elif activity_type == "Dungeon":
        acceptable_activity_names = {"1"}
        activity_name_dictionary = {
            "1": "The Shattered Throne",
        }

        print("Which of the following activities would you like to access?")
        print(" - The Shattered Throne (1)")

    activity_name = input(f"{Fore.GREEN}")

    # If input is accetable, convert the number input to words wit the dictionary
    if activity_name in acceptable_activity_names:
        activity_name = activity_name_dictionary[activity_name]
        print(f"You have selected: {activity_name}")

    # Otherwise reprompt the user
    else:
        print(f"{Fore.RED}Invalid! Your input is: {activity_name}{Style.RESET_ALL}")
        prompt_activity_name_instruction()
        return

    print(f"{Style.RESET_ALL}")


def show_final_results():
    print(f"{Fore.GREEN}You have selected: ")
    print(f" - Character: {character_to_select}")
    print(f" - Activity Type: {activity_type}")
    print(f" - Activity: {activity_name}")
    print(f"{Style.RESET_ALL}")
