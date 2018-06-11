import numpy as np
import sys
sys.path.append("../Newton_Raphson")
import newton_raphson as nr
import matplotlib.pyplot as plt
from functools import reduce
from math import *

# Définition des forces.
def centrifugal_component(k, x, x0):
    return k * (x - x0)

def centrifugal(k, U0):
    return list(map( lambda i : lambda U : centrifugal_component(k, U[i], U0[i]), [0, 1]))

def gravitational_component(k, i, U, U0):
    return -k * (U[i] - U0[i]) / pow( (U[0] - U0[0])**2 + (U[1] - U0[1])**2 , 1.5)

def gravitational(k, U0):
    return list(map( lambda i : lambda U : gravitational_component(k, i, U, U0), [0, 1]))

def elastic(k, x0):
    return [lambda U : -k * (U[0] - x0)]

# Fonctions outils.
def sum_lambda(S):
    return np.matrix(list(map( lambda i : reduce(lambda x,y : lambda U : x(U) + y(U), map(lambda j : S[j][i], range(len(S)))),
                               range(len(S[0]))))).T
# Recherche de solutions à partir de points de départ multiples.
def search_points(S, dx, eps, U_list):
    F=sum_lambda(S)
    return list(map(lambda U : nr.Backtracking_Newton_Raphson_Auto_Jacob(F, np.matrix([U]).T, dx, 10**(-6))[0].T.tolist()[0], U_list))


