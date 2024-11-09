from tkinter import *

master = Tk()

Label(master, text='Username').grid(row=0)
Label(master, text='Password').grid(row=1)
Label(master, text='Nama').grid(row=2)
Label(master, text='Kelas').grid(row=3)

var1 = IntVar()
Checkbutton(master, text='RPL', variable=var1).grid(row=3, column=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text='TKJ', variable=var2).grid(row=4, column=1, sticky=W)
var3 = IntVar()
Checkbutton(master, text='EPU', variable=var3).grid(row=3, column=2, sticky=W)
var4 = IntVar()
Checkbutton(master, text='TKR', variable=var4).grid(row=4, column=2, sticky=W)


Label(master, text='Jurusan').grid(row=5)
var_jurusan = IntVar()
Radiobutton(master, text='TEKNIK INFORMATIKA', variable=var_jurusan, value=1).grid(row=5, column=1, sticky=W)
Radiobutton(master, text='TEKNIK OTOMOTIF', variable=var_jurusan, value=2).grid(row=6, column=1, sticky=W)
Radiobutton(master, text='TENIK JARINGAN', variable=var_jurusan, value=3).grid(row=7, column=1, sticky=W)
Radiobutton(master, text='PENERBANGAN', variable=var_jurusan, value=4).grid(row=8, column=1, sticky=W)


Label(master, text='Alamat').grid(row=10)
Label(master, text='Sekolah').grid(row=11)

Button(master, text='SIMPAN').grid(row=12)
Button(master, text='BATAL').grid(row=12, column=1)
Button(master, text='KELUAR').grid(row=12, column=2)

e1 = Entry(master)
e2 = Entry(master, show='*')
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=10, column=1)
e5.grid(row=11, column=1)

mainloop()