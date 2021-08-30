import tkinter
from tkinter import *


win = tkinter.Tk()
win.title("Python GUI")
win.resizable(0, 0)
win.geometry("500x500")

# Create a menu bar


def nothing():
    file = Toplevel(win)
    file.geometry("300x300")
    file.title("File")
    button = Button(file, text="Do thing here")
    button.pack()


menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=nothing)
filemenu.add_command(label="Open", command=nothing)
filemenu.add_command(label="Save", command=nothing)
filemenu.add_command(label="Save as...", command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=nothing)
menubar.add_cascade(label="Help", menu=helpmenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=nothing)
editmenu.add_command(label="Cut", command=nothing)
editmenu.add_command(label="Copy", command=nothing)
editmenu.add_command(label="Paste", command=nothing)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=nothing)
editmenu.add_command(label="Select All", command=nothing)
menubar.add_cascade(label="Edit", menu=editmenu)


def quit():
    win.quit()
    win.destroy()
    exit()


# Create a button
action = tkinter.Button(win, text="Quit", command=quit)
action.pack()

win.config(menu=menubar)
win.mainloop()
