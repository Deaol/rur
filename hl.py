from tkinter import *
import turtle


root = Tk()

def bu():
    x = int(x_entry.get())
    y = int(y_entry.get())
    turtle.setpos(x, y)
    turtle.exitonclick()


button = Button(text="", command=bu)
button.grid(row=2, column=1, padx=5, pady=5, sticky="тык")
x_entry = Entry()
y_entry = Entry()
x_entry.grid(row=0, column=1, padx=5, pady=5)
y_entry.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

