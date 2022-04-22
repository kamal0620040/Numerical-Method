
# Iteration False Position Method(Page- , Root finding)
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
mytable = PrettyTable(["Iteration","a(-)","b(+)","x","f(x)"])
condition=True
while condition:
    print(i)
    temp=x
    x= fx(a,b)
    func=f(x)
    mytable.add_row([i,a,b,x,func])
    if func<0:
        a=x
    else:
        b=x
    i+=1
    condition=abs(temp-x)>epsilon  

print(mytable)
print('The root of the function using False Position method is: x= ' + str(x))



