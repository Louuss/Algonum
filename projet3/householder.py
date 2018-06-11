import numpy as np
from math import sqrt, floor, ceil
from random import randint
    
    
def is_zero(x):
    p = 0
    if (x < 10 ** (-10) ):
        return 1
    return 0

def norme(V, n):
    s = 0.
    for i in range(n):
        s += V[i, 0]**2
    return sqrt(s)

def matrix_multiplication(A, B):
    m, n  = A.shape
    tmp, p = B.shape
    if ( n != tmp ):
        return False
    M = np.matrix( [[0. for _ in range(p)] for _ in range(m)] )
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i, j] += A[i, k] * B[k, j]
    return M

def transpose_matrix(M):
    n, p = M.shape
    transpose_M = np.matrix( [[0. for _ in range(n)] for _ in range(p)] )
    for i in range(p):
        for j in range(n):
            transpose_M[i, j] = M[j, i]
    return transpose_M

#on sup X et Y sont des vecteurs de meme taille
def householder(X, Y):
    n = X.shape[0]
    U = X - Y
    N = norme(U,n)
    if N != 0:
        U = (1./N)*U
    transpose_U = transpose_matrix(U)
    #H = - 2.*matrix_multiplication(U, transpose_U)
    H = - 2.*np.dot(U, transpose_U)
    for i in range(n):
        H[i, i] += 1.
    return (H, U)


def generate_x_y(n):
    X = np.matrix( [[0.] for _ in range(n)] )
    Y = np.matrix( [[0.] for _ in range(n)] )
    for i in range(n):
        X[i, 0] = randint(0, 5)
    Y[0, 0] = norme(X, n)
    return (X, Y)
    
def pretty_vector(V):
    n, p = V.shape
    for i in range(n):
        for j in range(p):
            if is_zero(V[i, j]):
                V[i, j] = 0
    return V    


X, Y = generate_x_y(3)

H, U = householder(X, Y)

print("\n",pretty_vector(matrix_multiplication(H, X)))
print("\n",Y)


def householder_multiplication_vector(U, X):
    transpose_U = transpose_matrix(U)
    Tmp =  matrix_multiplication(transpose_U, X)
    Tmp = matrix_multiplication(U, Tmp)
    return (X - 2*Tmp)


# On suppose M carré
def householder_multiplication(U, M):
    n = U.shape[0]
    result = np.matrix( [[0. for _ in range(n)] for _ in range(n)] )
    tmp = np.matrix( [[0.] for _ in range(n)] )
    for j in range(n):
        for i in range(n):
            tmp[i, 0] = M[i, j]
        tmp = householder_multiplication_vector(U, tmp)
        for i in range(n):
            result[i, j] = tmp[i, 0]
    return result



print("\n", pretty_vector(householder_multiplication_vector(U, X)))
print("\n", Y, "\n")

    
