import tkinter
from tkinter import *

pw = PanedWindow()
pw.pack(fill=BOTH, expand=1)
left = Entry(pw, bd=5)
pw.add(left)

pw2 = PanedWindow(pw, orient=VERTICAL)
pw.add(pw2)
s = Scale(pw2, orient=HORIZONTAL)
pw2.add(s)

b = Button(pw2, text="OK", width=10)
pw2.add(b)

mainloop()
