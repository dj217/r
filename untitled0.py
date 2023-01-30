from tkinter import *
import random

root=Tk()
root.title('password generater')
root.geometry('400x400')

#label=label(root)

array=[['1','2','3','4','5','6','7','8','9','0'],['thb','lotr'],['a','b','c','d','e','f','g']]
p=0

def np():
    rn=random.randint(0,9)
    rn1=random.randint(10,11)
    rn2=random.randint(12,18)
    
    p=[rn,rn1,rn2]
    
b=Button(root,text=p,command=np())
b.place(relx=0.1,rely=0.1,anchor=CENTER)

root.mainloop