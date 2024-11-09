import tkinter as tk

def on_button_click():
    print("Tombol diklik!")

def connect_vpn():
    print("Menghubungkan ke VPN...")

def disconnect_vpn():
    print("Memutuskan koneksi VPN...")

root = tk.Tk()
root.title("Aplikasi VPN")
root.geometry("300x200")  # Menentukan ukuran jendela
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang

label = tk.Label(root, text="Halo, Aplikasi VPN!", bg="#f0f0f0", font=("Arial", 14))
label.pack(pady=10)  # Menambahkan padding vertikal

connect_button = tk.Button(root, text="Hubungkan VPN", command=connect_vpn, bg="#4CAF50", fg="white", width=20)
connect_button.pack(pady=5)  # Menambahkan padding vertikal

disconnect_button = tk.Button(root, text="Putuskan VPN", command=disconnect_vpn, bg="#f44336", fg="white", width=20)
disconnect_button.pack(pady=5)  # Menambahkan padding vertikal

root.mainloop()