from operator import truediv
import pyautogui, random, time
from tkinter import *
print('Press Ctrl-C to quit.')
pyautogui.FAILSAFE = False

mouse=True

def mover():
    pyautogui.hotkey('Win', 'd')
    while mouse==True:
        posicao1 = random.randint(1,1000)
        posicao2 = random.randint(1,1000)
        tempo = random.randint(2,10)
        arrastar = random.randint(1,5)
        pyautogui.moveTo(posicao1, posicao2, duration=arrastar)
        pyautogui.leftClick()
        time.sleep(tempo)
    return

def parar():
    return mouse==False

master = Tk()
master.geometry("180x160")

master.configure(bg='light grey')

Button(master, text="Mover Mouse", command=mover).place(x=40, y=30)
Button(master, text="Parar Mouse", command=parar).place(x=40, y=80)

mainloop()

