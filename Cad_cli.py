# https://www.youtube.com/watch?v=9eqAxOqRcJo
# 010 Python Tkinter Alterando tios de letras e fontes
# https://www.youtube.com/watch?v=Gg_BsA_FlJo
# 011 - Python tkinter - DEFINIR LARGURA DE UM LABEL E IMPLICAÇÕES

from tkinter import *

def most():
    print("Nome:.........%s" % ed.get())
    print("sobre nome:...%s" % v_sb.get())
    print("e-mail:.......%s" % v_mail.get())
    print("celular:......%s" % v_cel.get())
    print("Data Nasc.:...%s" % v_data.get())
    print("Obs:..........%s" % obs.get(1.0, END))


root = Tk()
root.title("KZ")
root.iconbitmap("images/icon.ico")
root.geometry("300x350+200+200")
root["bg"] = "#deb887"

vp_d = Label(root, 
text="Preencha seus dados",
 font="times 15 bold italic",
  bg="#deb887", fg="#A52A2A")

vp_d.place(x=65, y=10)

v_nome = Label(root, 
width=4,
 text=" nome ",
  bg="#deb887",
   font="arial 8 " )
v_nome.place(x=10,
 y=55,
  height=10)
ed = Entry(root)
ed.place(x=10, 
y=70,
 width=120,
  height=22)

vs_b = Label(root,
 width=10,
  text="sobre nome",
   bg="#deb887", 
   font="arial 8 ")
vs_b.place(x=135,
 y=55,
  height=10)
v_sb = Entry(root)
v_sb.place(x=135,
 y=70,
  width=155,
   height=22)

v_mail = Label(root,
 width=10, 
 text="e-mail",
  bg="#deb887",
   font="arial 8 ")
v_mail.place(x=-7,
 y=100,
  height=10)
v_mail = Entry(root)
v_mail.place(x=10,
 y=115,
  width=280,
   height=22)

v_cel = Label(root,
 text="celuar", 
 bg="#deb887",
  font="arial 8 ")
v_cel.place(x=9,
 y=145,
  height=10)
v_cel = Entry(root)
v_cel.place(x=10,
 y=160,
  width=122,
   height=22)

v_data = Label(root,
 text="data nasc.",
  bg="#deb887",
   font="arial 8 ")
v_data.place(x=135,
 y=145, 
 height=10)
v_data = Entry(root)
v_data.place(x=137, 
y=160,
 width=155,
  height=22)

Label(root,
 text="Obs:.",
  bg="#deb887",
   font="times 10 ",
    anchor=W).place(x=10,
     y=210, 
     width=50,
      height=10)
obs=Text(root)
obs.place(x=10,
 y=225, 
 width=280,
  height=80)

Button(root,
 width=10,
  text="Enviar",
   font="times 8 ", 
   bg="gray", 
   fg="black", 
   command=most).place(x=10,
    y=320, 
    width=70, 
    height=20)

Button(root,
 width=10,
  text="Limpar",
  font="times 8",
   bg="gray", 
   fg="black").place(x=100, 
   y=320,
    width=70,
    height=20)

root.mainloop()
