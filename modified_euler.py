
# Heun's Method (Modified Eurler method)
def f(x,y):
  return round(x - y**2, 4)

def fyn(x,y, h):
  return  round ( y + h* f(x,y) , 4 ) 

def fy(x,y,yn, h):
  return round(y + h * (f(x,y) + f(x+h,yn)) / 2 ,4)


a=0
b=1
y=1
n=4
h=(b-a)/n
 
for i in range(n):
  yn=fyn(a,y,h)
  y=fy(a,y,yn,h)

  print(yn)
  print(y) 
  print('**************')
  a=a+h
