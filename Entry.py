from tkinter import *

root=Tk()

my_entry=Entry(root,width=20,bg="red",fg="blue",borderwidth=5)
my_entry.grid(row=0,column=0)
my_entry.focus()
my_entry.insert(0,"search")

def ssd():
    kss=my_entry.get()
    lab=Label(root,text= kss)
    lab.grid()

btn=Button(root,text="open",padx=5,pady=5,fg="blue",bg="green",command=ssd)
btn.grid()


root.mainloop()