# Kat Chonka
# Created 12/25/19
# Last edited 12/28/19 by author

# An instantiation of a calculator.

import math

class Calculator(object):

    """Attributes:
        past : a list of previous results.
        expression : a string of the input expression to be calculated.
    """

    past = []
    expression = ""

    def __init__(self):
        self.past = []
        self.past.append(0)  # Adds 0 to the list of past results.
        self.expression = ""  # Initializes an empty string.

    def add_input(self, user_input):
        self.expression = self.expression + str(user_input)

    # Parses the string expression and evaluates the result
    def evaluate(self):
        argument1 = 0
        argument2 = 0
        operand = ""
        # Find the operand
        operands = ["+", "-", "*", "/", "%", "+/-"]
        for x in operands:
            pos = self.expression.find(x)
            if pos is not -1:    # Operand found
                operand = self.expression[pos]
                if operand == self.expression[0]:   # Operand is the first expression
                    argument1 = float(self.expression[1:len(self.expression)-1])
                else:
                    argument1 = float(self.expression[0:pos-1])
                    argument2 = float(self.expression[pos+1:len(self.expression)-1])

        if operand == "+":
            return self.add(argument1, argument2)
        elif operand == "-":
            return self.subtract(argument1, argument2)
        elif operand == "*":
            return self.multiply(argument1, argument2)
        elif operand == "/":
            return self.divide(argument1, argument2)

        # Clear the expression string at the end of this function:
        self.expression = ""

    # Clear: clears the list of past calculations and the expression string
    def clear(self):
        self.past.clear()
        self.past.append(0)
        self.expression = ""

    # Addition
    def add(self, x, y=None):
        if y is not None:
            z = x + y
            self.past.append(z)
            return z
        else:
            z = self.past[-1] + x
            self.past.append(z)
            return z

    # Subtraction
    def subtract(self, x, y=None):
        if y is not None:
            z = x - y
            self.past.append(z)
            return z
        else:
            z = self.past[-1] - x
            self.past.append(z)
            return z

    # Multiplication
    def multiply(self, x, y=None):
        if y is not None:
            z = x * y
            self.past.append(z)
            return z
        else:
            z = self.past[-1] * x
            self.past.append(z)
            return z

    # Division
    def divide(self, x, y=None):
        if y is not None:
            z = x / y
            self.past.append(z)
            return z
        else:
            z = self.past[-1] / x
            self.past.append(z)
            return z


