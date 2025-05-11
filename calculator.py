from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("C:/Users/PC/Desktop")

def button_click(number):
    current = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, str(current) + str(number))


def clear():
    my_entry.delete(0, END)


def plus():
    first_number = my_entry.get()
    global f_number
    global math
    math= "addition"
    f_number = int(first_number)
    my_entry.delete(0, END)
def minas():
    first_number = my_entry.get()
    global f_number
    global math
    math = "minas"
    f_number = int(first_number)
    my_entry.delete(0, END)
def gun():
    first_number = my_entry.get()
    global f_number
    global math
    math = "gun"
    f_number = int(first_number)
    my_entry.delete(0, END)
def vag():
    first_number = my_entry.get()
    global f_number
    global math
    math = "vag"
    f_number = int(first_number)
    my_entry.delete(0, END)



def eql():
    second_number = my_entry.get()
    my_entry.delete(0, END)
    if math == "plus":
     my_entry.insert(0, int(f_number) + int(second_number))
    elif math == "minas":
         my_entry.insert(0, int(f_number) - int(second_number))
    elif math == "gun":
        my_entry.insert(0, int(f_number) * int(second_number))
    elif math == "vag":
        my_entry.insert(0, int(f_number) / int(second_number))


my_entry = Entry(root, width=40, borderwidth=10,bg="red")
my_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
my_entry.focus()
my_entry.insert(0, "")

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=plus)
button_eql = Button(root, text="=", padx=40, pady=20, command=eql)
button_clear = Button(root, text="C", padx=40, pady=20, command=clear)

button_gun = Button(root, text="x", padx=40, pady=20, command=gun)
button_vag = Button(root, text="/", padx=40, pady=20, command=vag)
button_minas = Button(root, text="-", padx=40, pady=20, command=minas)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_eql.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

button_gun.grid(row=6, column=0)
button_vag.grid(row=6, column=1)
button_minas.grid(row=6, column=2)

root.mainloop()
