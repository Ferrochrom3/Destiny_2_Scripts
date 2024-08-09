All scripts support 2560x1440 resolution. Scripts that only use keyboard inputs can be used with any resolution.

## Library Versions
 - PyScreeze: 0.1.27
 - PyAutoGUI: 0.9.50
    - PyAutoGUI newer versions doesn't allow image checks by using if pyautogui.locateOnScreen() when image is not present on screen, it will throw an exception.
 - opencv-python: 4.9.0.80
 - pillow: 10.3.0 

## Scripts that support both 1920x1080 and 2560x1440:
 - All scripts that only use keyboard inputs
 - AFK Exotic Class Item Farm (V2, V3, V4)
 - AFK Warlords Ruin First Boss Farm
 - Internet Error Fix
 - Spam Join
 - AFK Silver Leaves Farm

## In-Game Settings (anything not mentioned will be default)
 - Keybinds
   - Mouse
      - Look Sensitivity: 7
      - ADS Sensitivtiy Modifier 1.0
   - Keyboard
      - Interact: Alt
      - Uncharged Melee: C
      - Charged Melee: Mouse 5
 - Video
   - Video
      - Field of View: 105
      - Screen Bounds: Set the bounds to max, covering the entire screen
 - Gameplay
   - HUD Opacity: Full (Default)
   - Colorblind Mode: Off

 ## Steps to Package Executables
  0. Ensure the script's code supports exe packaging
   - Image path needs to be dynamically determined if the script is running as a bundled executable or in development
  1. Make a copy of "Destiny_2_Scripts" folder
  2. In the newly copied "Destiny_2_Scripts" folder, remove any folders that are not used for the script's exeuction, leaving only the Python Source Files that are used in imports and any image folders.
  3. Open Auto Py To Exe in Command Prompt with `auto-py-to-exe`
  4. Locate the .py script file in **Script Location**
  5. Under **Onefile**, set "One File"
  6. Under **Console Window**, set "Console Based" (if not already)
  7. Under **Additional Files**, add in "Destiny_2_Scripts" folder and all Python Source Files that are used
  8. Under **Settings**, change "Output Directory"
  9. Convert .py to .exe
  10. Remove all source files and image folders, only the EXE is needed.
