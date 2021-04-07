#anchor ->  N=Norte, S=SUl, E=Leste, W=Oeste
# NE=Nordeste, SE=Sudeste, SO=Sudoeste, NO=Noroeste

from tkinter import *

root = Tk()
root.title("Modelo")
root.iconbitmap("images/icon.ico")
root.geometry("300x350+200+200")
root["bg"] = "#deb887"

def fileNew():
      print(fileNew)

browse = Menu(root)
#Menu File
naveg = Menu(browse, tearoff=0)
naveg.add_command(label="Mew",command=fileNew)
naveg.add_command(label="Open")
naveg.add_command(label="save")
naveg.add_separator()
naveg.add_command(label="Exit")
browse.add_cascade(label="File", menu=naveg) 

v_relief = Label(root, relief="solid", bg="#deb887",  bd=1, width=5, height=2)
v_relief.place(x=12, y=4)
valor_a = IntVar()
valor_b = IntVar()
valor_c = IntVar()
valor_d = IntVar()
Label(root,bg="#A52A2A").place(x=55,
                               y=20,
                               width=250,
                               height=18)
Label(root, width=1,
      text="Tipo de Colarinho",
      bg="#A52A2A",
      font="Times 10 bold italic",
      fg="white").place(x=100,
                        y=21,
                        width=100,
                        height=16)
rad_1 = Radiobutton(root,
                    text="Itáliano ",
                    variable=valor_a,
                    value=1,
                    bg="#deb887")
rad_2 = Radiobutton(root,
                    text="Inglês ",
                    variable=valor_a,
                    value=2,
                    bg="#deb887")
rad_3 = Radiobutton(root,
                    text="Chanfrado ",
                    variable=valor_a,
                    value=3,
                    bg="#deb887")
rad_4 = Radiobutton(root,
                    text="Gola de Padre ",
                    variable=valor_a,
                    value=4,
                    bg="#deb887")
rad_5 = Radiobutton(root,
                    text="París ",
                    variable=valor_a,
                    value=5,
                    bg="#deb887")
rad_6 = Radiobutton(root,
                    text="Monaco ",
                    variable=valor_a,
                    value=6,
                    bg="#deb887")
rad_7 = Radiobutton(root,
                    text="Windisor ",
                    variable=valor_a,
                    value=7,
                    bg="#deb887")
rad_8 = Radiobutton(root,
                    text="Douglas ",
                    variable=valor_a,
                    value=8,
                    bg="#deb887")
rad_9 = Radiobutton(root,
                    text="U.S.A ",
                    variable=valor_a,
                    value=9,
                    bg="#deb887")
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
      text="Tipo de Frente",
      font="times 10 bold italic",
      bg="#A52A2A",
      fg="white").place(x=1,
                        y=110,
                        width=300,
                        height=18)

rad_1 = Radiobutton(root,
                    text="Frente Lisa",
                    variable=valor_b,
                    value=1,
                    bg="#deb887")
rad_2 = Radiobutton(root,
                    text="Frente Dupla",
                    variable=valor_b,
                    value=2, bg="#deb887")
rad_1.place(x=10, y=130)
rad_2.place(x=10, y=150)

rad_1.select()

Label(root,
      text="Bordado",
      font="times 10 bold italic",
      bg="#A52A2A",
      fg="white").place(x=1,
                        y=185,
                        width=300,
                        height=18)

lb_1 = Radiobutton(root,
                   text="Sim",
                   variable=valor_c ,
                   value=1,
                   bg="#deb887")
lb_1.place(x=10, y=215)
lb_2 = Radiobutton(root,
                   text="Não",
                   variable=valor_c ,
                   value=2,
                   bg="#deb887")
lbi = Label(root,
            width=7,
            height=0,
            text="iniciais ",
            bg="#deb887")
lbi.place(x=142, y=218)
lb_2.place(x=65, y=215)
lbe = Entry(root)
lbe.place(x=195, y=218, width=80)
lb_1.select()
lb_41 = Label(root,
              width=7,
              text="Tipo de Manga ",
              font="times 10 bold italic",
              fg="white",
              bg="#A52A2A")
lb_41.place(x=1,
            y=250,
            width=300,
            height=18)
rd_42 = Radiobutton(root,
                    text="Manga longa ",
                    variable=valor_d,
                    bg="#deb887",
                    value=1)
rd_42.place(x=10, y=280)
rd_43 = Radiobutton(root,
                    text="Manga curta ",
                    bg="#deb887",
                    variable=valor_d,
                    value=2)
rd_43.place(x=120, y=280)

rd_42.select()

def mostrar():
        print("Colarinho:__%s" % valor_a.get())
        print("Frente:_____%s" % valor_b.get())
        print("Manga:______%s" % valor_d.get())
        print("Bordado:____%s" % valor_c.get())
        print("Iniciais:___%s" % lbe.get())
cmd = Button(root,
             text="Finalizar",
             font="times 8 ",
             fg="black",
             bg="gray",
             width=10,
             command=mostrar)
cmd.place(x=10, y=320, width=70, height=20)

root.config(menu=browse)

root.mainloop()
