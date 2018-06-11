import numpy as np
import sys
sys.path.append("../Newton_Raphson")
from newton_raphson import *
from math import *


def sum1(u, i, N):
    s = 0
    for j in range(N):
        if (j != i):
            s += (1/(u[i]-u[j]))
    return s

# Génère la composante i du gradient de E            
def composante_i(u, i, N):
    return (1/(u[i]-1)) + (1/(u[i]+1)) + sum1(u, i, N)


# Génère F = gradient (E)
# N : nombre de charges électrostatiques
def generate_F(N):
    return np.matrix(list(map( lambda i : lambda U : composante_i(U, i, N), range(N)))).T


def sum2(i, u, N):
    s = 0
    for j in range(N):
        if (j != i):
            s += (1/(u[i]-u[j])**2)
    return s

# Génère la composante (i, k) de la matrice jacobienne de F
def composante_jacobienne_i_k(i, k, u, N):
    if(i == k):
        return -((1/(u[i]-1)**2) + (1/(u[i]+1)**2) + sum2(i, u, N))
    else:
        return (1/(u[i]-u[k])**2)

# Génère la jacobienne de gradient de E 
# N : nombre de charges électrostatiques 
def generate_jacobienne(N):
    return np.matrix(list(map(lambda i : list(map(lambda k : lambda U : composante_jacobienne_i_k(i, k, U, N), range(N))), range(N))))


def est_definie_positive(x):
    return np.all(np.linalg.eigvals(x) > 0)
