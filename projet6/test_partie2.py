from partie2 import *

print("Variations d’une population dans le modèle de Malthus")
plot_malthus(step_heun)

print("Variations d’une population dans le modèle de Velhust")
plot_verlhust(step_heun)

print("Variations d’une population dans le modèle de Lotka-Vloterra")
plot_lotka_volterra([1, 3], 80, step_heun)

print("Les solutions autour d’un point de départ donné")
sol_approx([1, 3], step_runge_kutta4)
