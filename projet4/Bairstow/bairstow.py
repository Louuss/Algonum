import numpy as np
import sys
sys.path.append("../Newton_Raphson")
import newton_raphson as nt


def polynomial_euclidian(p, b, c):
	v = np.array([1.0, b, c])
	(qq, rem) = np.polydiv(p, v)
	r = rem[0]
	if (rem.size == 1):
		s = 0
	else:
		s = rem[1]
	return (qq, r, s)
	

def bairstow(p):
	b = p[1]/p[0]  #We choose as first polynomial cefficients the normalization from the three leading coefficients of p
	c = p[p.size - 1]/p[0] 
	U0 = np.matrix([b, c]).T
	def r(U):
		(q, r, s) = polynomial_euclidian(p, U[0], U[1])
		return r
	def s(U):
		(q, r, s) = polynomial_euclidian(p, U[0], U[1])
		return s
	def rc(U):
		(q, r, s) = polynomial_euclidian(p, U[0], U[1])
		(qq, r1, s1) = polynomial_euclidian(q, U[0], U[1])
		return -r1
	def sc(U):
		(q, r, s) = polynomial_euclidian(p, U[0], U[1])
		(qq, r1, s1) = polynomial_euclidian(q, U[0], U[1])
		return -s1
	def sb(U):
		return -U[1]*rc(U)
	def rb(U):
		return -U[0]*rc(U)+sc(U)
	f = np.matrix([[r], [s]])
	j = np.matrix([[rb, rc], [sb, sc]])
	dx=np.ones(f.shape) * 10**(-12)
	return nt.Newton_Raphson(f, j, U0, dx, 400, 10**(-14))

def poly_roots(p):
	p1 = p
	roots_array = []
	while (p1.size > 2):
		(U, Ite) = bairstow(p1)
		r = np.array([1.0, U[0], U[1]])
		(q, rem) = np.polydiv(p1, r)
		p1 = q
		roots_array.append(np.roots(r)[0])
		roots_array.append(np.roots(r)[1])
	if (p1.size == 2):
		roots_array.append(-p1[1]/p1[0])
	return roots_array
