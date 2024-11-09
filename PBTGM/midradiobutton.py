from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text='rpl', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='tkj', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='te', variable=v, value=3).pack(anchor=W)
Radiobutton(root, text='tmo', variable=v, value=4).pack(anchor=W)

mainloop()