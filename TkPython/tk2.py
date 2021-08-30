import tkinter
from tkinter import *

win = tkinter.Tk()
win.title("Python GUI")
win.resizable(0, 0)
win.geometry("500x500")

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)

list = Listbox(win, yscrollcommand=scrollbar.set)

for line in range(100):
    list.insert(END, "This is line number " + str(line))

list.pack()


win.mainloop()
