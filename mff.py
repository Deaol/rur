from tkinter import *
import turtle

root = Tk()
mas = []
a = 0
b = 0
def bu():
    x = int(x_entry.get())
    y = int(y_entry.get())
    mas.append([])
    mas[len(mas)-1].append(x)
    mas[len(mas)-1].append(y)
    print(mas)
def done():
    a = len(mas)
    global b
    for i in range(b, a):
        turtle.goto(mas[i][0], mas[i][1])
    turtle.getscreen()
    b = a



add = Button(text="тык", command=bu)
add.grid(row=2, column=1, padx=5, pady=5)

do = Button(text="клац", command= done)
do.grid(row=3, column=1, padx=5, pady=5)

x_entry = Entry()
y_entry = Entry()
x_entry.grid(row=0, column=1, padx=5, pady=5)
y_entry.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

