from tkinter import *

root=Tk()
def butt():
    lab=Label(root,text="msaa")
    lab.grid(row=1,column=0)

root.title("msaa")
my_button=Button(root,text="open",fg="blue",bg="red",padx="10",pady="20",command=butt)
my_button.grid(row=0,column=0)

root.mainloop()