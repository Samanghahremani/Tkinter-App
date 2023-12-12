from tkinter import *


window = Tk()

# main function
def see_result():
   lbl = Label(window, text= check_val.get()).pack()


# checkbox and its placeholder variable
check_val = IntVar()
checkbox_tool = Checkbutton(window, text="سیاست های ما مورد قبول است؟", variable=check_val)
checkbox_tool.pack()

# Button to record information
button = Button(window, text="تایید کردن", command=see_result, border=3,background="lightblue")
button.pack()

window.mainloop()
