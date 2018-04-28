# -*- coding: utf-8 -*-

import sys  # Importe les fonctions systèmes
# import os

# System computing
sys.stdout.write("Un test\n")
fichier = open('sortie.txt', 'w')
# sys.stdout = fichier
sys.stdout = sys.__stdout__
print("Quelque chose...")
fichier.close()  # Fermeture du fichier

sys.stdout = sys.__stdout__  # pour remettre la sortie par défaut
