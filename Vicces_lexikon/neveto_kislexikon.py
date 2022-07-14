from random import randrange
from tkinter import *

win = Tk()
win.title("Nevető kislexikon")
win.configure(background="gray")

dict = []
with open("szotar.txt", "r", encoding="utf-8") as file:
    for sor in file:
        i = sor.index(chr(9))
        word = sor[:i]
        definition = sor[i+1:]
        dict += [[word, definition.strip()]]


def click():
    rand = randrange(len(dict))
    word.delete(0.0, END)
    word.insert(END, dict[rand][0])
    definition.delete(0.0, END)
    definition.insert(END, dict[rand][1])

Label(win, text="Mindent megmagyarázok!", width=23, bg="black", fg="white", font="none 15 bold").grid(row=0, column=0)
photo = PhotoImage(file="banana.gif")
Label(win, image=photo, bg="black").grid(row=1, column=0)
Button(win, text="Új szó", width=40, relief="ridge", command=click, bg="orange", fg="black").grid(row=2, column=0)
word = Text(win, width=35, height=1, background="black", foreground="white")
word.grid(row=3, column=0)
definition = Text(win, width=35, height=7, wrap=WORD, background="white", foreground="black")
definition.grid(row=4, column=0)

win.mainloop()
