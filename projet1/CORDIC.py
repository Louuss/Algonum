
import numpy as np
import matplotlib.pyplot as pl

L=[np.log(2), np.log(1.1), np.log(1.01), np.log(1.001), np.log(1.0001), np.log(1.00001), np.log(1.000001)]
A = [np.arctan(1), np.arctan(0.1), np.arctan(0.001), np.arctan(0.0001), np.arctan(0.00001), np.arctan(0.000001)]


def ln(x):
    k = 0
    y = 0
    p = 1

    while k<=6:
        while x >= p+p*(10**(-k)):
            y = y+L[k]
            p = p+p*(10**(-k))
        k = k+1

    return y + (x/p -1)




def arctan(x):
    k=0
    y=1
    r=0

    while ( k <= 4 ):
        while (x< y*10**(-k)):
            k=k+1
        xp = x-y *(10**(-k))
        y= y+x*(10**(-k))
        x=xp
        r=r+A[k]
    return r+(x/y)





def exp(x):
    k = 0
    y = 1

    while k <= 6:
        while x >= L[k]:
            x = x-L[k]
            y = y + y*(10**(-k))
        k = k+1
    return y + y*x

def tan(x):
    k=0
    n=0
    d=1

    while k<=4:
        while x>=A[k]:
            x = x-A[k]
            np = n+d*10**(-k)
            d = d-n*10**(-k)
            n = np
        k = k+1
    return (n+x*d)/(d-x*n)
