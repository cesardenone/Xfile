import pyautogui, random, time
from tkinter import *
pyautogui.FAILSAFE = False

mouse=False

def mover(mouse):
    #pyautogui.hotkey('Win', 'd')#
    while mouse==True:
        posicao1 = random.randint(1,1000)
        posicao2 = random.randint(1,1000)
        tempo = random.randint(2,10)
        arrastar = random.randint(1,5)
        pyautogui.moveTo(posicao1, posicao2, duration=arrastar)
        #pyautogui.leftClick()#
        time.sleep(tempo)
    return

app = Tk()
app.title("Never Sleep")
app.geometry("250x150")
app.configure(background="#000")

text1=Button(app, text="Mouse Moving", activebackground="#999", command=mover(True))
text1.place(x=80, y=40, width=100, height=30)
text2=Label(app, text="Ctrl+C to stop", background="#000", foreground="#999")
text2.place(x=80, y=80, width=100, height=30)

app.mainloop()
