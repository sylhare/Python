# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:06:13 2016

"""
import os
import random
import sys
import time
from threading import Thread, RLock


#==============================================================================
# os.getcwd() 
# file = open("newfile.txt", "w")
# file.write('\n'+"hello world in the new file")
# file.write('\n'+"and another line")
# 
# file = open('newfile.txt', 'r')
# print (file.read())
# #file.read(number of character to read)
# #file.readline(line to print)
# #file.readlines() give back an array with the data
# file.close()
# 
#==============================================================================

##Multi Threading
#print("Avant le sleep...")
#time.sleep(5) #Met en pause le programe
#print("Après le sleep.")

class Afficheur(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()#♣Print the letters as they arrives
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1
            
# Création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

print('\n')

class Afficheur2(Thread):
    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 3:
            for lettre in self.mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
            i += 1


# Création des threads
thread_1 = Afficheur2("canard")
thread_2 = Afficheur2("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

print('\n')

verrou = RLock()

class Afficheur3(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 3:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur3("canard")
thread_2 = Afficheur3("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()