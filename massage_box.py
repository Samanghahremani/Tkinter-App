from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("massagebox")
window.iconbitmap("image/box.ico")
def callback():
    lable = messagebox.askyesno("یه سوال","آیا تو بهترینی؟ ")
    if lable == 0:
        callback()
    elif lable == 1:
        lable = messagebox.showinfo("آفرین","می دونستم")
button = Button(window,text="click here for continue",padx=100,pady=100,command=callback).grid()
window.mainloop()