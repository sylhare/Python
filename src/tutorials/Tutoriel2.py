# -*- coding: utf-8 -*-

# Créer ses propres packages
"""
Créer un repertoire avec le même nom que le package,
dans le même dossier que votre programme Python.
Dans ce répertoire, vous pouvez soit :
   - mettre vos modules, vos fichiers à l'extension .py ;
   - créer des sous-packages de la même façon, en créant un répertoire dans votre package
"""
# import fonctionne comme dans java
import math  # Importe une bibliothèque de fonctions
# import timeit

import sys

sys.stdout = sys.__stdout__

# help("math") #Pour avoir e l'aide sur cette bibliothèque
print(math.sqrt(16))  # Racine carré
import math as m  # Renomme la bibliothèque pour plus de simplicité

print(m.sqrt(16))

from math import fabs  # Import de math (ne fonctionne pas en utilisant m) la fonction fabs

print(fabs(-5))  # fabs donne la valeur absolue du paramètre
print(fabs(2))

# Reference d'une fonction dans une autre
printbis = print  # L'objet pointe sur la fonction print

# Division float
10 / 3

# Division euclydienne
10 // 3

# Modulo ou reste de la division
10 % 3

vtest = 1
del vtest  # Supprime la variable
variable = 9
variable = 2 * variable + 1

"""Les trois guillmets pour faire une longue chaîne de texte"""
"Pour faire une chaîne de caractères"
'Pareil qu\' au dessus'

a = 1
b = 2
a, b = b, a  # permutation
a = b = 3  # affectation

# Pour effectuer une opération sur plusieur lignes
1 + 2 + 3 \
+ 4 + 5  # donnera 15

# Fonction type pour connaiître type de variable
type(variable)  # int
print(variable)  # 19
print("La variable =", variable, "!")

# Premier exemple de condition
b = 5
if a > 0:  # Si a est supérieur à 0
    b = 2  # Pour ajouter des conditions, il faut faire une tabulation puis entrée
    print(a, "et", b)  # Pas besoin d'antislash pour passer à la ligne
    print("a est positif")
elif a < 0:  # Pas de tab, contraction de else if
    b = 3
    print("a est négatif")
else:
    print("a est nul")

# Operateur
# <= inférieur ou égal à
# >= supérieur ou égal à
# == égal à
# != Différent de

bool_elem = False
if variable == 9 or bool_elem is not True and a != 0:
    print("a:", a, "et", variable, "mais bool est", bool_elem)

# Boucles
# while avec le mot clef continue
i = 1
while i < 20:  # Tant que i est inférieure à 20
    if i % 3 == 0:  # i=3,9,15 par exeemple les autres sont passés (6,12,18)
        i += 4  # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue  # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1  # Dans le cas classique on ajoute juste 1 à i

# for parcours une séquence =foreach
sequence = "Sequence de lettres ! oui"
for lettre in sequence:
    if lettre in "AEIOUYaeiouy":  # lettre est une voyelle
        print(lettre)
    elif lettre == '!':
        break  # Arrête la boucle

# Tout est objet en python -> ojet.method
chaine = str()  # Pour créer un objet de la classe string (chaine de charactere vide)
chaine = "NE CRIE PAS SI FORT !"
print(chaine)
print(
    "En minuscule : " + chaine.lower() + " en majuscule " + chaine)  # Sort la chaine en minuscule mais ne la change pas

# Avec format, on peut choisir l'ordre des infos dans print
prenom = "Paul"
nom = "Dupont"
age = 21
chaine = "Je m'appelle {} {} et j'ai {} ans.".format(prenom, nom, age)
print(chaine)  # On peut l'assigner ou non à une valeur
print(
    "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} "
    "ans.".format(prenom, nom, age, nom.upper())
)

# Concatenation
print(prenom + ", " + nom + ": " + str(age))  # il faut faire un cast le int en string avec str()

# Parcours et selection d'une chaîne
chaine = "Hello W0rld!"
print(chaine[0])  # Donne 'H'
print(chaine[0:2])  # Donne 'He'
print(len(chaine))  # longueur  d'une chaine -> len() est une fonction globale plutôt que faire chaine.len()
print(chaine[2:len(chaine)])  # On sélectionne la chaîne sauf les deux premières lettres
print(chaine[2:])  # De la troisième lettre (comprise) à la fin
print(chaine[:4])  # Du début jusqu'à la cinquième lettre non comprise

