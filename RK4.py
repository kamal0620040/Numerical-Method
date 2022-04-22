
def f(x,y):
    return round( y * (1 + x**2), 4)
def fk1(x,y,h ):
  return  round( h* f(x,y), 4)
def fk2(x,y,h,k1 ):
    return  round( h* f(x + h/2,y + k1/2), 4)
def fk3(x,y,h,k2 ):
    return  round( h* f(x + h/2,y + k2/2), 4)
def fk4(x,y,h,k3 ):
    return  round( h* f(x + h,y + k3), 4)

def fy(y,k1,k2,k3,k4):
   return round( y +  (k1 + 2*k2 + 2*k3 + k4)/6 , 4)
a=0.0
b=1.0
y=1.0
n=4
h=round((b-a)/n,4)
s=0.0

for i in range(n):
    k1=fk1(a,y,h)
    k2=fk2(a,y,h,k1)
    k3=fk3(a,y,h,k2)
    k4=fk4(a,y,h,k3)
    y=fy(y,k1,k2,k3,k4)
    
    print(k1)
    print(k2)
    print(k3)
    print(k4)
    print(y)
    print('******************')
    a=a+h
