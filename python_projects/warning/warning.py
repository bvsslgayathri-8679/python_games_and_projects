import sys
from tkinter import *

import random

def color_change():
    list1=["red","yellow","blue","orange"]
    virus.config(background=random.choice(list1))
    virus.after(200,color_change)


def war():
    tkMessageBox.showinfo(message="do you want to continue")



root=Tk()
root.geometry("700x250")

virus=Label(root,text="You have virus warning ",font=("times",50,"bold"))
virus.grid(row=2,column=0,pady=20,padx=20)
color_change()


b1=Button(root,text="Warning! do u want to continue",width=5,height=10,command=war)
b1.place(x=955,y=350)

root.mainloop()






