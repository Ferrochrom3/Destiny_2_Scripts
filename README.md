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
  1. Locate .py script file in Script Location
  2. Under Onefile, set "One File"
  3. Under Console Window, set "Console Based"
  4. Under Additional Files, add in Destiny_2_Scripts folder.
  5. Under Settings, change "Output Directory"
  6. After EXE is finished packaging, copy and past "Destiny_2_Scripts" to a new location
  7. Remove any folders that are not used in the script and all image folders, leaving only the EXE and Python Source Files that are used in imports.
  8. The remaining are all that's necessary to use the EXE.
