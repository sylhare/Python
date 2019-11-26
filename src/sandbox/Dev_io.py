# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:44:52 2015

"""
import os
import pickle  # Pour enregistrer et récupèrer des fichiers
from os.path import dirname, abspath

from ..tutorials import Tutoriel
from ..tutorials.Tutoriel import f  # Importe la fonction f() deTutoriel

# Test des imports
Tutoriel.table(5)  # Appel la fonction
print(Tutoriel.tronc3(3.999998978))
print(f(4))

# Accèder au dossier o`sont les fichiers pyhton
os.chdir("C:/Users/sylvain.hareng1/Documents/Python Scripts")  # On met '/' ou '//' et non '\'
os.getcwd()  # get CWD : Current Working Directroy

# Ouverture de fichier
mon_fichier = open("fichier.txt", "r")  # r - Read - leture du fichier
# a - Append - Ajoute à la fin du fichier du contenu
# b - Binairy - Ouvre le chier en mode binaire
contenu = mon_fichier.read()
print('1-', mon_fichier, '\n2-', contenu)
mon_fichier.close()  # Fermeture du fichier

mon_fichier = open("fichier.txt", "w")  # w - Write - Efface puis Écrit (remplace ce qui était là précèdemment)
mon_fichier.write("Premier test d'écriture dans un fichier via Python")  # Renvoie le nombre de caractères écrits
mon_fichier.close()

with open('fichier.txt', 'r') as variable:  # With permet de créer un context, d'ouvrir et fermer le fichier à la fin
    texte = variable.read()
print(mon_fichier.closed)  # Renvoi True si le fichier est fermé

# Utilisation du package Pickle
score = {
    "joueur 1": 5,
    "joueur 2": 35,
    "joueur 3": 20,
    "joueur 4": 2,
}
with open('donnees.test', 'wb') as fichier:  # wb comme écriture binaire,
    pikler = pickle.Pickler(fichier)  # Enregistrement, on peut modifer l'extension : ici c'est ".test"
    pikler.dump(score)

with open('donnees.test', 'rb') as fichier:  # rb comme écriture binaire,
    unPikler = pickle.Unpickler(fichier)  # lecture des objets contenus dans le fichier
    rScore = unPikler.load()

print(rScore)

# Filepath

print(os.path.sep.join(dirname(abspath(__file__)).split(os.path.sep)[:-1]))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.getcwd()))
readme = os.path.join("docs", "README.md")
print(os.path.join(os.path.dirname(os.getcwd()), readme))

# ==============================================================================
# ###Open two files
# try:
#     #with open('a', 'w') as a, open('b', 'w') as b:
#     f1 = open("plop.txt", "r")
#     f2 = open("test.txt", "w")
# except IOError as e:
#     print ("Erreur", e.errno, ":", e.filename, "n'a pas pu être ouvert (", e.strerror, ").")
# 
# f1.close()
# f2.close()
# 
# with open('primes 1.txt', 'rb') as fichier: #rb comme écriture binaire,
#    unpickler = pickle.Unpickler(fichier) #lecture des objets contenus dans le fichier
#    try: data = unpickler.load()
#    except EOFError: data = [] # or whatever you want
#
# print(data)
# ==============================================================================
