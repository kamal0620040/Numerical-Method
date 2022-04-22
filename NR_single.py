
# Newton Rhapson Method(Page- 19, Root finding)
import math
from prettytable import PrettyTable

def f(x):
    x= x**3 - x -1
    return round(x,4)
def fdx(x):
    x= 3*x**2-1
    return round(x,4)

def fx(a):
    a=a - f(a)/fdx(a)
    return round(a,4)

  
a=1
epsilon = 0.00005
i=1
mytable = PrettyTable(["Iteration","a","x"])
condition=True
x=0
while condition:
    temp=x
    x=fx(a)
    # temp=x
    # x = round(x,4)
    mytable.add_row([i,a,x])
    a=x

    i+=1
    condition=abs(temp-x)>=epsilon 

print(mytable)
print('The root of the function using Newton Rhapson method is: ' + str(x))