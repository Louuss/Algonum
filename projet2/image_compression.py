# Compression d'image

import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

earth_full = mp.image.imread("p3_earth_base.png")
takeoff_full = mp.image.imread("p3_takeoff_base.png")

def transform(x) :
    n = np.shape(x)[0]
    M = np.zeros((n,n))

    for i in range(n):
        M[i][i] = x[i]
    return M

def trunc(M):
    (n,m) = np.shape(M)
    for i in range(n) :
        for j in range(m) :
            if M[i][j] < 0 :
                M[i][j] = 0
            elif M[i][j] > 1 :
                M[i][j] = 1
    return M

def split(M):
    (m,n,p) = np.shape(M)
    R = np.zeros((m, n))
    G = np.zeros((m, n))
    B = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            R[i][j] = M[i][j][0]
            G[i][j] = M[i][j][1]
            B[i][j] = M[i][j][2]
    return (R, G, B)

def merge(R, G, B):
    (m,n) = np.shape(R)
    M = np.zeros((m,n,3))
    for i in range(m) :
        for j in range(n) :
            M[i][j] = [R[i][j], G[i][j], B[i][j]]
    return M

            
def compress_one(M, k) :
    n = np.shape(M)[0]
    
    for i in range(k + 1,n):
        M[i][i] = 0

#We had to use the numpy svd due to the failure of the use of the SVD fuction created by our friends... 
def compress(M, k):
    (m, n, p) = np.shape(M)
    (R, G, B) = split(M)
    (Ur, Sr, Vr) = np.linalg.svd(R, full_matrices=False)
    (Ug, Sg, Vg) = np.linalg.svd(G, full_matrices=False)
    (Ub, Sb, Vb) = np.linalg.svd(B, full_matrices=False)

    Sr = transform(Sr)
    Sg = transform(Sg)
    Sb = transform(Sb)
    
    compress_one(Sr, k)
    compress_one(Sg, k)
    compress_one(Sb, k)

    
    R = trunc(np.dot(Ur, np.dot(Sr, Vr)))
    G = trunc(np.dot(Ug, np.dot(Sg, Vg)))
    B = trunc(np.dot(Ub, np.dot(Sb, Vb)))

    
    Mcomp = merge(R, G, B)
    return Mcomp

    
earth_10 = compress(earth_full, 10)
earth_50 = compress(earth_full, 50)
earth_100 = compress(earth_full, 100)

takeoff_5 = compress(takeoff_full, 5)
takeoff_50 = compress(takeoff_full, 50)
takeoff_130 = compress(takeoff_full, 130)

plt.figure()
plt.imshow(earth_full)
plt.figure()
plt.imshow(earth_10)
plt.figure()
plt.imshow(earth_50)
plt.figure()
plt.imshow(earth_100)

plt.figure()
plt.imshow(takeoff_full)
plt.figure()
plt.imshow(takeoff_5)
plt.figure()
plt.imshow(takeoff_50)
plt.figure()
plt.imshow(takeoff_130)
plt.show()
