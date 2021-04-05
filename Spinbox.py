from tkinter import *

root = Tk()
root.title("KX")
root.iconbitmap("images/icon.ico")
root.geometry("300x250")


lb_1 = Spinbox(root, from_=0,to=100)
lb_1.pack()

lb_2 = Spinbox(root, values=(10,20,30,40,50,60,70,80,90,100), wrap=True)
lb_2.pack()

lb_3 = Spinbox(root, values= ("João", 
"Maria",
 "Pedro",
  "Isabél",
   "Francisco",
    "Josefa", 
    "Carlos", 
    "Sandra"),wrap=True)
lb_3.pack()

def executar():
    print(lb_3.get())


bt = Button(root, text="executar", command=executar)
bt.pack()







root.mainloop()