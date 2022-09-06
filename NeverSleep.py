import pyautogui, random, time
from tkinter import *
import mover_mouse
pyautogui.FAILSAFE = False

app = Tk()
app.title("Never Sleep")
app.geometry("250x150")
app.configure(background="#000")

text1=Button(app, text="Mouse Moving", activebackground="#999", command=lambda: mover_mouse.move())
text1.place(x=80, y=40, width=100, height=30)

text2=Label(app, text="Press S to stop", background="#000", foreground="#999")
text2.place(x=80, y=80, width=100, height=30)

app.mainloop()
