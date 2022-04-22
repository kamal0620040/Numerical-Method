


# Euler method page-8 of slide(differential eqn)
def f(x,y):
  return  round((y**2 - x**2)/(y**2 + x**2), 4)
def fy(x,y,h):
    print('***********')


    return round(y + h * f(x,y), 4)
a=0
b=1
n=5
h=(b-a)/n
s=0

for i in range(n):
    s=fy(a,b,h)
    print(s)
    a=a+h
    b=s
