# Kat Chonka
# Created 12/25/19
# Last edit 12/25/19 by author

# An instantiation of a calculator.

import math

class Calculator(object):

    """Attributes:
        past : a list of previous results.
    """

    past = []

    def __init__(self):
        self.past = []
        self.past.append(0)

    # Clear: clears the list of past calculations
    def clear(self):
        self.past.clear()

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
    def multiply (self, x, y=None):
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


