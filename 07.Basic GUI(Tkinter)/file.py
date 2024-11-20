from tkinter import *

root = Tk()

root.title("Basic GUI by Tkinter")
root.geometry('400x400')

lb = Label(root,text="Click me?")
lb.grid()

def clicked():
    lb.configure(text="I just got clicked")

btn = Button(root, text="Click me",
             fg = "red", command=clicked)

btn.grid(column=1,row=0)
root.mainloop()