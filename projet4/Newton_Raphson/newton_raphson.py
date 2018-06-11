import numpy as np
import numpy.linalg as la
import math

def __solve_solve(A, B):
    return la.solve(A, B)

def __solve_lstsq(A, B):
    return la.lstsq(A, B)[0]

__solve=__solve_lstsq

def calc(j, U):
#-------------------------------------------------#
#--- Calcule l'image de U par j ------------------#
#-------- j : Vecteur colonne de fonctions -------#
#-------- U : Vecteur colonne de nombres ---------#
#--- Retourne l'image de U par j -----------------#
#--- Remarques :                                  #
#                                                 #
#       Les fonctions du vecteur j doivent accep- #
#    ter comme unique argument une liste et re-   #
#    tourner un nombre.                           #
#                                                 #
#-------------------------------------------------#
    x=U.T.tolist()[0]
    Q=np.zeros(j.shape)
    for i in range(0, j.shape[0]):
        for k in range(0, j.shape[1]):
            Q[i,k] = j[i,k](x)
    return Q

def dim_der(f, U, n, h):
#-------------------------------------------------#
#--- Calcule les nombres derives en U de plu-     #
# sieurs fonctions a variables multiples. --------#
#-------- f : Vecteur colonne de fonctions -------#
#-------- U : Vecteur colonne de nombres ---------#
#-------- n : Indice de la dimension pour laquel- #
# le calculer le nombre derive -------------------#
#-------- h : Nombre definissant l'ecart sur le-  #
# quel caluler le nombre derive. -----------------#
#--- Retourne les nombres derives en U des fonc-  #
# tions du vecteur f pour la dimension n. --------#
#-------------------------------------------------#
    V=np.copy(U)
    V[n]=float(V[n]) + float(h)
    return (f(V) - f(U)) / h

def jacob(f, U, dx):
#-------------------------------------------------#
#--- Calcule l'image en U d'une matrice jaco-     #
# bienne basee sur un vecteur de fonction f. -----#
#--------  f : Vecteur colonne de fonctions ------#
#--------  U : Vecteur colonne de nombres --------#
#-------- dx : Ecart avec lequel calculer les     #
# nombres derives contenu dans la sortie ---------#
#--- Retourne l'image en U de la jacobienne asso- #
# ciee a f. --------------------------------------#
#-------------------------------------------------#
    n=f.shape[0]
    Q=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            Q[i][j]=dim_der(f[i,0], U, j, dx[i,0])
    return Q

def __Newton_Raphson_G(f, J, U0, dx, N, eps, jcb_func): #jcb_func(f, J, U, dx)
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton. ---------------#
#--------        f : Vecteur colonne de fonctions #
# du systeme d'equation. -------------------------#
#--------        J : Matrice Jacobienne de f -----#
#--------       U0 : Vecteur colonnne servant de  #
# point de depart a l'algorithme. ----------------#
#--------       dx : Vecteur colonne des var-     #
# iations ----------------------------------------#
# des variables du systeme. ----------------------#
#--------        N : Nombre maximal d'iterations -#
#--------      eps : Precision a atteindre -------#
#-------- jcb_func : Fonction retournant l'image  #
# d'une matrice jacobienne en U. Signature :      #
# (f, J, U, dx). ---------------------------------#
#-------------------------------------------------#
    IM=N
    tol=la.norm(calc(f, U0))
    ndx=la.norm(dx)
    Dx=__solve(jcb_func(f, J, U0, dx), calc(f, U0))
    while (( la.norm(Dx) > ndx ) and ( tol > eps) and (N > 0)):
        U0=U0-Dx
        tol=la.norm(calc(f, U0))
        Dx=__solve(jcb_func(f, J, U0, dx), calc(f, U0))
        N-=1
    return (U0, IM - N)

def Newton_Raphson(f, J, U0, dx, N, eps):
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton. ---------------#
#--------  f : Vecteur colonne de fonctions du    #
# systeme d'equation. ----------------------------#
#--------   J : Matrice Jacobienne de f ----------#
#--------  U0 : Vecteur colonnne servant de point #
# de depart a l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du systeme. ----------------------#
#--------   N : Nombre maximal d'iterations ------#
#-------- eps : Precision a atteindre ------------#
#-------------------------------------------------#
    return __Newton_Raphson_G(f, J, U0, dx, N, eps, lambda f, J, U, dx : calc(J, U))

