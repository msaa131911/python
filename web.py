from tkinter import *
import webbrowser

def web():
    ss = enty.get().strip().lower()
    if ss == "google":
        webbrowser.open("https://www.google.com")
    elif ss:  # If not empty
        # Search on Google by default
        webbrowser.open(f"https://www.google.com/search?q={ss}")

def clear_entry(event):
    if enty.get() == "Search:":
        enty.delete(0, END)

root = Tk()
root.title("web search")

enty = Entry(root, width=40, borderwidth=20)
enty.insert(0, "Search:")
enty.bind("<FocusIn>", clear_entry)  # Clear when clicked
enty.grid(row=0, column=0, columnspan=5)
enty.focus()

butn = Button(root, padx=30, pady=15, text="Enter", command=web)
butn.grid(row=1, column=2)  # Centered better

root.mainloop()