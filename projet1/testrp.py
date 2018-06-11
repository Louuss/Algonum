import rp
import os
import numpy
import matplotlib.pyplot as plt

#Definition des tests pour rp
def testrp_unit(num):
    print "  ", num, rp.rp(num, 4), rp.rp(num, 6)

def testrp():
    print "Essais de la fonction rp (Question 1 - Troncature des valeurs)"
    print "  x, rp(x, 4), rp(x, 6)"
    testrp_unit(3.141592658)
    testrp_unit(10507.1823)
    testrp_unit(0.0001857563)
    print

#Definition des tests pour sum
def testsum_unit(x,y,p):
    print "  ", x, y, p, x + y, rp.sum(x,y,p)

def testsum():
    print "Essais de la fonction sum (Question 2 - Addition simulee)"
    print "  x, y, p, x + y, sum(x,y,p)"
    testsum_unit(102422, 0.1458915, 4)
    testsum_unit(123, 42.1, 3)
    testsum_unit(0.00058, 0.000666, 2)
    print

#Definition des tests pour mul
def testmul_unit(x,y,p):
    print "  ", x, y, p, x * y, rp.mul(x,y,p)

def testmul():
    print "Essais de la fonction mul (Question 2 - Multiplication simulee)"
    print "  x, y, p, x + y, mul(x,y,p)"
    testmul_unit(102422, 0.1458915, 4)
    testmul_unit(123, 421, 3)
    testmul_unit(21.4578, 987.2115, 2)
    print

#Definition des tests pour erel_sum
def testerel_sum_unit(x,y,p):
    print "  ", x, y, p, rp.erel_sum(x,y,p)

def testerel_sum():
    print "Essais de la fonction erel (Question 3 - Erreur relative sur l'addition simulee)"
    print "  x, y, p, erel(x,y,p)"
    testerel_sum_unit(102422, 0.1458915, 4)
    testerel_sum_unit(123, 42.1, 3)
    testerel_sum_unit(0.00058, 0.000666, 2)
    print

#Definition des tests pour erel_mul
def testerel_mul_unit(x,y,p):
    print "  ", x, y, p, rp.erel_mul(x,y,p)

def testerel_mul():
    print "Essais de la fonction mul (Question 3 - Erreur relative sur la multiplication simulee"
    print "  x, y, p, x + y, erel_mul(x,y,p)"
    testerel_mul_unit(102422, 0.1458915, 4)
    testerel_mul_unit(123, 421, 3)
    testerel_mul_unit(21.4578, 987.2115, 2)
    print

def graph_erel_sum():
    x=numpy.arange(-850, 0, 0.1)
    y=[ rp.erel_sum(424.24242,v,3) for v in x]
    plt.title("Erreur relative d'une addition t + y avec t=424.24242")
    plt.plot(x, y, 'r')
    plt.show()

def graph_erel_mul():
    x=numpy.arange(-850, 850, 0.1)
    y=[ rp.erel_mul(424.24242,v,3) for v in x]
    plt.plot(x, y, 'r')
    plt.title("Erreur relative d'une multiplication t * y avec t=424.24242")
    plt.show()

def test_log2_unit(q):
    print "  [bound=10^" + str(q) + "]", rp.log2(q)

def test_log2():
    print "Essai de la fonction de calcul de ln(2) (Question 4 - Calcul de log2)"
    print "Valeurs de log(2)"
    print "  [Precision ] (machine, reel, erreur relative)"
    print "  [Arbitraire]", ("-", numpy.log(2), 0)
    [ test_log2_unit(q) for q in range(1,5)]


testrp()
testsum()
testmul()
testerel_sum()
testerel_mul()

test_log2()

graph_erel_sum()
graph_erel_mul()

print


