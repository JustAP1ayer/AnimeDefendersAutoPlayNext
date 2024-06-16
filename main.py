import os
import time
import json
try:
    import pyautogui
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install opencv-python")
with open("config.json", "r") as config_file:
    config = json.load(config_file)
buttonchosen = config["button"]
print(f"Auto Clicker Activated! Waiting for the '{buttonchosen}' button.")
while True:
    if buttonchosen == "Next":
        button = pyautogui.locateCenterOnScreen('next.png', confidence=0.75)
    else:
        button = pyautogui.locateCenterOnScreen('replay.png', confidence=0.75)
    if button:
        pyautogui.moveTo(button)
        time.sleep(0.06)
        pyautogui.click()
        print(f"Clicked '{buttonchosen}' button at {button}")
    else:
        time.sleep(0.1)