# Pour les lettres, il existe aussi count, find and replace
chaine = chaine.replace('e', '3')  # Remplace e par 3
print(str(chaine.find('l')) + " " + str(chaine.find('b')))  # Renvoi le nombre de lettres trouvé, -1 si faux
print(str(chaine.count('e')) + " " + chaine)  # Compte le nombre de e

# listes [element] et tuples(indice,element)
liste1 = []  # liste1=list() #On crée une liste
liste1.append([1, 2, 3])
type(liste1)
liste = []  # On crée une liste vide
liste = [1, 2, [], "Hype", -5]
liste.insert(2, "le 3")  # Insert "le 3" en troisième position
liste.append("new element")  # Ajoute un nouvel element à la liste, ne renvoie rien
print(liste[3], liste, liste1)  # Accès à toute la liste ou juste un élément
del liste[3]  # Supprime le quatrième element de la liste
liste.remove("new element")  # Retire la premiere occurence de la valeur dans la liste
liste1 += liste  # Ajoute liste à liste 1 #liste1.append(liste) marche aussi
print(liste1, '\n')

# Parcours de la liste
ma_liste = ['a', 'b', 'c']
i = 0  # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1  # On incrémente i, ne pas oublier !

# Cette méthode est cependant préférable
for elt in ma_liste:  # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt.upper())  # elt le upper est pour mieux le différencier

for elt in enumerate(ma_liste):  # Enumerate renvoie un tuples (indice, valeur)
    print(elt)  # Un tuple ne peut être modifié une fois créé

# Entre chaînes et listes
chaine = "bonjour à tous"
print(chaine.split(" "))  # Sépare une chaîne au niveau des espaces
liste = ['Bonjour', 'à', 'tous']
print(" ".join(liste))  # Réunit une liste avec des espaces

# Modification de la liste
liste0 = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in liste0]  # Donne le carré pour chaque élement de la liste
[nb for nb in liste0 if nb % 2 == 0]  # Affiche que les chiffres paires de la liste

inv = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
invReversed = [(nb, fruit) for fruit, nb in inv]  # Reversed fruit and quntity
inv = [(fruit, nb) for nb, fruit in sorted(invReversed, reverse=True)]
print(inv, '\n')

temp1 = list(range(100))
temp2 = [i * 2 for i in range(50)]
list(set(temp1) - set(temp2))  # Tiny bit longer
s = set(temp2)
[x for x in temp1 if x not in s]  # fastest
[item for item in temp1 if item not in temp2]  # Longest

# Dictionnaire : clef = chaine
dico1 = dict()  # Création object dictionnaire
dico = {}
dico["pseudo"] = "Agent"
dico["mot de passe"] = "*****"
dico["pseudo"] += " 007"  # Permet de modifier/remplacer la valeur du dictionnaire
print(dico)
print('\t', dico["mot de passe"])  # KeyError si la clef n'existe pas dans le dico

# Set comme petit dictionnaire
tets = set(["login", "mdp"])
print(tets)

# Dictionnaire : clef = chiffres /!\Non ordonné, si on supprime le 2 ça ne décale pas de 1
mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"

# Dictionnaire : clef = tuples
chess = {}
chess['a', 1] = "tour blanche"  # En bas à gauche de l'échiquier
chess['b', 1] = "cavalier blanc"  # À droite de la tour
chess['a', 2] = "pion blanc"  # Devant la tour
chess['b', 2] = "pion blanc"  # Devant le cavalier, à droite du pion

# Dictionnaire déj
placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}  # Syntax {clef : valeur}
del placard["chemise"]  # Supprime la clef
placard.pop("pantalon")  # Supprime la clef mais renvoie la valeur, ici 6

# Parcours des dictionnaires
fruits = {"pommes": 21, "melons": 3, "poires": 31}

# for key in fruits: #Parcours les clefs du dictionnaire
for key in fruits.keys():  # Parcours les clefs du dictionnaire : explicit
    print(key)
for valeur in fruits.values():  # Parcours les valeurs du dictionnaire : explicit
    print(valeur)
for cle, valeur in fruits.items():  # Parcours les clefs et valeurs d'un dictionnaire
    print("La clé {} contient la valeur {}.".format(cle, valeur))

# Sep pour choisir le separeur, et en end pour dire quoi mettre à la fin
parametres = {"sep": " >> ", "end": " -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)  # ** permet de formater selon le parametre
print("Voici", "un", "exemple", "d'appel", sep=" >> ", end=" -\n")
print("\n")
