from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("radio button")

ra_val = IntVar()

def av():
    lable = messagebox.askyesno("Warning", "Are you sure?")
    if lable == 1:
        window2 = Toplevel()
        lable2 = Label(window2,text="Thanks").pack()
    elif lable == 0:
        window2 = Toplevel()
        lable2 = Label(window2,text="Thank you").pack()

Radiobutton(window,value=1,text="pizza",variable=ra_val).pack(anchor=W)
Radiobutton(window,value=2,text="sandwich",variable=ra_val).pack(anchor=W)
Radiobutton(window,value=3,text="burger",variable=ra_val).pack(anchor=W)
Radiobutton(window,value=4,text="pasta",variable=ra_val).pack(anchor=W)

button = Button(window,text="done",command=av).pack()
window.mainloop()
