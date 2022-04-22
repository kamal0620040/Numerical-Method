
# Iteration Secant Method(Page-15 , Root finding)
import math
from prettytable import PrettyTable

def f(x):
    x= x**3 - x -1
    return round(x,4)

def fx(a,b):
    x= (a*f(b) - b*f(a))/(f(b)-f(a))
    return round(x,4)

  
epsilon = 0.00005
i=1
a=1
b=2
x=0
mytable = PrettyTable(["Iteration","a","b","x",])
condition=True
while condition:
    temp=x
    x= fx(a,b)
    mytable.add_row([i,a,b,x])
    a=b
    b=x

    i+=1
    condition=abs(temp-x)>epsilon  

print(mytable)
print('The root of the function using Secant method is: x= ' + str(x))



