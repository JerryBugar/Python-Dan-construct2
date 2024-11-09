import tkinter
main_windows = tkinter.Tk()
label1 = tkinter.Label(main_windows, text= "label1")
label2 = tkinter.Label(main_windows, text= "label2")
tombol1 = tkinter.Button(main_windows, text= "tombol1")
tombol2 = tkinter.Button(main_windows, text= "tombol2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_windows.mainloop()