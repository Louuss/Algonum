from math import *
from curves_length import *
import numpy as np
import matplotlib.pyplot as plt

#Integration methods Test:


print("Test of the 5 integration methods:\n\n")
print("We compare the integral of f: x --> 1/(1+x) from 0 to 1 to the exact result, using 5 different integration methods :\n\n")
print("Expected value : ln(2) ≃", log(2) ,"\n")
print("The integration table\n")
integration_table(lambda x : 1/(1+x), 0, 1)
print("\n")


print("Graph comparing the 5 integration methods:\n")
axes = plt.gca()
axes.set_ylim([0,1.5])
x = np.arange(1, 100, 1)

#rectangular
rre = lambda x: rectangular(lambda z : 1/(1+z), 0, 1, x) 
re = [rre(k) for k in x]
#trapezoidal
tt = lambda x: trapezoidal(lambda z : 1/(1+z), 0, 1, x)
t = [tt(k) for k in x]
#simpson
ss = lambda x: simpson(lambda z : 1/(1+z), 0, 1, x)
s = [ss(k) for k in x]
#reinmann
rr = lambda x: riemann_sums(lambda z : 1/(1+z), 0, 1, x)
r = [rr(k) for k in x]
#romberg
rro = lambda x: romberg(lambda z : 1/(1+z), 0, 1, logg(x))
ro = [rro(k) for k in x]

plt.semilogx(x,re)
plt.semilogx(x,t)
plt.semilogx(x,s)
plt.semilogx(x,r)
plt.semilogx(x,ro)

plt.xlabel("Number of subdivisions")
plt.ylabel("Integral of f(x) : x --> 1/(1+x) from 0 to 1")
plt.legend(['y = rectangular method', 'y = trapezoidal method', 'y = simpson method', 'y = riemann_sums method', 'y = romberg method'], loc='lower right')

plt.show() 


print("\n")

print("Test of the function curve_length:\n")


print("The graph's length of f: x --> 1/(1+x) defined on [",0,",",1,"] using simpson method is :\n", (curve_length(simpson, lambda x : 1/(1+x), 0, 1, 10, 0.001)))
print("Expected value: 1.13209")
