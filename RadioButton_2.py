from tkinter import *


root=Tk()
def click(vlaue):
    my_label=Label(root,text=vlaue)
    my_label.pack()


test=[
    ('a','alif'),
    ('b','abid'),
    ('c','araf')

]
testvar=StringVar()
testvar.set('a')


for k,val in test:
    Radiobutton(root,text=k,variable=testvar,value=val).pack()


btn=Button(root,text="open",command=lambda :click(testvar.get()))
btn.pack()

root.mainloop()