from tkinter import *

root = Tk()
root.title("K.Z")
root.iconbitmap("images/icon.ico")
root.geometry("200x110")

def form():
    nome = box.get()
    lab_f = Label(root, text="O teu nome:\n " + nome)
    lab_f.grid()

lab = Label(root, text="Escreva o teu nome e: ", font =" times 12 italic " )
box = Entry(root, width=30)
bt = Button(root, text="Executar", command=form)

lab.grid(row=0, stick=W)
box.grid(row=1, columnspan=3,stick=W)
bt.grid(row= 2, columnspan=3, stick="we")

root.mainloop()