from tkinter import *
from PIL import Image , ImageTk

#Basic settings
window = Tk()
window.title("Image Viewer")
window.iconbitmap("icons/image.ico")

#Add photos

img1 = ImageTk.PhotoImage(Image.open("images/program1.png"))
img2 = ImageTk.PhotoImage(Image.open("images/program2.png"))
img4 = ImageTk.PhotoImage(Image.open("images/program4.png"))

#The main part
images_list = [img1,img2,img4]
main_lable = Label(window, image= img1)
main_lable.grid(columnspan=3)
status = Label(window, text="image 1 of {}".format(len(images_list)),bg="lightblue",fg="black",relief=SUNKEN)
status.grid(row=2,column=1,sticky=W+E)
# anchor=CENTER,NW,N,NE,W,E,SW,S,SE
# relief = FLAT,RAISED,SUNKEN,GROOVE,RIDGE

def forward(image_number):
    global main_lable
    global button_forward
    global button_back
    global status
    main_lable.grid_forget()
    main_lable = Label(window,image=images_list[image_number - 1])
    main_lable.grid(columnspan=3)
    button_forward = Button(window , text=">>",bg="black",fg="white", command=lambda: forward(image_number + 1))
    button_back = Button(window, text="<<",bg="black",fg="white",command= lambda: back(image_number - 1))
    status = Label(window, text="image {1} of {0}".format(len(images_list),image_number),bg="lightblue",fg="black",relief=SUNKEN)

    if image_number == 3:
        button_forward = Button(window, text=">>",state=DISABLED)
    
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    main_lable.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=1,sticky=W+E)

def back(image_number):
    global main_lable
    global button_forward
    global button_back
    global status

    main_lable.grid_forget()
    main_lable = Label(window,image=images_list[image_number - 1])
    main_lable.grid(columnspan=3)
    button_forward = Button(window , text=">>",bg="black",fg="white", command=lambda: forward(image_number + 1))
    button_back = Button(window, text="<<",bg="black",fg="white",command= lambda: back(image_number - 1))
    status = Label(window, text="image {1} of {0}".format(len(images_list),image_number),bg="lightblue",fg="black",relief=SUNKEN)

    if image_number == 1:
        button_back = Button(window, text="<<",state=DISABLED)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    main_lable.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=1,sticky=W+E)

button_forward = Button(window , text=">>",bg="black",fg="white", command=lambda: forward(2)).grid(column=2 , row=1)
button_back = Button(window , text="<<",bg="black",fg="white",state=DISABLED).grid(column=0 , row=1)
button_quit = Button(window,text="quit",command=window.destroy).grid(column=1 , row=1)

window.mainloop()
