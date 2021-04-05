from tkinter import *

root = Tk()
root.title("K.Z")
root.iconbitmap("images/icon.ico")
root.geometry("250x250")

meuMenu = Menu(root)

def filenew_click():
    print("FileNew_click")
#Menu File
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="Mew",command=filenew_click)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
meuMenu.add_cascade(label="file", menu=fileMenu)   
#Menu Edit
fileEdit = Menu(meuMenu, tearoff=0)
fileEdit.add_command(label="Copy",)
fileEdit.add_command(label="Paste")
fileEdit.add_command(label="Select All")

meuMenu.add_cascade(label="Edit", menu=fileEdit)   

root.config(menu=meuMenu)

root.mainloop()