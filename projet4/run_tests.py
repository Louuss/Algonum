import sys




print ("=========== Test de Newton Raphson ============")
sys.path.append("./Newton_Raphson")
import newton_raphson_test
print ()

print ("========= Test des points de Lagrange =========")
sys.path.append("./Points_de_Lagrange")
import lagrange_test
print ()

print ("============== Test de Bairstow ===============")
sys.path.append("./Bairstow")
import bairstow_test
print ()

print ("===== Test de l'équilibre électrostatique =====")
sys.path.append("./Equilibre_Electrostatique")
import ES_equilibrium_test
print ()
