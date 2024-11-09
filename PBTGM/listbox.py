from tkinter import *

Lop = Tk()
Lb = Listbox(Lop)  
Lb.insert(1, 'python')
Lb.insert(2, 'java')
Lb.insert(3, 'c++')
Lb.insert(4, 'php')
Lb.pack()
Lb.mainloop()