import tkinter as tk
from tkinter import ttk

def create_combobox(root):
    def on_select(event):
        selected_item = combo_box.get()
        label.config(text="selected item: " + selected_item)

    # Membuat label
    label = tk.Label(root, text="pilih item")
    label.pack(pady=10)

    combo_box = ttk.Combobox(root)  
    combo_box['values'] = ("Gia Revaldo", "Alya Putri", "Budi Santoso", "Citra Dewi", "Doni Prabowo", 
                            "Eka Lestari", "Fajar Nugraha", "Gina Sari", "Hendra Wijaya", "Ika Amelia")
    combo_box.pack(pady=10)  
    combo_box.set("data siswa")

    # Bind event to selection
    combo_box.bind("<<ComboboxSelected>>", on_select)
