import tkinter as tk

r = tk.Tk()
r.title("counting second")
button = tk.Button(r, text="Berhenti", width=25, command=r.destroy)
button.pack()

r.mainloop()