from tkinter import *
import time
master = Tk()

def diHola():
    #print("Has pulsado el boton")
    print("Lo que has escrito es: ",campo.get())

f = Frame(width=300,height=300)
f.pack(padx=30,pady=30)

#ponemos textos
titulo = Label(f,text="Programa guay")
titulo.pack(side=TOP)

campo = Entry(f)
campo.pack(side=TOP,padx=10,pady=10)

boton = Button(f,text="Pulsame",command=diHola)
boton.pack(side=TOP,padx=10,pady=10)

w = Canvas(master, width=200, height=100)
w.pack()
posx = 0


w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
photo = PhotoImage(file="logo.gif")
w.create_image(posx,0, image=photo,anchor="nw")
posx += 1
time.sleep(5)
    
    