def Newton_Raphson_Auto_Jacob(f, U0, dx, N, eps):
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton sans demander   #
# la matrice Jacobienne de f. --------------------#
#--------  f : Vecteur colonne de fonctions du    #
# systeme d'equation. ----------------------------#
#--------  U0 : Vecteur colonnne servant de point #
# de depart a l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du systeme. ----------------------#
#--------   N : Nombre maximal d'iterations ------#
#-------- eps : Precision a atteindre ------------#
#-------------------------------------------------#
    return __Newton_Raphson_G(f, None, U0, dx, N, eps, lambda f, J, U, dx : jacob(f, U, dx))

def Backtracking_Second_Loop_Action(lbd, f, U, Dx):
#-------------------------------------------------#
#     Action de la boucle de :                    #
#          Backtracking_Main_Loop_Action          #
#-------------------------------------------------#
    lbd=lbd/2

    # Calcul du vecteur colonne avec la
    # retroaction appliquee
    Z=U-lbd*Dx
    FZ=calc(f, Z)

    return (lbd, Z, FZ)


def Backtracking_Main_Loop_Action(f, U, lbd, dx, K, J, jcb_func):
#-------------------------------------------------#
#     Action de la boucle de :                    #
#          Backtracking_Newton_Raphson            #
#-------------------------------------------------#
    # Image de U par f
    FU=calc(f, U)
    nFU=la.norm(FU)

    # Distance de U au vecteur solution de
    # l'algothime de Newton non optimise
    Dx=__solve(jcb_func(f, J, U, dx), FU)

    # Recherche d'une solution convergente
    # entre U et U+Dx
    (lbd, Z, FZ)=Backtracking_Second_Loop_Action(lbd, f, U, Dx)
    K+=1
    while( (la.norm(FZ) > (1 - lbd / 2)* nFU) and ( lbd > 1/256 ) ):
        (lbd, Z, FZ)=Backtracking_Second_Loop_Action(lbd, f, U, Dx)
        K+=1

    return (Z, FZ, Dx, K)


def __Backtracking_Newton_Raphson_G(f, J, U0, dx, eps, jcb_func):
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton avec l'optimi-  #
# sation de retour en arriere. -------------------#
#--------        f : Vecteur colonne de fonctions #
# du systeme d'equation. -------------------------#
#--------        J : Matrice Jacobienne de f -----#
#--------       U0 : Vecteur colonnne servant de  #
# point de depart a l'algorithme. ----------------#
#--------       dx : Vecteur colonne des var-     #
# iations ----------------------------------------#
# des variables du systeme. ----------------------#
#--------      eps : Precision a atteindre -------#
#-------- jcb_func : Fonction retournant l'image  #
# d'une matrice jacobienne en U. Signature :      #
# (f, J, U, dx). ---------------------------------#
#-------------------------------------------------#
    ndx=la.norm(dx)

    # Facteur de retroaction
    lbd=2

    # Recherche d'une solution
    I=1
    K=0
    (U, FU, Dx, K)=Backtracking_Main_Loop_Action(f, U0, lbd, dx, K, J, jcb_func)
    while( ( la.norm(Dx) > ndx ) and ( la.norm(FU) > eps ) ):
        (U, FU, Dx, K)=Backtracking_Main_Loop_Action(f, U, lbd, dx, K, J, jcb_func)
        I+=1
    return (U, K)


def Backtracking_Newton_Raphson(f, J, U0, dx, eps):
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton avec l'optimi-  #
# sation de retour en arriere. -------------------#
#--------  f : Vecteur colonne de fonctions du    #
# systeme d'equation. ----------------------------#
#--------   J : Matrice Jacobienne de f ----------#
#--------  U0 : Vecteur colonnne servant de point #
# de depart a l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du systeme. ----------------------#
#-------- eps : Precision a atteindre ------------#
#-------------------------------------------------#
    return __Backtracking_Newton_Raphson_G(f, J, U0, dx, eps, lambda f, J, U, dx : calc(J, U))


def Backtracking_Newton_Raphson_Auto_Jacob(f, U0, dx, eps):
#-------------------------------------------------#
#--- Approxime la solution d'un systeme non li-   #
# neaire par la methode de Newton avec l'optimi-  #
# sation de retour en arriere. -------------------#
#--------  f : Vecteur colonne de fonctions du    #
# systeme d'equation. ----------------------------#
#--------  U0 : Vecteur colonnne servant de point #
# de depart a l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du systeme. ----------------------#
#-------- eps : Precision a atteindre ------------#
#-------------------------------------------------#
    return __Backtracking_Newton_Raphson_G(f, None, U0, dx, eps, lambda f, J, U, dx : jacob(f, U, dx))
