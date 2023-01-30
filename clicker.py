from tkinter import *
import tkinter as tk
import time

canvas = tk.Tk()
canvas.title("clicker")
canvas.geometry("400x150")
canvas.config(bg = '#A65AF2')


def uiPrint(): #not currently used
    print("")
    print(click)

click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")

label = tk.Label(canvas, text="0")
label.config(font = ('ds-digital', 15))
label.pack() #its 1am why am i doing this to myself
titleachieve = tk.Label(canvas, text="Achievements:")
titleachieve.pack()
titleachieve.config(font = (14))

achieve = tk.Label(canvas, text="")
achieve.pack()
achieve.config(width=45, font = (14))

def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    label.config(text=str(click))
    if click == 100:
        achieve.config(text='''Achievement Unlocked: Junior Clicker!
        BONUS 100 clicks!''')
        click += 100

    elif click == 400:
        achieve.config(text='''Achievement Unlocked: Little Ninja Clicks!
        BONUS 200!''')
        click += 300

    elif click == 1500:
        achieve.config(text='''Achievement Unlocked: Click Ninja Master!
        QUAD CLICKS!''')
        mult = mult * 4

    elif click == 3000:
        achieve.config(text='''Achievement Unlocked:  Jackie Chan Style!
        8 TIMES THE CLICKS!''')
        mult = mult * 8

mainClickButton = Button(canvas, text="Click!", command = buttonCommand)
mainClickButton.pack()

canvas.mainloop()
