import numpy as np

def f(x):
    return np.exp((-(x)**2)/2)

def simpson1_3(a,b,n):
    h=(b-a)/n
    sum = f(a)+f(b)
    for i in range(1,n):
        y = a + i*h

        if i%2 == 0:
            sum = sum + 2 * f(y)
        else:
            sum = sum + 4 * f(y)
    integration = (sum * h/3)
    return np.around(integration / (np.sqrt(2*np.pi)),4)

# Given data:
lower_limit = -4
upper_limit = 4
sub_intervals = 50

print("The value of integration Simpson Rule:",simpson1_3(lower_limit,upper_limit,sub_intervals))