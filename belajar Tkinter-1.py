#belajar membuat program GUI menggunakan modul tkinter
import tkinter as myGUI
root = myGUI.Tk()
w = myGUI.Label(root,text="Hello World") #pembuatan widget label
x = myGUI.Button(root,text="Click Here") #pembuatan widget Butoon / tombol
w.pack()
x.pack()
root.mainloop()