import pyautogui, random, time
print('Press Ctrl-C to quit.')
pyautogui.FAILSAFE = False


try:
    while True:
        pyautogui.hotkey('Win','d')
        posicao1 = random.randint(1,1000)
        posicao2 = random.randint(1,1000)
        tempo = random.randint(2,10)
        arrastar = random.randint(1,5)
        pyautogui.moveTo(posicao1, posicao2, duration=arrastar)
        pyautogui.leftClick()
        time.sleep(tempo)
except KeyboardInterrupt:
    print('\n')
