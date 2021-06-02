#https://www.youtube.com/watch?v=25aSCfcHRME
#https://www.youtube.com/watch?v=0WRMYdOwHYE

from tkinter import *
from tkinter.ttk import *


def start():
    GB = 10000
    download = 0
    speed = 1
    while(download<GB):
        #time.sleep(0.05)
        bar['value'] +=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" tarefa completeda")
        root.update_idletasks()

root = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(root, textvariable=percent).pack()
taskLabel = Label(root, textvariable=text).pack()

button = Button(root, text="download", command=start).pack()


root.mainloop()




