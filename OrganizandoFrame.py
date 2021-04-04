from tkinter import *

root = Tk()
root.title("App")

frame_nome = Frame(root)
frame_morada = Frame(root)
  
label_nome = Label(frame_nome, text="Nome : ")
label_apelido = Label(frame_nome, text="Apelido : ")
label_rua = Label(frame_morada, text="Rua : ")
label_cidade = Label(frame_morada, text="Cidade : ")

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)

text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

cmd_salvar=Button(root, text="Salvar",bg="#40ff00", fg="black")

label_nome.grid(row=0, column=0)
label_apelido.grid(row=1, column=0)
text_nome.grid(row=0, column=1)
text_apelido.grid(row=1, column=1)

label_rua.grid(row=0, column=0)
label_cidade.grid(row=1, column=0)
text_rua.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)

cmd_salvar.grid(column=1, sticky='we')

root.mainloop()