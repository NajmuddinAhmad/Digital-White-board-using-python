from tkinter import *
import tkinter
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk 
from tkinter import filedialog
import os


##################### *****DEVOLOP BY NAJMUDDIN AHMAD***** ###################

############ App size details #######################
window = Tk()
window.title("WHITE BOARD BY NAJMUDDIN AHMAD")
window.config(bg="#f2f3f5")
window.geometry("1050x570+150+50")
window.resizable(False,False)


######################## Canvas functionality #############################
current_x = 0
current_y = 0
color ="black"

def locate_xy(work):
    global current_x,current_y
    
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x,current_y
    

    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill = color,capstyle=ROUND,smooth=True)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color

    color = new_color

################### Eraser function #######################################
def new_canvas():
    canvas.delete('all')
    display_pallet()

################### For adding image from pc files ########################
def insertimage():
    global filename
    global f_img

    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("PNG file","*.png"),("ALL file","new.txt")))

    f_img=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180,50,image=f_img)
    window.bind("<B3-Motion>",my_callback)

def my_callback(event):
    global f_img

    f_img=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(event.x,event.y,image=f_img)



#########icon#####################
logo = PhotoImage(file="logo.png")
window.iconphoto(False,logo)

##############sidebar#####################
color_box =PhotoImage(file="sidebar.png")
Label(window,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser = PhotoImage(file="eraser_icon.png")
Button(window,image=eraser ,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

import_photo = PhotoImage(file="add_photo.png")
Button(window,image=import_photo ,bg="white",command=insertimage).place(x=30,y=450)


#########colors############

colors = Canvas(window,bg="#fff",width=37,height=300,bd=0)
colors.place(x=30,y=60)


def display_pallet():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    # id = colors.create_rectangle((10,10,30,30),fill="grey")
    # colors.tag_bind(id,'<Button-1>',lambda x: show_color('grey'))

    id = colors.create_rectangle((10,40,30,60),fill="brown4")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id = colors.create_rectangle((10,100,30,120),fill="magenta")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('magenta'))

    id = colors.create_rectangle((10,130,30,150),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id = colors.create_rectangle((10,160,30,180),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,190,30,210),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id = colors.create_rectangle((10,250,30,270),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))  


display_pallet()


# main screen
canvas = Canvas(window,width=930,height=465,background="white",cursor="hand2")
canvas.place(x=100,y=30)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)

#############slider##############

current_value = tk.DoubleVar()
def get_current_value():
    return'{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_lable.configure(text=get_current_value())

slider = ttk.Scale(window, from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

value_lable =ttk.Label(window,text=get_current_value())
value_lable.place(x=27,y=550)


window.mainloop()