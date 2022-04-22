

# Iteration Double Method(Page- 25, Root finding)
import math
from prettytable import PrettyTable

def fx(x,y):
    x= (3*y*x**2 + 7)/10
    return round(x,4)

def fy(y):
    y= (y**2 + 4)/5
    return round(y,4)

  
epsilon = 0.00005
i=1
mytable = PrettyTable(["Iteration","x","y"])
condition=True
x,y=0,0
while condition:
    tempx=x
    tempy=y
    x=fx(x,y)
    y=fy(y)
    mytable.add_row([i,x,y])
    a=x

    i+=1
    condition=abs(tempx-x)>=epsilon or abs(tempy-y)>=epsilon 

print(mytable)
print('The root of the function using Iteration double method is: x=' + str(x) + ', y= ' + str(y))



