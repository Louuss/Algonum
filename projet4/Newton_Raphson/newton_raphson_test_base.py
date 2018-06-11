from math import *
#Définition des fonctions de la matrice f
def f0(U):
    return 3*U[0] - cos(U[1] * U[2]) - (3/2)

def f1(U):
    return 4 * U[0] * U[0] - 625 * U[1] * U[1] + 2 * U[2] - 1

def f2(U):
    return 20 * U[2] + exp(-U[0] * U[1]) + 9

#Définition des fonction de la matrice jacobienne de f
def g00(U):
    return 3

def g01(U):
    return U[2]*sin(U[1]*U[2])

def g02(U):
    return U[1]*sin(U[1]*U[2])

def g10(U):
    return 8 * U[0]

def g11(U):
    return -1250 * U[1]

def g12(U):
    return 2

def g20(U):
    return - U[1] * exp(- U[0] * U[1])

def g21(U):
    return - U[0] * exp(- U[0] * U[1])

def g22(U):
    return 20

