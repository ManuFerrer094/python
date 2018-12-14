import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
rectangle = canvas.create_rectangle(350, 10, 375, 200, fill="blue")
canvas.itemconfig(rectangle, outline="black")
triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="red")
canvas.itemconfig(triangle, outline="black")
 
def startgame():
    while 1:
        for x in range(0, 60):
            canvas.move(rectangle, 0, 4)
            tk.update()
            time.sleep(0.04)
        for x in range(0, 60):
            canvas.move(rectangle, 0, -4)
            tk.update()
            time.sleep(0.04)
 
        time.sleep(20)
        canvas.create_text(200, 200, text="GAME OVER", font=('Times', 30), fill="red")
        canvas.delete(rectangle)
        canvas.delete(triangle)
 
btn = Button(tk, text="Start Game", command=startgame)
btn.pack()
