from math import *
import numpy as np
from matplotlib import pylab as plt
from partie1 import *

#----------Modeles de Malthus et Verlhulst--------------

def malthus_model(t, y, gamma):
    return gamma * y

def verhulst_model(t, y, gamma, kappa):
    return gamma * y * (1 - (y / kappa))

def sol_malthus(gamma, method):
    def f(t, y):
        return malthus_model(t, y, gamma)
    return meth_epsilon(1, 0, 3, 0.0001, f, method)

def sol_verlhust(gamma, kappa, method):
    def f(t, y):
        return verhulst_model(t, y, gamma, kappa)
    return meth_epsilon(1, 0, 4, 0.0001, f, method)

#---------------Modele de Lotka-Volterra------------------

def lotka_volterra_model(t, y, a, b, c, d):
    d_N = y[0] * (a - b * y[1])
    d_P = y[1] * (c * y[0] - d)
    return np.array([d_N, d_P])

def sol_lotka_voltera(ini, a, b, c, d, t_f, method):
    def f(t, y):
        return lotka_volterra_model(t, y, a, b, c, d)
    n_ini = ini[0]
    p_ini = ini[1]
    return meth_epsilon(np.array([n_ini, p_ini]), 0, t_f, 0.0001, f, method)

#------------------Periode des solutions-----------------

def period_solution(N, P, step, epsilon):
    T = 2 * step
    i = 2
    N_diff = abs(N[1] - N[i])
    P_diff = abs(P[1] - P[i])
    while((N_diff > epsilon) or (P_diff > epsilon)):
        T += p
        i += 1
    return T

#-------------------------Les tracés------------------------

def plot_malthus(method):
    for i in np.arange(4):
        s = sol_malthus(i, method)
        h = 1/len(s)
        t = np.arange(0, 1, h)
        plt.plot(t, s, label = "gamma")

    plt.ylabel("Population")
    plt.xlabel("Temps")
    plt.title("Solution (Malthus)")
    plt.legend()
    plt.show()

def plot_verlhust(method):
    for i in range(1, 5):
        s = sol_verlhust(2, i, method)
        h = 1/len(s)
        t = np.arange(0, 1, h)
        plt.plot(t, s, label = "Kappa")

    plt.ylabel("Population")
    plt.xlabel("Temps")
    plt.title("Solution (Verlhust)")
    plt.legend()
    plt.show()

def plot_lotka_volterra(ini, t_f, method):
    s = sol_lotka_voltera(ini, 0.5, 0.7, 0.5, 0.3, t_f, method)
    h = t_f / len(s)
    N = np.zeros([len(s)])
    P = np.zeros([len(s)])

    for i in range(1, len(s)):
        N[i] = s[i][0]
        P[i] = s[i][1]

    t = np.arange(0, t_f, h)
    T = period_solution(N, P, h, 0.01)
    print("Pour (a = 0.5, b = 0.7, c = 0.5 et d = 0.3), la période est: ", T)

    plt.plot(t, N, label = "Proies")
    plt.plot(t, P, label = "Predateurs")
    plt.xlabel("Temps")
    plt.ylabel("N(t) et P(t)")
    plt.title("Lotka-Volterra avec a = 0.5, b = 0.7, c = 0.5 et d = 0.3")
    plt.legend()
    plt.show()

#----------------Relation Proie-Prédateur -----------------

def plot_P_function_N(init, method):
    t_f = 50
    s = sol_lotka_voltera(init, 0.5, 0.7, 0.5, 0.3, t_f, method)
    h = t_f/len(s)
    N = np.zeros([len(s)])
    P = np.zeros([len(s)])

    for i in range(2, len(s)):
        N[i] = s[i][0]
        P[i] = s[i][1]
    plt.plot(N, P)

#-------------------Solution approchée --------------------

def sol_approx(init, method):
    r = 0.001
    n = init[0] - 3
    p = init[1] - 3

    for i in range(1, 4):
        n += r
        p += r
        plot_P_function_N(init, method)

    n = init[0]
    p = init[1]

    for i in range(1, 4):
        n += r
        p += r
        plot_P_function_N(init, method)

    plt.xlabel("Proies")
    plt.ylabel("Predateurs")
    plt.title("Prédateurs en fonction des proies")
    plt.legend()
    plt.show()
