from load_foil import *
from scipy import misc 

def affichage(A):
    for i in A:
        print(i.tolist())

def h(X, i):
    return X[i+1] - X[i]
 
def construct_A(X, Y):
    n = len(X) - 1
    diag = []
    for i in range(1, n):
        diag.append((h(X, i-1) + h(X,i))/3)
    A = np.diag(diag)
    for i in range(n-2):
        A[i][i+1] = h(X, i)/6
        A[i+1][i] = h(X, i)/6
    return A

def construct_B(X, Y):
    n = len(Y) - 2
    B = np.zeros((n, 1))
    for i in range(n):
        B[i][0] = (1/( X[i+1] - X[i])) * (Y[i+1] - Y[i]) - (1/(X[i] - X[i-1])) * (Y[i] - Y[i-1])
    return B

def second_derivative_Y(A, B):
    t = np.linalg.solve(A, B)
    d = [0]
    for e in t:
        d.append(e[0])
    d.append(0)
    return d
    

def identify_interval(X, x):
    n = len(X)
    for i in range(n):
        if (x == X[i]):
            return i
        if(x < X[i]):
            return (i-1)

def zeta(X, x, i):
    return (x-X[i])/(X[i+1]-X[i])
    

def interpolation(X, Y, x):
    A = construct_A(X, Y)
    B = construct_B(X, Y)
    i = identify_interval(X, x)
    second_derivative = second_derivative_Y(A, B)
    return (1-zeta(X, x, i))*Y[i] + zeta(X, x, i)*Y[i+1] + ((h(X,i)**2)/6)*(((1-zeta(X, x, i))**3-(1-zeta(X, x, i)))*second_derivative[i]+(zeta(X, x, i)**3-zeta(X, x, i))*second_derivative[i+1])

    
def interpolation_above(X, Y, lbd, x):
    return ((1-lbd)*interpolation(X, Y, x) + lbd*3*0.1) 


def interpolation_below(X, Y, lbd, x):
    return (lbd*interpolation(X, Y, x) - (1-lbd)*3*0.029) 
