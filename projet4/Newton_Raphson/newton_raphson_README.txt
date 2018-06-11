Résumé des fichiers :
       newton_raphson.py : Contient les différentes implémentations de l'algorithme de newton-raphson.

       newton_raphson_test_base.py : Contient les définitions des fonctions de la matrice de test et de sa jacobienne.

       newton_raphson_test.py : Contient les tests à exécuter.

Exécution des test :
	> python3 newton_raphson_test.py
git commit -m "Ajout des instructions d'exécution et d'utilisation pour la partie newton_raphson


Note à l'attention des utilisateurs de newton_raphson.py :

      Newton_Raphson(f, J, U0, dx, N, eps)
#-------------------------------------------------#
#--- Approxime la solution d'un système non li-   #
# néaire par la méthode de Newton. ---------------#
#--------  f : Vecteur colonne de fonctions du    #
# système d'équation. ----------------------------#
#--------   J : Matrice Jacobienne de f ----------#
#--------  U0 : Vecteur colonnne servant de point #
# de départ à l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du système. ----------------------#
#--------   N : Nombre maximal d'iterations ------#
#-------- eps : Precision à atteindre ------------#
#-------------------------------------------------#

   Newton_Raphson_Auto_Jacob(f, U0, dx, N, eps)
#-------------------------------------------------#
#--- Approxime la solution d'un système non li-   #
# néaire par la méthode de Newton sans demander   #
# la matrice Jacobienne de f. --------------------#
#--------  f : Vecteur colonne de fonctions du    #
# système d'équation. ----------------------------#
#--------  U0 : Vecteur colonnne servant de point #
# de départ à l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du système. ----------------------#
#--------   N : Nombre maximal d'iterations ------#
#-------- eps : Precision à atteindre ------------#
#-------------------------------------------------#

   Backtracking_Newton_Raphson(f, J, U0, dx, eps)
#-------------------------------------------------#
#--- Approxime la solution d'un système non li-   #
# néaire par la méthode de Newton avec l'optimi-  #
# sation de retour en arriere. -------------------#
#--------  f : Vecteur colonne de fonctions du    #
# système d'équation. ----------------------------#
#--------   J : Matrice Jacobienne de f ----------#
#--------  U0 : Vecteur colonnne servant de point #
# de départ à l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du système. ----------------------#
#-------- eps : Precision à atteindre ------------#
#-------------------------------------------------#

Backtracking_Newton_Raphson_Auto_Jacob(f, U0, dx, eps)
#-------------------------------------------------#
#--- Approxime la solution d'un système non li-   #
# néaire par la méthode de Newton avec l'optimi-  #
# sation de retour en arriere. -------------------#
#--------  f : Vecteur colonne de fonctions du    #
# système d'équation. ----------------------------#
#--------  U0 : Vecteur colonnne servant de point #
# de départ à l'algorithme. ----------------------#
#--------  dx : Vecteur colonne des variations    #
# des variables du système. ----------------------#
#-------- eps : Precision à atteindre ------------#
#-------------------------------------------------#

Les implémentations avec backtracking offre de meilleures perfomance et une meilleure stabilité, elles sont a privilégier.

Les implémentation Auto_Jacob permettent de ne pas spécifier la matrice jacobienne. Ces implémentations ne sont recommmandée que si f contient des fonctions qui sont dérivable sur R.
