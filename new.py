from tkinter import *

root=Tk()
root.title("MSAA")

lab1=Label(root,text="label 1")
lab2=Label(root,text="label 2")
lab3=Label(root,text="label 3")
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=2,column=0)

root.mainloop()