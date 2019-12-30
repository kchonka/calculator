# Kat Chonka
# Created 12/27/19
# Last edited 12/29/19 by author

from tkinter import *

# Global string variable for the expression
expression = ""


# Calculator functions:
def add_input(user_input):
    global expression
    expression = expression + str(user_input)
    input_text.set(expression)


# Negates the expression. Implementation of the "+/-" negation button
def negate():
    global expression
    expression = "-(" + expression + ")"
    input_text.set(expression)


# Clears the calculator & the input expression.
def clear():
    global expression
    expression = ""
    input_text.set("")


# Parses the input and evaluates the string expression.
# Throws an error if unable to evaluate due to the format.
def evaluate():
    global expression
    try:
        total = str(eval(expression))
        input_text.set(total)      # Place the result in the input_text bar
        expression = total         # Updates the expression to the total
    except:
        input_text.set("Error")
        expression = ""


# Driver Code:
# Creating a main window "m" - blank window with close, maximize, and minimize buttons:
m = Tk()
# Renaming the title of the window:
m.title("Calculator")
# Defining the size of the window (in pixels):
m.geometry("624x688")
# Prevent the window from being resized:
m.resizable(0,0)

# Separating the window into frames:
input_frame = Frame(m, width=648, height=150, bd=0)
input_frame.pack(side=TOP)
bottom_frame = Frame(m, width=648, height=610, bg="white")
bottom_frame.pack()

# Variable to capture the input of the input_field:
input_text = StringVar()

# Creating an input field inside input_frame:
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="magenta",
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=25)

# Creating the rest of the buttons:
# First row:
clear = Button(bottom_frame, text="C", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=clear).grid(row=0, column=0)
negate = Button(bottom_frame, text="+/-", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=negate).grid(row=0, column=1)
percentage = Button(bottom_frame, text="%", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input("%")).grid(row=0, column=2)
divide = Button(bottom_frame, text="/", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input("/")).grid(row=0, column=3)
# Second row:
seven = Button(bottom_frame, text="7", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("7")).grid(row=1, column=0)
eight = Button(bottom_frame, text="8", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("8")).grid(row=1, column=1)
nine = Button(bottom_frame, text="9", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("9")).grid(row=1, column=2)
multiply = Button(bottom_frame, text="*", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input("*")).grid(row=1, column=3)
# Third row:
four = Button(bottom_frame, text="4", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("4")).grid(row=2, column=0)
five = Button(bottom_frame, text="5", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("5")).grid(row=2, column=1)
six = Button(bottom_frame, text="6", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("6")).grid(row=2, column=2)
minus = Button(bottom_frame, text="-", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input("-")).grid(row=2, column=3)
# Fourth row:
one = Button(bottom_frame, text="1", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("1")).grid(row=3, column=0)
two = Button(bottom_frame, text="2", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("2")).grid(row=3, column=1)
three = Button(bottom_frame, text="3", font=('arial', 11, 'bold'), fg="white", width=16, height=6, bg="purple", cursor="hand1", command=lambda: add_input("3")).grid(row=3, column=2)
add = Button(bottom_frame, text="+", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input("+")).grid(row=3, column=3)
# Fifth row:
zero = Button(bottom_frame, text="0", font=('arial', 11, 'bold'), fg="white", width=36, height=6, bg="purple", cursor="hand1", command=lambda: add_input("0")).grid(row=4, column=0, columnspan=2)
decimal = Button(bottom_frame, text=".", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: add_input(".")).grid(row=4, column=2)
equals = Button(bottom_frame, text="=", font=('arial', 11, 'bold'), fg="black", width=16, height=6, bg="plum2", cursor="hand1", command=lambda: evaluate()).grid(row=4, column=3)

# Run the GUI:
m.mainloop()







