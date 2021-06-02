#https://www.youtube.com/watch?v=FQ1exJhqvo0
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("kmisaria Zanuto")
root.geometry("510x370")
root.iconbitmap("images/icon.ico")
#root["bg"] = "#ffffcc"

aba = ttk.Notebook(root)
aba.place(x=0, y=0, width=520,height=380)

menu1 = Frame(aba)
aba.add(menu1, text="Cad.Cliente")
menu1["bg"] = "#d9f2e6"

cad_cli = Label(menu1, text="Cadastro de Cliente", bg="black", font="times 14 bold", fg="white", width=45)
cad_cli.grid(row=0, columnspan=7, stick=E)

#img = Label(menu1, bg="green", width=10, height=3)
#img.grid(row=13, column=6)

lb_id = Label(menu1, text="ID: ", bg="#d9f2e6", fg="red")
lb_id.grid(row=1, column=0)
box_id = Entry(menu1, width=6)
box_id.grid(row=1, column=1, stick=W)

lb_nome = Label(menu1, text="Nome: ", bg="#d9f2e6")
lb_nome.grid(row=3, column=0, stick=SE)
box_nome = Entry(menu1, width=20)
box_nome.grid(row=3, column=1, columnspan=2, stick=SE)

lb_snome = Label(menu1, text="S/n:  ", bg="#d9f2e6")
lb_snome.grid(row=3, column=3)
box_snome = Entry(menu1)
box_snome.grid(row=3, column=4, columnspan=5, stick="we")

lb_aniv = Label(menu1, text="Aniv.: ", bg="#d9f2e6")
lb_aniv.grid(row=4, column=0, stick="we")
box_aniv = Entry(menu1, width=15)
box_aniv.grid(row=4, column=1, stick=W)

lb_rg = Label(menu1, text="RG.: ", bg="#d9f2e6")
lb_rg.grid(row=4, column=3)
box_rg = Entry(menu1, width=20)
box_rg.grid(row=4, column=4, stick=W)

lb_cpf = Label(menu1, text="CPF: ", bg="#d9f2e6")
lb_cpf.grid(row=4, column=5)
box_cpf = Entry(menu1)
box_cpf.grid(row=4, column=6)

lb_end = Label(menu1, text="End.: ", bg="#d9f2e6")
lb_end.grid(row=5, column=0)
box_end = Entry(menu1)
box_end.grid(row=5, column=1, columnspan=5,stick="we")

lb_num = Label(menu1, text="Nº: ", bg="#d9f2e6")  
lb_num.grid(row=5, column=6)                      
box_num = Entry(menu1, width=5)
box_num.grid(row=5, column=6, stick=E)      

lb_compl = Label(menu1, text="Compl.: ", bg="#d9f2e6")
lb_compl.grid(row=6, column=0)
box_compl = Entry(menu1)
box_compl.grid(row=6, column=1, stick="we")

lb_cid = Label(menu1, text="Cid.:", bg="#d9f2e6")
lb_cid.grid(row=6, column=3)
box_cid = Entry(menu1)
box_cid.grid(row=6, column=4)

lb_bairro = Label(menu1, text="Bairro: ", bg="#d9f2e6")
lb_bairro.grid(row=6, column=5)
box_bairro = Entry(menu1)
box_bairro.grid(row=6, column=6)

lb_cep = Label(menu1, text="Est: ", bg="#d9f2e6")
lb_cep.grid(row=7, column=0)
box_cep = Entry(menu1)
box_cep.grid(row=7, column=1)

lb_uf = Label(menu1, text="UF",bg="#d9f2e6" )
lb_uf.grid(row=7, column=3 )
box_uf = Entry(menu1, width=5)
box_uf.grid(row=7, column=4, stick=W)

lb_email = Label(menu1, text="Email: ", bg="#d9f2e6")
lb_email.grid(row=7, column=4)
box_email = Entry(menu1, width=34)
box_email.grid(row=7, column=4, columnspan=7, stick=E)

lb_tel = Label(menu1, text="Tel.: ", bg="#d9f2e6")
lb_tel.grid(row=8, column=0)
box_tel = Entry(menu1)
box_tel.grid(row=8, column=1)

lb_cel = Label(menu1, text="Cel.: ", bg="#d9f2e6")
lb_cel.grid(row=8, column=3)
box_cel = Entry(menu1)
box_cel.grid(row=8, column=4)

lb_whats = Label(menu1, text="Whats: ", bg="#d9f2e6" )
lb_whats.grid(row=8, column=5)
box_whats = Entry(menu1)
box_whats.grid(row=8, column=6)

lb_risc = Label(menu1, text="**"*45, bg="#d9f2e6", fg="#d9f2e6")
lb_risc.grid(row=10, column=0, columnspan=7, stick="we")

lb_ref = Label(menu1, text="Como conheceu a Empresa? ", bg="#d9f2e6")
lb_ref.grid(row=11, column=0, columnspan=7, stick="we")

valor_a = IntVar()

rad_pass = Radiobutton(menu1, text="Passagem ", bg="#d9f2e6", variable=valor_a, value=1)
rad_pass.grid(row=12, column=1, stick=W)

rad_site = Radiobutton(menu1, text="Site ", bg="#d9f2e6", variable=valor_a, value=2)
rad_site.grid(row=13, column=1, stick=W)

rad_ind = Radiobutton(menu1, text="Indicação ", bg="#d9f2e6", variable=valor_a, value=3)
rad_ind.grid(row=14, column=1, stick=W)

rad_pass.select()
box_nome.focus()

cmd = Button(menu1, text="Salvar",bg="#39c639")
cmd.place(x=10, y=300, width=100, height=20)

