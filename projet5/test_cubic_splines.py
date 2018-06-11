from cubic_splines import *
import matplotlib.pyplot as plt


(dim,ex,ey,ix,iy) = load_foil("boe103.dat")

print("\nThe aifoil of the upper surface of the wing : \n")
print("\t abscissas : ", ex)
print()
print("\t ordinates : ", ey)
print()

#------------------------------ Test construct_A ---------------------------------#

print("\nTest construct_A\n")
A = construct_A(ex, ey)
print("\tMatrix A of the upper surface :\n")
affichage(A)
print()

#------------------------------ Test construct_B ---------------------------------#

print("\nTest construct_B\n")
B = construct_B(ex, ey)
print("\tVector B of the upper surface :\n")
print(B)
print()
#------------------------------ Test second_derivative_Y -------------------------#
print("second_derivatie_Y\n")
print("\tThe second derivative of ey after solving A Y\"=B\n", second_derivative_Y(A, B))
print() 

#------------------------------ Test identify_interval ---------------------------#

print("Test identify_interval\n")
print("\t The inferior index expected : 3 \t\t got :  ", identify_interval(ex, 0.026))
print("\t The inferior index expected : 0 \t\t got :  ", identify_interval(ex, 0.0))
print()

#------------------------------ Test zeta ----------------------------------------#

print("Test zeta\n")
print("\tzeta(ex, 0.25, 2)\texpected : 1.0  \t got : ", zeta(ex, 0.025, 2))
print("\tzeta(ex, 0.25, 2)\texpected : 0.0  \t got : ", zeta(ex, 0.01875, 2))
print()

#------------------------------ Test interpolation -------------------------------#

print("Test interpolation\n")

x_e = []
y_e = []
k_e = 0.0
while (k_e < 1.0):
    x_e.append(k_e)
    y_e.append(interpolation(ex, ey, k_e))
    k_e += 0.001
plt.xlabel("abscissa axis")
plt.ylabel("ordinate axis")
plt.plot(x_e, y_e, label="interpolation of the upper surface's airfoil")


x_i = []
y_i = []
k_i = 0.0
while (k_i < 1.0):
    x_i.append(k_i)
    y_i.append(interpolation(ix, iy, k_i))
    k_i += 0.001
plt.plot(x_i, y_i, label="Interpolation of the lower surface's airfoil")
plt.legend()
#plt.ylim(-0.1, 0.1)
plt.show()


