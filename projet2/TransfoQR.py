import numpy as np
from random import randint
import matplotlib.pyplot as mp
from householder import norme, householder, householder_multiplication


#M bidiag superieure
def conv(M):
    n = len(M)
    norme = 0
    for i in range(n-1):
        norme+=abs(M[i,i+1])
    return norme
    
def is_zero(x):
    p = 0
    if (x < 10 ** (-10)):
        return 1
    return 0

def abs(x):
    if x>0. :
        return x
    return -x
    
def gap_between(x, y):
    return abs(x-y)

def pretty_vector(V):
    n, p = V.shape
    for i in range(n):
        for j in range(p):
            if is_zero(V[i, j]):
                V[i, j] = 0.
    return V    

def S_diagonal_gap(S, n):
    gap = 0
    for i in range(n):
        for j in range(n):
            if (i != j):
                gap += gap_between(S[i, j], 0)
    return gap

def draw_S_convergence(Y, NMax):
    X = np.array( [k for k in range(NMax+2)] )
    mp.ion()
    mp.figure("Graphique representant l'ecart entre la norme des elements extra-diagonaux de S et 0 :")
    mp.plot(X, Y, linewidth=1)
    mp.show()
    mp.pause(5)

def SVD1(NMax, BD):
    n = np.shape(BD)[0]
    S = BD
    U = np.eye(n,n)
    V = np.eye(n,n)
    Y = np.array( [0. for _ in range(NMax+2)] )
    Y[0] = gap = S_diagonal_gap(S, n)
    for i in range(NMax):
        Q1, R1 = np.linalg.qr(np.transpose(S))
        Q2, R2 = np.linalg.qr(np.transpose(R1))
        S = R2
        U = np.dot(U,Q2)
        V = np.dot(np.transpose(Q1),V)
        # ajout des coordonnees pour tracer la convergence de S vers une matrice diagonale :
        Y[i+1] = S_diagonal_gap(S, n)
        # verification de l'invariant UxSxV = BD
        test = pretty_vector(np.dot(U, np.dot(S, V))) 
        for i in range(n):
            for j in range(n):
                if ( gap_between(test[i, j], BD[i, j]) > 10 ** (10) ):
                    exit("L'invariant U*S*V = BD n'est pas verifie, le test est faux.")
    print("\nMatrice U*S*V obtenue (supposee egale a BD) :\n", test)
    print("\nMatrice BD :\n", BD, "\n")
    Y[NMax+1] = S_diagonal_gap(S, n)
    S = pretty_vector(np.dot(np.eye(n, n), S))
    draw_S_convergence(Y, NMax)
    return (U, S, V)

def generate_bidiagonal(n):
    BD = np.matrix( [[0 for _ in range(n)] for _ in range(n)] )
    for i in range(n):
        BD[i, i] = randint(0, 255)
    if ( randint(0, 1) ):
        for i in range(n-1):
            BD[i+1, i] = randint(0, 255)
    else:
        for i in range(n-1):
            BD[i, i+1] = randint(0, 255)
    return BD

def test_SVD1(NMax, taille):
    BD = generate_bidiagonal(taille)
    U, S, V = SVD1(NMax, BD)
    print("Matrice S obtenue (supposee diagonale) :\n", S, "\n")
    for i in range(taille):
        for j in range(taille):
            if ( i != j ) & ( S[i, j] != 0 ):
                return False
    return True
            
print("Booleen correspondant a la valuation de la convergance de S vers une matrice diagonale et de l'invariant de boucle U*S*V = BD : ", test_SVD1(50, 3))
 

#ne fonctionne pas
#M matrice carree
def mon_QR(M):
    n = len(M)
    R = M
    Q = np.eye(n,n)
    for i in range(n):
        y = np.zeros([n,1])
        #norme du vecteur M[:,i]
        s=0
        for j in range(n):
            s+=M[j,i]**2
        y[i] = s
        U = householder(M[:,i] ,y)[1]
       # print(householder(M[:,i],y)[0])
        print("i=",i)
        R = householder_multiplication(U, R)
        Q = householder_multiplication(U, Q)
    return (Q, R)

def SVD2(NMax,BD):
    X=np.zeros([NMax,1])
    for k in range(NMax):
        X[k] = k
    Y=np.zeros([NMax,1])
    n = len(BD)
    S = BD
    U = np.eye(n,n)
    V = np.eye(n,n)
    for i in range(NMax):
        Q1, R1 = mon_QR(np.transpose(S))
        Q2, R2 = mon_QR(np.transpose(R1))
        S = R2
        Y[i] = conv(S)
        U = np.dot(U,Q2)
        V = np.dot(np.transpose(Q1),V)
    return (U, S, V, X, Y)
        
    

print("Test de mon_QR")
A=np.matrix([[12, -51, 4],[6, 167, -68],[-4, 24, -41]])
print("A=",A)
qr = mon_QR(A)
print("Q=", qr[0])
print("R=", qr[1])



print()
#temps d'attente tres long et on n'obtient pas le resultat attendu
print("Test de SVD2")

X2=SVD2(10,M)[3]
Y2=SVD2(10,M)[4]

mp.plot(X2,Y2)
mp.show()
