#https://www.youtube.com/watch?v=FQ1exJhqvo0
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("kmisaria Zanuto")
root.geometry("600x400")
root.iconbitmap("images/icon.ico")

aba = ttk.Notebook(root)
aba.place(x=0, y=0, width=600, height=400)

menu1 = Frame(aba)
aba.add(menu1, text="  Matriz      ")

menu2 = Frame(aba)
aba.add(menu2, text="  Filial SP   ")

menu3 = Frame(aba)
aba.add(menu3, text="  Filial SC   ") 

menu4 = Frame(aba)
aba.add(menu4, text="  Estoque     ")

menu5 = Frame(aba)
aba.add(menu5, text="  Compras     ")

menu6 = Frame(aba)
aba.add(menu6, text="  Vendas      ")

menu7 = Frame(aba)
aba.add(menu7, text="  Financeiro  ")

menu8 = Frame(aba)
aba.add(menu8, text="  Cliente     ")






root.mainloop()
