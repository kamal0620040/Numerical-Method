import math
import numpy as np
from prettytable import PrettyTable

# Used equation x^3-x-1 = 0
def g(x):
    return ((x+1)**(1/3))

def iteration(x, accuracy):
    c = x
    temp = x
    mytable = PrettyTable(["Iteration","x", "F(x)"])
    for i in range(30):
        c = round(g(c), accuracy)
        mytable.add_row([i+1,temp, c])
        if (temp != c):
            temp = c
        else :
            break
    print(mytable)
    print("The value of x is:")
    print(temp)


# for equation cosx = 3x - 1
def h(x):
    return ((math.cos(x)+1)/3)
def iteration1(x,accuracy):
    c = x
    temp = x
    mytable = PrettyTable(["Iteration","x", "F(x)"])
    for i in range(30):
        c = round(h(c), accuracy)
        mytable.add_row([i+1,temp, c])
        if (temp != c):
            temp = c
        else :
            break
    print(mytable)
    print("The value of x is:")
    print(temp)

#
iteration(1,5)
iteration1(0,6)
