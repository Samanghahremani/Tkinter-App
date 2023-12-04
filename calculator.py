from tkinter import *

#Basic settings
window = Tk()
window.title("calculator")
window.iconbitmap("icons/calculator.ico")

#main body
entry = Entry(window,width=48,borderwidth=10)
entry.grid(row=0,column=0,columnspan=4)

#Functions section
def clear():
    entry.delete(0,END)

def add_char_to_entry(char):
    current_value = entry.get()
    entry.delete(0,END)
    new_value = str(current_value)+str(char)
    entry.insert(0,new_value)

def equal():
    second_number = entry.get()
    entry.delete(0,END)
    if operator == "add":
        final_calculation = int(second_number) + int(first_number)
    elif operator == "sub":
        final_calculation = int(first_number) - int(second_number)
    elif operator == "div":
        final_calculation = int(first_number) / int(second_number)
    elif operator == "multi":
        final_calculation = int(first_number) * int(second_number)
    entry.insert(0,final_calculation)

def add_number():
    global first_number
    global operator
    first_number = entry.get()
    entry.delete(0,END)
    operator = "add"
def subtraction():
    global first_number
    global operator
    first_number = entry.get()
    entry.delete(0,END)
    operator = "sub"

def division():
    global first_number
    global operator
    first_number = entry.get()
    entry.delete(0,END)
    operator = "div"

def multiply():
    global first_number
    global operator
    first_number = entry.get()
    entry.delete(0,END)
    operator = "multi"

button1 = Button(window, text="1",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(1)).grid(row=1,column=0)
button2 = Button(window, text="2",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(2)).grid(row=1,column=1)
button3 = Button(window, text="3",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(3)).grid(row=1,column=2)

button4 = Button(window, text="4",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(4)).grid(row=2,column=0)
button5 = Button(window, text="5",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(5)).grid(row=2,column=1)
button6 = Button(window, text="6",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(6)).grid(row=2,column=2)

button7 = Button(window, text="7",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(7)).grid(row=3,column=0)
button8 = Button(window, text="8",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(8)).grid(row=3,column=1)
button9 = Button(window, text="9",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(9)).grid(row=3,column=2)
button0 = Button(window, text="0",padx=32,pady=23,bg="lightblue",command=lambda: add_char_to_entry(0)).grid(row=4,column=0)

button_clear = Button(window, text="cls",padx=28,pady=23,bg="gray",command=clear) .grid(row=4,column=1)
button_equal = Button(window, text="=",padx=31,pady=23,bg="gray",command=equal) .grid(row=4,column=2)
button_add = Button(window, text="+",padx=30,pady=23,bg="gray",command=add_number) .grid(row=1,column=3)
button_subtraction = Button(window, text="-",padx=31,pady=23,bg="gray",command=subtraction) .grid(row=2,column=3)
button_multiply = Button(window, text="x",padx=31,pady=23,bg="gray",command=multiply).grid(row=3,column=3)
button_division = Button(window, text="÷",padx=30,pady=23,bg="gray",command=division) .grid(row=4,column=3)
# state=DISABLED #To disable the button
# command #To attach the function to the button
window.mainloop()
