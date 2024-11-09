#mid5
from tkinter import *

master = Tk()
label = Label(master, text='first name').grid(row=0)
label = Label(master, text='last name').grid(row=1)
label = Label(master, text='jurusan').grid(row=2)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

mainloop()