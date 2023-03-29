from tkinter import *

root = Tk()
python_course_logo = PhotoImage(file="python.gif")

rightlabel = Label(root, image=python_course_logo)
rightlabel.pack(side="right")

our_text = """With tkinter, you can only use gif images. There are other
more powerful Python packages that allow you to use other image types."""

leftlabel = Label(root, 
           justify=RIGHT,
           padx = 10, 
           text=our_text).pack(side="left")

print("Launching window ... ")
root.mainloop()
