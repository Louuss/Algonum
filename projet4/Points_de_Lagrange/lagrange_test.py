import numpy as np
import matplotlib.pyplot as plt

import lagrange as lg
import newton_raphson as nr



# Fonctions utilitaires
def eval_f_jacob(S, U, dx):
    F= lg.sum_lambda(S)
    return (nr.calc(F, U), nr.jacob(F, U, dx))

def split_coordonate(point_list):
    return ( list(map( lambda P : P[0] ,point_list)), list(map( lambda P : P[1] ,point_list)))

def display_lagrange_points(S, dx, eps, P1, C1, P2, C2, U_list, C_list) :
    co=lg.search_points(S, dx, eps, U_list)
    for i in range(len(co)) : plt.plot(co[i][0], co[i][1], C_list[i] + 'o')
    for P in U_list : plt.plot(P[0], P[1], 'm.')
    plt.plot(P1[0], P1[1], C1 + 'o')
    plt.plot(P2[0], P2[1], C2 + 'o')

    plt.title("Points de lagrange dans un système orbital")

    plt.show()
    return co

# Définition de la configuration de test
# Système de forces
S=[lg.gravitational(   1., [        0. ,   0.]),
   lg.gravitational(0.01,  [        1. ,   0.]),
   lg.centrifugal  (   1,  [ 0.00990099, 0.])]

# Dimension de l'espace
dx=np.ones((2, 1)) * (10**-8)

# Liste des points proches des points de lagranges
U_list=[[0.01,0], [1.5, 0], [ -1.15, 0], [0.5, 0.5], [0.5, -0.5]]


print ("Test de la configuration")
(FU, JU)=eval_f_jacob(S, np.matrix([U_list[1]]).T, dx)
print (FU)
print (JU)

# Représentation graphique des points de lagrange identifiés
print("Calcul des points de Lagrange")
for p in display_lagrange_points(S, dx, 10**(-6), [0, 0], 'y', [1, 0], 'b', U_list, ['k', 'k', 'k', 'k', 'k']) :
    print (p)
