
def f(x,y):
    return round( (y **2 - x**2) /(y**2 + x**2), 4)
def fk1(x,y,h ):
  return  round( h* f(x,y), 4)
def fk2(x,y,h,k1 ):
    return  round( h* f(x + h,y + k1), 4)


def fy(y,k1,k2):
   return round( y +  (k1 + k2)/2 , 4)
a=0
b=1
y=1
n=5
h=round((b-a)/n,4)
s=0.0

for i in range(n):
    k1=fk1(a,y,h)
    k2=fk2(a,y,h,k1)

    y=fy(y,k1,k2)
    
    print(k1)
    print(k2)

    print(y)
    print('******************')
    a=a+h
