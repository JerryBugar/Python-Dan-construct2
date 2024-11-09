from tkinter import *
main = Tk()
ourmessage = 'pesanku pesanmu'
messagevar = Message(main, text=ourmessage)  # Menggunakan 'Message' dengan huruf kapital
messagevar.config(bg="lightcoral")
messagevar.pack()
mainloop()
