
import os
try:
    import pyautogui, time, keyboard
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install keyboard")

print("Auto Clicker Activated!")
while True:
    autonext = pyautogui.locateCenterOnScreen('next.png', confidence=0.9)
    if autonext:
        pyautogui.moveTo(autonext)
        time.sleep(0.06)
        pyautogui.click()
        print(f"Clicked buy button on {autonext}")
    else:
    time.sleep(0.1)
    
