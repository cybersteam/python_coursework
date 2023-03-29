import turtle
from tkinter import *

def a_function():
    print("A function has been fired")

class Dog():
    def bark(self):
        print("the dog barks!\n")

    def dog_draw_square(self):
        t = turtle.Pen()
        for x in range(1,5):
            t.forward(50)
            t.left(90)

        print("Dog has run around the block")


    def dog_spawn_window(self):
        tk = Tk()

        tk.geometry('100x100')

        btn = Button(tk, text="click to draw", command=self.dog_draw_square)

        btn.place(x = 50,y = 50)
        print("this has happened")
        tk.mainloop()
