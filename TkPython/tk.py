from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Python GUI")
win.geometry("400x400")


# Create a label
label = Label(win, text="This is a label")
label.pack()
# Create a button and print welcome message to it


def print_hello():
    print("Hello you click on Button1")


def welcome_message():
    messagebox.showinfo("Welcome", "Welcome to Python GUI")


button = Button(win, text="Click Me", activeforeground="red",
                command=welcome_message)
button.pack()
button1 = Button(win, text="Click Me1", command=print_hello,
                 bg="red", fg="white", padx=20, pady=20)
button1.pack()
c = Canvas(win, width=400, height=300, bg="grey")
coord = 10, 50, 240, 210
are = c.create_arc(coord, start=0, extent=150, fill="red")
line = c.create_line(10, 10, 200, 200, fill="yellow")
c.pack()


win.mainloop()