menu2 = Frame(aba)
aba.add(menu2, text="  Cad.Produto  ")

lb_cadprod = Label(menu2, text="Cadastro de Produto")
lb_cadprod.grid()

#menu3 = Frame(aba)
#aba.add(menu3, text="   Senha   ") 

menu4 = Frame(aba)
aba.add(menu4, text="   Medidas   ")

aba1 = ttk.Notebook(root)
aba.place(x=0, y=0, width=520,height=380)

menu2 = Frame()
aba1.add(menu2, text="Cad.Cliente")
menu1["bg"] = "#d9f2e6"

def fileNew(menu2:
      print(fileNew)

menu2  = Menu(menu2)
#Menu File
browse = Menu(menu1, tearoff=0)
browse.add_command(label="Mew",command=fileNew)
browse.add_command(label="Open")
browse.add_command(label="save")
browse.add_separator()
browse.add_command(label="Exit")
show.add_cascade(label="File", menu2=browse) 

v_relief = Label(menu2, relief="solid", bg="#deb887",  bd=1, width=5, height=2)
v_relief.place(x=12, y=4)
valor_a = IntVar()
valor_b = IntVar()
valor_c = IntVar()
valor_d = IntVar()
Label(menu2,bg="#A52A2A").place(x=55, y=20, width=250, height=18)
Label(root, width=1,
      text="Tipo de Colarinho", bg="#A52A2A", font="Times 10 bold italic",
       fg="white").place(x=100, y=21, width=100, height=16)
rad_1 = Radiobutton(menu2, text="Itáliano ", variable=valor_a, value=1,
 bg="#deb887")
rad_2 = Radiobutton(menu2, text="Inglês ", variable=valor_a, value=2,
 bg="#deb887")
rad_3 = Radiobutton(menu2, text="Chanfrado ", variable=valor_a, value=3,
 bg="#deb887")
rad_4 = Radiobutton(menu2, text="Gola de Padre ", variable=valor_a,
 value=4, bg="#deb887")
rad_5 = Radiobutton(menu2, text="París ", variable=valor_a,
 value=5, bg="#deb887")
rad_6 = Radiobutton(menu2, text="Monaco ", variable=valor_a,
 value=6, bg="#deb887")
rad_7 = Radiobutton(menu2, text="indisor ", variable=valor_a,
 value=7, bg="#deb887")
rad_8 = Radiobutton(menu2, text="Douglas ", variable=valor_a,
 value=8, bg="#deb887")
rad_9 = Radiobutton(menu2, text="U.S.A ", variable=valor_a,
 value=9, bg="#deb887")
rad_1.select()

rad_1.place(x=10, y=45)
rad_2.place(x=10, y=65)
rad_3.place(x=10, y=85)
rad_4.place(x=100, y=45)
rad_5.place(x=100, y=65)
rad_6.place(x=100, y=85)
rad_7.place(x=200, y=45)
rad_8.place(x=200, y=65)
rad_9.place(x=200, y=85)
rad_1.select()

Label(root,
      text="Tipo de Frente", font="times 10 bold italic",
      bg="#A52A2A", fg="white").place(x=1, y=110, width=300, height=18)

rad_1 = Radiobutton(menu2, text="Frente Lisa", variable=valor_b, value=1,
 bg="#deb887")
rad_2 = Radiobutton(menu2, text="Frente Dupla", variable=valor_b, value=2,
 bg="#deb887")
rad_1.place(x=10, y=130)
rad_2.place(x=10, y=150)
rad_1.select()

Label(root, text="Bordado", font="times 10 bold italic", bg="#A52A2A",
      fg="white").place(x=1, y=185, width=300, height=18)
lb_1 = Radiobutton(menu2, text="Sim", variable=valor_c , value=1, bg="#deb887")
lb_1.place(x=10, y=215)
lb_2 = Radiobutton(menu2, text="Não", variable=valor_c , value=2, bg="#deb887")
lbi = Label(root, width=7, height=0, text="iniciais ", bg="#deb887")
lbi.place(x=142, y=218)
lb_2.place(x=65, y=215)
lbe = Entry(root)
lbe.place(x=195, y=218, width=80)
lb_1.select()
lb_41 = Label(menu2, width=7, text="Tipo de Manga ", font="times 10 bold italic",
              fg="white", bg="#A52A2A")
lb_41.place(x=1, y=250, width=300, height=18)
rd_42 = Radiobutton(menu2, text="Manga longa ", variable=valor_d, bg="#deb887", value=1)
rd_42.place(x=10, y=280)
rd_43 = Radiobuttonmenu2t, text="Manga curta ", bg="#deb887", variable=valor_d, value=2)
rd_43.place(x=120, y=280)
rd_42.select()

def mostrar():
        print("Colarinho:__%s" % valor_a.get())
        print("Frente:_____%s" % valor_b.get())
        print("Manga:______%s" % valor_d.get())
        print("Bordado:____%s" % valor_c.get())
        print("Iniciais:___%s" % lbe.get())
cmd = Button(root, text="Finalizar", font="times 8 ", fg="black", bg="gray",
 width=10, command=mostrar)
cmd.place(x=10, y=320, width=70, height=20)

root.config(menu=show)
root.mainloop()

menu5 = Frame(aba)
aba.add(menu5, text="   Clientes   ")

menu6 = Frame(aba)
aba.add(menu6, text="   Produtos   ")

##menu7 = Frame(aba)
#aba.add(menu7, text="   Vendas   ")

menu8 = Frame(aba)
aba.add(menu8, text="   Cliente   ")






menu2.mainloop()
