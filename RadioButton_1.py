from tkinter import *

root=Tk()
c=IntVar()
c.set("hello")

def click(vlaue):
    my_label=Label(root,text=vlaue)
    my_label.pack()

Radiobutton(root,text='option 1',variable=c,value=1,command=lambda :click(c.get())).pack()
Radiobutton(root,text='option 2',variable=c,value=2,command=lambda :click(c.get())).pack()
Radiobutton(root,text='option 3',variable=c,value=3,command=lambda :click(c.get())).pack()


root.mainloop()