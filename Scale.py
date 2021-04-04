from tkinter import *

root = Tk()
root.title("KZ")
root.iconbitmap("images/icon.ico")
root.geometry("250x250")

def vervalor():
    print(slide.get())


slide = Scale(root,
 from_=0,
 to=100,
 orient=HORIZONTAL,resolution=0.1)
slide.pack()
 
cmd=Button(root, text="Ver Valor", command=vervalor)
cmd.pack() 
 







root.mainloop()
