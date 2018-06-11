from math import *
import numpy as np

######
######

def rectangular(f,a,b,n) : 
    h=(b-a)/float(n)
    area=0
    for i in range(n) :
        area=area+f(a+i*h)
    return h*area
    

######
######



def trapezoidal(f,a,b,n) :

    h=(b-a)/float(n)

    area=0.5*(f(a)+f(b))

    for i in range(1,int(n)) :

        area=area+f(a+i*h)

    return h*area


######
######


def simpson(f,a,b,n) :
    h=(b-a)/float(n)

    area=(f(a)+f(b))/6

    for i in range(1,n) :

        area=area+f(a+i*h)/3

    for i in range(n) :

        area=area+f(a+(2*i+1)*h/2)*2/3

    return h*area



######
######



def riemann_sums(f, a, b, n) :

    h=(b-a)/float(n)
    area = 0
    for i in range(n) :
        area=area+f(a+((2*i+1)*h/2))*h
    return area

######
######


def romberg(f,a,b,k,m=10):
    if(m==0):
        if(k==0):
            return (0.5*(b-a)*(f(a)+f(b)))
        return trapezoidal(f,a,b,2**k)
    return (((pow(4,m)*romberg(f,a,b,k,m-1))-(romberg(f,a,b,k-1,m-1)))/(pow(4,m)-1))

######
######



def derivative(f, h):
        def g(x):
            return (f(x+h) - f(x)) / h
        return g

######
######


def curve_length(integral_method, func, a, b, n=5, h=0.001):
    func_der = lambda x : sqrt(1 + derivative(func, h)(x)**2)
    return (integral_method(func_der, a, b, n))

def logg(x):
    if (x==8):   
        return 3
    elif (x==32):
        return 5
    return 7

######
######

def integration_table(f, a, b):
    print ("n       rectangular         trapezoidal           simpson         riemann_sums         romberg")
    for n in [8, 32, 128]:
        print ('%4s %18.9f %18.9f %18.9f %18.9f %18.9f'  % (n, rectangular(f, a, b, n), trapezoidal(f, a, b, n), simpson(f, a, b, n),riemann_sums(f, a, b, n), romberg(f,a,b,logg(n),m=10)))
'''
def f(x):
    return pow(x,8)
    
integration_table(f, -1, 1)
'''