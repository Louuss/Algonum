import numpy as np
import householder as hh

def transposeLtoC(M):
    n = np.shape(M)[0]
    if n == 1:
        return M
    C = np.matrix([[M[i]]for i in range(n)])
    return C

def bidiag(M, n, m):
    Qleft = np.eye(n)
    Qright = np.eye(n)
    BD = M
    for i in range(n -1):
        #Let Q1 be a HH matrix mapping BD[i:n,i] on a vector with a single non-zero element
        print("BD", BD)
        print("BD[i : n] = ", BD[i : n, i])
        X1 = BD[i:n, i]
        print("X1 =", X1)
        print("|X1| =", hh.norme(X1, n - i))
        Y1 = np.array([[hh.norme(X1, n - i)] if j == 0 else [0.] for j in range(n-i)])
        print("step :", i)
        (Q1,U1) = hh.householder(X1, Y1)
        print("Q1 =", Q1)
        print("Coucou")
        Qleft[i : n, i : n] = np.dot(Qleft[i : n, i : n], Q1)
        BD[i : n, i : n] = np.dot(Q1, BD[i : n, i : n])
        if i != (m-2) :
            #Let Q2 be a HH matrix mapping BD[i,(i+1):m] on a vector with a single non-zero element
            X2 = np.transpose(BD[i, i+1:m])
            print("X2 =", X2)
            
            Y2 = np.array([[hh.norme(X2, m - i - 1)] if j == 0 else [0.] for j in range(m-i-1)])
            print("Y2 =", Y2)
            (Q2,U2) = hh.householder(X2, Y2)
            print("Q2 : ",Q2)
            Qright[i+1 : m, i+1 : m] = np.dot(Q2, Qright[i+1 : m, i+1 : m]) 
            BD[i+1 : m, i+1 : m] = np.dot(BD[i+1 : m, i+1 : m], Q2)
        print("end ofstep : ", i)
    return(Qleft, BD, Qright)

M = np.matrix([[1., 2., 3.], [3., 4., 5.], [6., 7., 8.]])

(Qleft, BD, Qright) = bidiag(M, 3, 3)


print(Qleft)
print(BD)
print(Qright)
print()
print(np.dot(np.dot(Qleft, BD), Qright))
