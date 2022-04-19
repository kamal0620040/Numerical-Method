from multiprocessing import Condition
import numpy as np
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def fx(x,y,z,u):
    x= (3+2*y+z+u)/10
    return x
def fy(x,y,z,u):
    y= (15+2*x+z+u)/10
    return y
def fz(x,y,z,u):
    z= (27+x+y+2*u)/10
    return z
def fu(x,y,z,u):
    u= (-9+x+y+2*z)/10
    return u
  
x0, y0, z0, u0= 0, 0, 0, 0
epsilon = 0.0001
i=0
mytable = PrettyTable(["Iteration","x","y","z","u",])
condition=True
while condition:
    x1 =round( fx(x0,y0,z0,u0), 4)
    y1=round( fy(x0,y0,z0,u0), 4)
    z1=round( fz(x0,y0,z0,u0), 4)
    u1=round( fu(x0,y0,z0,u0), 4)
    # x = round(x,4)
    mytable.add_row([i,x0,y0,z0,u0])


    i+=1
    condition=abs(x1-x0)>=epsilon or abs(y1-y0)>=epsilon or abs(z1-z0)>=epsilon or abs(u1-u0)>=epsilon
    x0=x1
    y0=y1
    z0=z1
    u0=u1
mytable.add_row([i,x0,y0,z0,u0])
print('Solution using Jacobi Method:-')
print(mytable)
print("Hence, the solution of given problem is\nx= "+ str(x1) + ', y= '+ str(y1) + ', z= '+ str(z1) + ', u= '+ str(u1))
# print("The root of the function is: ",x)
