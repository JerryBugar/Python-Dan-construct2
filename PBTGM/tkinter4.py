#latihan tkinter 4
from tkinter import *

master = Tk()
label = Label(master, text="first name").grid(row=0)
label = Label(master, text="last name").grid(row=1)
a1 = Entry(master)
a2 = Entry(master)
a1.grid(row=0, column=1)
a2.grid(row=1, column=1)

mainloop()
