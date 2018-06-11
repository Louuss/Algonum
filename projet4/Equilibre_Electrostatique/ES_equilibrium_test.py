from ES_equilibrium import *
import scipy as sp
from numpy.polynomial import Polynomial

# Conditions de test

U0=np.matrix([-0.5, 0.3]).T
IMAX=400
EPS=10**(-14)
dx=np.ones((1, 2)) * 10**(-12)
F=generate_F(2)
J=generate_jacobienne(2)
res = Newton_Raphson(F, J, U0, dx, IMAX, EPS)

print ("\nDébut des tests de l'implémentation de l'algorithme cherchant la position d'équilibre des charges\n")
print("   Tests pour N = ", 2)
print()
print("\t Position initiale = ", U0.T)
print()
print("\t Nombre d'itérations = ", res[1])
print()
print("\t Position d'équilibre = ", res[0].T)
print()
print("\t Racine de la dérivée du troisième polynome de Legendre = + ou -", sqrt(3/15))
print()
print( "\t Correspond au minimum d'énergie :", est_definie_positive(calc(J, res[0])))
print()


U00=np.matrix([-0.5, 0.3, 0.2, -0.1]).T
F=generate_F(4)
J=generate_jacobienne(4)
res2 = Newton_Raphson(F, J, U00, dx, IMAX, EPS)


print("   Tests pour N = ", 4)
print()
print("\t Position initiale = ", U00.T)
print()
print("\t Nombre d'itérations = ", res2[1])
print()
print("\t Position d'équilibre = ", res2[0].T)
print()
print( "\t Correspond au minimum d'énergie :", est_definie_positive(calc(J, res2[0])))
print()

p = Polynomial([0., 15/8, 0., -70/8, 0., 63/8]) 

print("\t Les racines de la dérivée du 5ème polynôme de Legendre = ", p.deriv().roots())
print()
print("\t Gradient de E évalué en la position d'équilibre = ", calc(generate_F(4),res2[0]).T)
print( "Correspond au minimum d'énergie :", est_definie_positive(calc(J, res2[0])))
print()



