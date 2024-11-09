#latihan tkinter 3
import tkinter as tk

r = tk.Tk()
r.title("counting second")
button = tk.Button(r, text="stop", width=10, command=r.destroy)
button.pack()

r.mainloop()