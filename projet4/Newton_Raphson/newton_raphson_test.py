from newton_raphson import *
import newton_raphson_test_base as tb
import numpy.linalg as la
# Vecteur colonne de test
f=np.matrix([[tb.f0], [tb.f1], [tb.f2]])

# Jacobienne de f
J=np.matrix([[tb.g00, tb.g01, tb.g02],[tb.g10, tb.g11, tb.g12],[tb.g20, tb.g21, tb.g22]])

# Conditions de test
U0=np.matrix([10., 10., 10.]).T
IMAX=400
EPS=10**(-14)
dx=np.ones(f.shape) * 10**(-12)


def print_result(head, U):
    print(head)
    print("     > U          :", U[0].T)
    print("     > ||f(U)||   :", la.norm(calc(f, U[0])))
    print("     > Itérations :", U[1])
    print()

def print_item(head, I):
    print(head)
    print(I)
    print()

#-------------------------------------------------#

print ("Début des tests des implémentation de l'algorithme de Newton-Raphson")
print()

#-------------------------------------------------#
print ("  Conditions de test :")
print ("     > Point de départ U0 :", U0.T)
print ()
print ("     > Nombre maximal d'itérations :", IMAX)
print ()
print ("     > Précision demandée : ", EPS)
print ()
print ("     > Variation transmises : ", dx.T)
print ()


#-------------------------------------------------#
print ("     > f(U0) =", calc(f, U0).T)
print ()

#-------------------------------------------------#
print_result("  Méthode sans retour arrière et Jacobienne requise",
Newton_Raphson(f,J, U0, dx, IMAX, EPS))

#-------------------------------------------------#
print_result("  Méthode sans retour arrière et Jacobienne non requise",
Newton_Raphson_Auto_Jacob(f, U0, dx, IMAX, EPS))

#-------------------------------------------------#
print_result("  Méthode avec retour arrière et Jacobienne requise",
Backtracking_Newton_Raphson(f, J, U0, dx, EPS))

#-------------------------------------------------#
print_result("  Méthode avec retour arrière et Jacobienne non requise",
Backtracking_Newton_Raphson_Auto_Jacob(f, U0, dx, EPS))

#-------------------------------------------------#
print ("Fin des tests des implémentation de l'algorithme de Newton-Raphson")
