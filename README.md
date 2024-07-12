All scripts support 2560x1440 resolution. Scripts that only use keyboard inputs can be used with any resolution.

## Library Versions
 - PyScreeze: 0.1.27
 - PyAutoGUI: 0.9.50
    - PyAutoGUI newer versions doesn't allow image checks by using if pyautogui.locateOnScreen() when image is not present on screen, it will throw an exception.
 - opencv-python: 4.9.0.80
 - pillow: 10.3.0 


## Scripts that support both 1920x1080 and 2560x1440:
 - AFK Exotic Class Item Farm (V2, V3, V4)
 - AFK Warlords Ruin First Boss Farm
 - Internet Error Fix
 - Spam Join


 ## Steps to Package Executables
  0. Ensure the script's code supports exe packaging
   - Image path needs to be dynamically determined if the script is running as a bundled executable or in development
  1. Open Auto Py To Exe
  2. Locate the .py script file in **Script Location**
  3. Under **Onefile**, set "One File"
  4. Under **Console Window**, set "Console Based"
  5. Under **Additional Files**, add in "Destiny_2_Scripts" folder
  6. Under **Settings**, change "Output Directory"
  7. After EXE has finished packaging, make a copy of "Destiny_2_Scripts" folder with the packaged EXE to a new location
  8. In the newly copied "Destiny_2_Scripts" folder, remove any folders that are not used for the script's exeuction and all image folders, leaving only the EXE and Python Source Files that are used in imports
  9. The remaining are all that's necessary to use the EXE.

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
   - Additional Video
      - Render Resolution: 100
 - Gameplay
   - HUD Opacity: Full (Default)
   - Colorblind Mode: Off
