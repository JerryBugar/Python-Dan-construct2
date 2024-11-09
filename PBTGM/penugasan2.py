from tkinter import *

root = Tk()

w1 = Label(root, text="Username").grid(row=0, column=0)
e1 = Entry(root).grid(row=0, column=1)
w2 = Label(root, text="Password").grid(row=1, column=0)
e2 = Entry(root, show="*").grid(row=1, column=1)
w3 = Label(root, text="Nama").grid(row=2, column=0)
e3 = Entry(root).grid(row=2, column=1)
w4 = Label(root, text="Kelas").grid(row=3, column=0)

var1 = IntVar()
Checkbutton(root, text='TKJ', variable=var1).grid(row=3, column=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text='TAV', variable=var2).grid(row=3, column=2, sticky=W)
var3 = IntVar()
Checkbutton(root, text='RPL', variable=var3).grid(row=4, column=1, sticky=W)
var4 = IntVar()
Checkbutton(root, text='TMO', variable=var3).grid(row=4, column=2, sticky=W)

w5 = Label(root, text="Jurusan").grid(row=5, column=0)


root.mainloop()