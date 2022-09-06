import pyautogui, random, time

mouse = bool(False)

def move():
    mouse = bool(True)
    while mouse == True:
        p1 = random.randint(1, 1000)
        p2 = random.randint(1, 1000)
        timeline = random.randint(2, 10)
        roll = random.randint(1, 5)
        pyautogui.moveTo(p1, p2, duration=roll)
        #pyautogui.leftClick()
        time.sleep(timeline)
    return