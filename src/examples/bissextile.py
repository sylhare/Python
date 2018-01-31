# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:37:54 2015

Programme Simple, année bissextile ou non

@author: HS
@source: https://openclassrooms.com/courses/apprenez-a-programmer-en-python/pas-a-pas-vers-la-modularite-2-2
"""
import \
    math  # Importe toutes les fonctions deTutoriel.py et lance toutes les instructions (contenu dans le même répertoire)
import os  # On importe le module os qui dispose de variables
# et de fonctions utiles pour dialoguer avec votre
# système d'exploitation
# from Tutoriel import *  #Un peu bancale
from Tutoriel import f  # Importe la fonction f() deTutoriel.py et lance toutes les instructions

annee = input("Saisissez une année :")  # recupérer une variable type string du clavier
try:
    annee = int(annee)  # change le type en int
except ValueError:
    # Exécuté si une exception de type ValueError est levée dans le bloc try
    print("Error: need an Integer")
else:
    # Executé si pas d'exceptions
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.", math.sqrt(f(annee)))
    else:
        print("L'année saisie n'est pas bissextile.", math.sqrt(f(annee)))

# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
