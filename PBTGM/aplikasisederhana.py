import tkinter as tk
from tkinter import messagebox

def submit():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    jurusan = entry_jurusan.get()
    hobi = entry_hobi.get()
    
    if not nama or not kelas or not jurusan or not hobi:
        messagebox.showwarning("Input Error", "Semua field harus diisi!")
    else:
        messagebox.showinfo("Data Diterima", f"Nama: {nama}\nKelas: {kelas}\nJurusan: {jurusan}\nHobi: {hobi}")

# Membuat jendela utama
root = tk.Tk()
root.title("Formulir Data Siswa")

# Membuat label dan entry untuk Nama
tk.Label(root, text="Nama:").grid(row=0, column=0, padx=10, pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Kelas
tk.Label(root, text="Kelas:").grid(row=1, column=0, padx=10, pady=5)
entry_kelas = tk.Entry(root)
entry_kelas.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Jurusan
tk.Label(root, text="Jurusan:").grid(row=2, column=0, padx=10, pady=5)
entry_jurusan = tk.Entry(root)
entry_jurusan.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Hobi
tk.Label(root, text="Hobi:").grid(row=3, column=0, padx=10, pady=5)
entry_hobi = tk.Entry(root)
entry_hobi.grid(row=3, column=1, padx=10, pady=5)

# Membuat tombol submit
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()