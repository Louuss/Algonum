import numpy as np
import householder as hh

def bidiag(M, n, m):
    Qleft = np.eye(n)
    Qright = np.eye(n)
    BD = M
    for i in range(n - 1):
        #Let Q1 be a HH matrix mapping BD[i:n,i] on a vector with a single non-zero element
        X1 = np.matrix([[BD[k, i]] if k >= i else [0.] for k in range(n)])
        Y1 = np.array([[hh.norme(X1, n)] if j == i else [0.] for j in range(n)])
        (Q1,U1) = hh.householder(X1, Y1)
        Qleft = np.dot(Qleft, Q1)
        BD = np.dot(Q1, BD)
        if i != (m-2) :
            #Let Q2 be a HH matrix mapping BD[i,(i+1):m] on a vector with a single non-zero element
            X2 = np.matrix([[BD[i, k]] if k > i else [0.] for k in range(m)])
            Y2 = np.array([[hh.norme(X2, m)] if j == i+1 else [0.] for j in range(m)])
            (Q2,U2) = hh.householder(X2, Y2)
            Qright = np.dot(Q2, Qright) 
            BD = np.dot(BD, Q2)
    return(Qleft, BD, Qright)

M = np.matrix([[1., 2., 3.], [3., 4., 5.], [6., 7., 8.]])

(Qleft, BD, Qright) = bidiag(M, 3, 3)


print(Qleft)
print(BD)
print(Qright)
print()
for i in range(3):
    for j in range(3):
        if BD[i,j] < 10**(-15):
            BD[i,j] = 0
        if Qleft[i,j] < 10**(-15):
            Qleft[i,j] = 0
        if Qright[i,j] < 10**(-15):
            Qright[i,j] = 0
print(np.dot(np.dot(Qleft, BD), Qright))
