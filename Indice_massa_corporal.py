from tkinter import *

root = Tk()
root.title("kamisaria Zanuto")
root.iconbitmap("images/icon.ico")
root.geometry("500x310")
root.resizable(False, False)
#root ["bg"] = "gray"

def execut():
    nome = box_name.get()
    nome1 = box_peso.get()
    show = Label(root, fg="#008",font="arial 10 ", text=" Ola  " + nome)
    show1 = Label(root, fg="#008",font="arial 10 ", text=" Você esta pesando  " + nome1)
    show.place(x=50, y=220)
    show1.place(x=50, y=240)

    peso = float(box_peso.get())
    altura = float(box_alt.get())
    imc = peso / (altura **2) 

    if imc <=30:
        screen.set(" Parabéns, Você esta ótimo. ")
    else:
        screen1.set(" Você precisa perder Caloria urgente ")   
        print(imc) 



      
screen  = StringVar(root)
screen1 = StringVar(root)

lb = LabelFrame(root, text="Indice de massa corporal",fg="gray", borderwidth=1, relief="sunken", bg="#ffffb3")
lb.place(x=10, y=30, width=480, height=150)

lb1 = LabelFrame(root, text="Resultado de sua pesquisa", fg="gray", borderwidth=1, relief="solid")
lb1.place(x=10, y=190, width=480, height=100)


titulo = Label(root, text="Digiite seus Dados", font="times 13 bold", fg="red")
titulo.place(x=190, y=5)

img = PhotoImage(file="images/corredora2.png")
image = Label(root, image=img, borderwidth=-1,  relief="solid",  bg="white")
image.place(x=350, y=45, width=135, height=130)

lb_name = Label(lb, text="Nome", bg="#ffffb3")
lb_peso = Label(lb, text="Peso", bg="#ffffb3")
lb_alt = Label(lb, text="Altura", bg="#ffffb3")
lb_idade = Label(lb, text="Idade", bg="#ffffb3")
lb_resp = Label(root, textvariable=screen, font="arial 10" , fg="#008")
lb_resp2 = Label(root, textvariable=screen1, font="arial 10" , fg="red")


lb_name.grid(row=1, column=0)
lb_peso.grid(row=2, column=0)
lb_alt.grid(row=1, column=2)
lb_idade.grid(row=2, column=2)
lb_resp.place(x=50, y=260)
lb_resp2.place(x=50, y=260)


box_name = Entry(lb)
box_peso = Entry(lb)
box_alt = Entry(lb)
box_idade = Entry(lb)

box_name.grid(row=1, column=1)
box_peso.grid(row=2, column=1)
box_alt.grid(row=1, column=3)
box_idade.grid(row=2, column=3)


cmd = Button(lb, text="Calcular", font="times 12", fg="white", bg="#008",command=execut)
cmd.place(x=10, y=100, width=110, height=25)

box_name.focus()

root.mainloop()