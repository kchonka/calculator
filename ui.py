# Kat Chonka
# Created 12/27/19
# Last edited 12/28/19 by author

from tkinter import *
from Calculator import Calculator

# Creating a main window "m" - blank window with close, maximize, and minimize buttons:
m = Tk()
# Renaming the title of the window:
m.title("Calculator")
# Defining the size of the window (in pixels):
m.geometry("624x648")
# Prevent the window from being resized:
m.resizable(0,0)

# Separating the window into frames:
input_frame = Frame(m, width=648, height=150, bd=0)
input_frame.pack(side=TOP)
bottom_frame = Frame(m, width=648, height=590, bg="white")
bottom_frame.pack()

# Variable to capture the input of the input_field:
input_text = StringVar()

# Creating an input field inside input_frame:
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="plum2", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=25)

# Creating the rest of the buttons:
# First row:
clear = Button(bottom_frame, text="C", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=0, column=0)
negate = Button(bottom_frame, text="+/-", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=0, column=1)
percentage = Button(bottom_frame, text="%", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=0, column=2)
divide = Button(bottom_frame, text="/", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=0, column=3)
# Second row:
seven = Button(bottom_frame, text="7", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=1, column=0)
eight = Button(bottom_frame, text="8", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=1, column=1)
nine = Button(bottom_frame, text="9", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=1, column=2)
multiply = Button(bottom_frame, text="x", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=1, column=3)
# Third row:
four = Button(bottom_frame, text="4", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=2, column=0)
five = Button(bottom_frame, text="5", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=2, column=1)
six = Button(bottom_frame, text="6", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=2, column=2)
minus = Button(bottom_frame, text="-", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=2, column=3)
# Fourth row:
one = Button(bottom_frame, text="1", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=3, column=0)
two = Button(bottom_frame, text="2", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=3, column=1)
three = Button(bottom_frame, text="3", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=3, column=2)
four = Button(bottom_frame, text="-", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=3, column=3)
# Fifth row:
zero = Button(bottom_frame, text="0", fg="white", width=36, height=6, bg="purple", cursor="hand1").grid(row=4, column=0, columnspan=2)
decimal = Button(bottom_frame, text=".", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=4, column=2)
equals = Button(bottom_frame, text="=", fg="white", width=16, height=6, bg="purple", cursor="hand1").grid(row=4, column=3)

m.mainloop()







