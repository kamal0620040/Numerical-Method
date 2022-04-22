import math

# Simpson 3h / 8
def f(x):
  return  x**2 + math.e **x

a=0
b=3
n=6
h=(b-a)/6
s=0
for i in range (n+1):
    if i==0 or i== n:
        s=s+ f(a)
    elif i%3==0:
        s=s+ 2*f(a)
    else:
        s=s+ 3 * f(a)
    a=a+h
ans=round(s*3*h/8,4)
print('Solution using Simpson3h/8 rule is: ' + str(ans))
