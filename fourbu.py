from tkinter import *
import turtle

root = Tk()
def left():
    turtle.backward(10)
    turtle.exitonclick()
def right():
    turtle.forward(10)
    turtle.exitonclick()
def top():
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.exitonclick()
def down():
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.exitonclick()

buup = Button(text="up", command = top)
bule = Button(text="le", command = left)
budo = Button(text="dow", command = down)
bur = Button(text="ri", command = right)

buup.pack(side='top')
bule.pack(side='left')
budo.pack(side='bottom')
bur.pack(side='right')
root.mainloop()


