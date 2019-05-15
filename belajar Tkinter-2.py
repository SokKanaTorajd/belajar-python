#memasukkan gambar/gif kedalam GUI
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="D:/Documents/Sistem Infomasi/Konsep Pemrograman/Wizard-Clap-by-Markus-Magnusson.gif") #menggunakan widget PhotoImage
tk.Label(root, image=logo).pack(side="right")
explanation = "I'am a GRANDPA"
tk.Label(root, justify=tk.CENTER, padx = 10, text=explanation).pack(side="bottom")

root.mainloop()