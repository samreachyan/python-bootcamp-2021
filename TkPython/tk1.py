from tkinter import *
from functools import partial

win = Tk()
win.title("Python GUI")
win.resizable(0, 0)
win.wm_attributes("-topmost", 1)
win.geometry("500x300")


def sum(label, a, b):
    n1 = int(a.get())
    n2 = int(b.get())
    sum = n1 + n2
    label.config(text="Sum = " + str(sum))


# Labels
l1 = label1 = Label(win, text="First Number")
l1.grid(row=0, column=0)
l2 = label2 = Label(win, text="Second Number")
l2.grid(row=1, column=0)
label = Label(win)
label.grid(row=3, column=0)

x1 = StringVar()
x2 = StringVar()
# Entries (Text Fields)
e1 = Entry(win, textvariable=x1)
e1.grid(row=0, column=1)
e2 = Entry(win, textvariable=x2)
e2.grid(row=1, column=1)

sum = partial(sum, label, x1, x2)
b1 = Button(win, text="Sum", command=sum)
b1.grid(row=2, column=0)
b2 = Button(win, text="Quit", command=win.quit)
b2.grid(row=2, column=1)

win.mainloop()
