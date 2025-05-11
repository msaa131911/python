from tkinter import *
from PIL import Image, ImageTk

root = Tk()

my_image = ImageTk.PhotoImage(Image.open("E:/use pic/494007127_2560149160992241_2684359926409464840_n.jpg"))
label = Label(root, image=my_image)
label.pack()

btn=Button(root,text="exit",command=root.quit)
btn.pack()
root.mainloop()