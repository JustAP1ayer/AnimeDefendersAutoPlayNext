import os
import time
try:
    import pyautogui
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install opencv-python")

print("Auto Clicker Activated!")
while True:
    autonext = pyautogui.locateCenterOnScreen('next.png', confidence=0.75)
    if autonext:
        pyautogui.moveTo(autonext)
        time.sleep(0.06)
        pyautogui.click()
        print(f"Clicked 'next' button at {autonext}")
    else:
        time.sleep(0.1)
