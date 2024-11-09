import tkinter as tk
from tkinter import messagebox

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
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Menambahkan event handler untuk tombol submit
submit_button.bind("<Button-1>", lambda event: messagebox.showwarning("Input Error", "Semua field harus diisi!") if not entry_nama.get() or not entry_kelas.get() or not entry_jurusan.get() or not entry_hobi.get() else messagebox.showinfo("Data Diterima", f"Nama: {entry_nama.get()}\nKelas: {entry_kelas.get()}\nJurusan: {entry_jurusan.get()}\nHobi: {entry_hobi.get()}"))

# Menjalankan aplikasi
root.mainloop()