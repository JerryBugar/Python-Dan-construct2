from tkinter import *
import combobox  # Mengimpor combobox.py

root = Tk()  # Inisialisasi Tk() harus dilakukan sebelum memanggil fungsi
menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)  # Pastikan 'file' didefinisikan sebelum digunakan
menu.add_cascade(label="File", menu=file)

def open_combobox_window():  # Definisikan fungsi di atas
    print("open_combobox_window dipanggil")  # Tambahkan print untuk debugging
    combobox.create_combobox(root)  # Tampilkan jendela combo_box

file.add_command(label="New", command=open_combobox_window)  # Menambahkan perintah untuk tombol New
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

root.mainloop()  
