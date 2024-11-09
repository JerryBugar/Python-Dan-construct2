from tkinter import Tk, Label, Entry, Button

root = Tk()
w1 = Label(root, text="Nama").grid(row=0, column=0)
e1 = Entry(root).grid(row=0, column=1)
w2 = Label(root, text="Kelas").grid(row=1, column=0)
e2 = Entry(root).grid(row=1, column=1)
w3 = Label(root, text="Jurusan").grid(row=2, column=0)
e3 = Entry(root).grid(row=2, column=1)
w4 = Label(root, text="Sekolah").grid(row=3, column=0)
e4 = Entry(root).grid(row=3, column=1)
w5 = Label(root, text="Alamat").grid(row=4, column=0)
e5 = Entry(root).grid(row=4, column=1)
w6 = Label(root, text='Username').grid(row=5, column=0)
e6 = Entry(root).grid(row=5, column=1)
w7 = Label(root, text="Password").grid(row=6, column=0)
e7 = Entry(root, show="*").grid(row=6, column=1)


button1 = Button(root, text="MASUK", width=10, command=root.destroy).grid(row=7, column=0)
button2 = Button(root, text="BATAL", width=10, command=root.destroy).grid(row=7, column=1)

root.mainloop()