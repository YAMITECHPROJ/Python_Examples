# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Arun's Py World")
# Set geometry (widthxheight)
root.geometry('900x500')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

#adding a label to the root window
lbl = Label(root, text = "welcome To Python world ?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =3, row =3)

# function to display text when
# button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text
# inside
btn = Button(root, text = "Click here" ,
             fg = "blue", command=clicked)

# set Button grid
btn.grid(column=4, row=0)
# all widgets will be here
# Execute Tkinter
root.mainloop()
