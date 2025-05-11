from tkinter import *
root=Tk()

fram=LabelFrame(root,padx=50,pady=40,bg="red")
fram.pack(padx=10,pady=10)

btn1=Button(fram,text="alif")
btn2=Button(fram,text="abid")

btn1.grid(row=1,column=2)
btn2.grid(row=2,column=3)


root.mainloop()

