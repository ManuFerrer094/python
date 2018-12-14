from tkinter import *

def diHola():
    print("Has pulsado el boton")

f = Frame(width=300,height=300)
f.pack(padx=30,pady=30)

#ponemos textos
titulo = Label(f,text="Programa guay")
titulo.pack(side=TOP)

boton = Button(f,text="Pulsame",command=diHola)
boton.pack(side=TOP,padx=10,pady=10)

