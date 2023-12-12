from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("massagebox")

def callback():
    lable = messagebox.askyesno("a question?","are you the best?")
    if lable == 0:
        callback()
    elif lable == 1:
        lable = messagebox.showinfo("good job","I knew")
button = Button(window,text="click here for continue",padx=100,pady=100,command=callback).grid()
window.mainloop()
