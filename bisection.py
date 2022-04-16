import numpy as np
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def f(x):
    y = x**2 - math.sin(x)
    y= round(y,4)
    return y
    
a, b = 0.5, 1.0
epsilon = 0.0001
i=1
abs_error = abs(b-a)
mytable = PrettyTable(["Iteration","a","b","x","f(x)"])
while abs_error>=epsilon:
    x = (a+b)/2
    x = round(x,4)
    fx = f(x)
    mytable.add_row([i,a,b,x,fx])
    if fx > 0:
        b=x
    else:
        a=x
    i+=1
    abs_error = abs(b-a)
print(mytable)
print("The root of the function is: ",x)