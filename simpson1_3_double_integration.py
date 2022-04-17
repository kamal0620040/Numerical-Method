import numpy as np

def f(x,y):
    return x**2 + np.exp(y)

# Given data
a = 2
b = 3
c = 0
d = 2
n = 4

h = np.around((b - a) / n,4)
k = np.around((d - c) / n,4)

z=[[0 for row in range(0,n+2)] for col in range(0,n+2)]
print("The functional value table is:-"+'\n')
for i in range(n+2):
         for j in range(n+2):
            if(i == 0 and j == 0):
                z[i][j] = "f(x,y)"
            elif(i == 0):
                z[i][j] = z[i][j-1] + k if z[i][j-1] != "f(x,y)" else c
            elif(j==0):
                z[i][j] =  z[i-1][j] + h if z[i-1][j] != "f(x,y)" else a
            else:
                z[i][j] = np.around(f(z[i][0],z[0][j]),4)


# Display the Result:

for i in range(n+2):
         for j in range(n+2):
             print(z[i][j],end=' '* (8 - len(str(z[i][j]))))
         print("\n")

def label(k):
    if(k == 1):
        return 4
    elif(k == 4):
        return 2
    elif(k == 2):
        return 4
    else:
        return 1

c=[[0 for row in range(0,n+2)] for col in range(0,n+2)]
print("The coefficient table for simpson's rule is:")
for i in range(n+2):
         for j in range(n+2):
            if(i == 0 and j == 0):
                c[i][j] = "*"
            elif(i == 0):
                if(j == n+1):
                    c[i][j] = 1
                else:
                    c[i][j] = label(c[i][j-1])
            elif(j == 0):
                if(i == n+1):
                    c[i][j] = 1
                else:
                    c[i][j] = label(c[i-1][j])
            else:
                c[i][j] = c[i][0] * c[0][j]

for i in range(n+2):
         for j in range(n+2):
             print(c[i][j],end=' '* (8 - len(str(c[i][j]))))
         print("\n")

# sum of multiples of functional value and coefficient table
sum = 0
for i in range(1,n+2):
         for j in range(1,n+2):
             sum += z[i][j] * c[i][j]

print("The value of double integration by Simpson Rule:",np.around((h*k*sum)/9,4))