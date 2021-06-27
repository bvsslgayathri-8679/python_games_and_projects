import sys
from tkinter import *
from tkinter import messagebox

import random

def color_change():
    list1=["red","yellow","blue","orange"]
    virus.config(background=random.choice(list1))
    virus.after(200,color_change)


def war():
    messagebox.showinfo(message="do you want to continue")


root1=Tk()

b1=Button(root1,text="Warning! do u want to continue",width=25,height=5,command=war)
b1.place(x=20,y=45)
root1.mainloop()
root=Tk()
root.geometry("700x250")


virus=Label(root,text="You have virus warning ",font=("times",50,"bold"))
virus.grid(row=2,column=0,pady=20,padx=20)
color_change()





root.mainloop()




