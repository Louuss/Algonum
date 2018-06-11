from bairstow import *

#test polynoms
p1 = np.array([3.0, -4.0, -5.0])
p2 = np.array([3.0, -5.0, -4.0, 4.0])

#test polynom roots
r1 = np.array([-0.7862996, 2.1196329])
r2 = np.array([-1.0, 0.666666667, 2.0])


# def print_roots(U, p):
# 	print("test polynom : ", p[0], "x²+", p[1], "x+", p[2])
# 	print("Expected roots : ", r[0], r[1])
# 	p = np.array([1.0, U[0], U[1]])
# 	r_bairstow = np.roots(p)
# 	print("Obtained roots : ", r_bairstow[0], r_bairstow[1])
# 	print()

def test_bairstow(p, r):
	r_b = poly_roots(p)
	print("Expected roots : ", r)
	print("Obtained roots : ", r_b)


test_bairstow(p1, r1)
test_bairstow(p2, r2)
	






