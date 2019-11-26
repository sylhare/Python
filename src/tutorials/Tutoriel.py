# -*- coding: utf-8 -*-


# Fonction affichant la table de multiplication par nb
def table(nb,
          max=10):  # max=10 permet de fournir une valeur par défaut, pas obligé de remplir le champs pour l'utilisateur
    """

    :param nb:
    :param max:
    """
    i = 0
    if max < 0:
        max = 10

    try:
        while i < max:  # Tant que i est strictement inférieure à la variable max
            print(i + 1, "*", nb, "=", (i + 1) * nb)
            i += 1
    except:
        print("Error, sans précisions")

    # Differents appels d'une fonction


def fonc(a=1, b=2, c=3, d=4, e=5):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    """
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
    # La fonction reconnait les variables ou change selon l'ordre des paramètres


fonc()  # default
fonc(4)  # a=4 reste inchangé
fonc(b=8, d=5)  # b et d changé
fonc(b=35, c=38, a=4, e=9)


# On redéfinit la même fonction
def fonc(v):
    """

    :param v:
    :return:
    """
    print("Pas de surcharge de fonction", v)
    return v * v


variable = 9
variable = fonc(variable)  # Variable aura la valeur retourné par fonc()

# Fonctions à une instruction
lambda x: x * x  # fonction non assignée, placé dans la mémoire
f = lambda x: x * x  # lambda arg1, arg2, ... : instruction
f(5)


def tronc3(flottant):  # Troncature 3 chiffres après la virgules
    """

    :param flottant:
    :return:
    """
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    int_part, float_part = flottant.split(".")
    return ",".join([int_part, float_part[:3]])  # La partie flottante est tronquée à 3 chiffres


# Paramètres libres
def fonction_inconnue(*en_liste, **en_dictionnaire):
    """

    :param en_liste:
    :param en_dictionnaire:
    """
    print(0)


def paramStar(*parametres):  # * indique que tous les paramètres seront placé dans un tuple puis manipulé
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    print("J'ai reçu : {}.".format(parametres))


def param2Star(**parametres_nommes):  # Récupère les paramètres assignés dans un dictionnaire
    """

    :param parametres_nommes:
    """
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))  # (p=4, j=8) ->  {'p': 4, 'j': 8}


# Refaire une fonction print (qui affiche tout les paramètres à l'écran)
# def afficher1(*parameters, sep=' ', end='\n', file=sys.stdout):
def afficher(*parameters, sep=' ', fin='\n'):
    """

    :param parameters:
    :param sep:
    :param fin:
    """
    parameters = list(parameters)  # Converti le tuple en liste pour plus de flexibilité

    for i, parameter in enumerate(parameters):  # Transforme chaque élément en string
        parameters[i] = str(parameter)
        chaine = sep.join(parameters)
        chaine += fin
    print(chaine, end='')  # On affiche


def fest():
    """

    """
    print("Let's party")


def bird():
    """

    """
    print("I believe I can fly")


functions = {}
functions["fest"] = fest  # On ne mets pas les parenthèses
functions["bird"] = bird
functions["bird"]()  # Pour appeler la fonction bird


def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables
    définies dans notre corps de fonction"""

    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après l'affectation, notre variable var vaut {0}.".format(var))


set_var(5)

i = 4  # Une variable, nommée i, contenant un entier


def iplus():
    """Fonction chargée d'incrémenter i de 1"""
    global i  # Python recherche i en dehors de l'espace local de la fonction
    i += 1


# Decorateur, pour modifier facilement le comportement d'une fonction
def decorateur(fonction):
    """

    :param fonction:
    :return:
    """
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction


def decorator(fct):
    """

    :param fct:
    :return:
    """

    def fct_modified():
        """

        :return:
        """
        print("We are calling {0}".format(fct))
        return fct()

    return fct_modified


@decorator
def fct_test():
    """

    """
    print("It's a trap!")


# Decorateur
# On peut mettre le decorateur directement en mettant un @
@decorateur
def salut():
    """Fonction modifiée par le décorateur"""
    print("Salut !")


# Ou on peut appeler une fonction par le décorateur pour la modifier
decorateur(salut)


def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine
    est obsolète"""

    def fonction_modifiee():
        """

        """
        raise RuntimeError("la fonction {0} est obsolète !".format(fonction_origine))

    return fonction_modifiee


"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""

import time


def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""

        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""

            tps_avant = time.time()  # avant d'exécuter la fonction
            ret = fonction_a_executer(*parametres_non_nommes,
                                      **parametres_nommes)  # Execute la fonction avec ses paramètres
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant

            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format( \
                    fonction_a_executer, tps_execution))
            return ret

        return fonction_modifiee

    return decorateur


# On peut chainer les décorateurs
@controler_temps(4)
@decorateur
def attendre():
    """
    Demo
    En appuyant rapidement sur entrée, rien ne se passe
    En attendant plus de 4s avant d'appuyer sur entrée, on a le temps d'execution de la fonction

    """
    input("Appuyez sur Entrée...")


attendre()  # En appuyant rapidement sur entrée, rien ne se passe
attendre()  # En attendant plus de 4s avant d'appuyer sur entrée, on a le temps d'execution de la fonction

# Mots clefs
# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# false
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# none
# nonlocal
# not
# or
# pass
# raise
# return
# true
# try
# while
# with
# yield
