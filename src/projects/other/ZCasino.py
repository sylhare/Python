# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:54:50 2015

ZCasino

@Site: https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-tous-au-zcasino
"""

import math
import os
import random
from math import ceil
from random import randrange

print("Casino Simulation")
print("Do casino() for my fonction and correction() for the intended one ...")


# Select the number you want to gamble on
def gambling():
    """

    :return:
    """
    number = input("Which number you want to be on ? (0 to 49) ")

    try:
        number = float(number)
    except ValueError:
        print("Error: need a Number")
    else:
        if (49 >= number) and (number >= 0):
            return number
        else:
            gambling()


# The actual process of betting, gambling and winning/losing
def betting(mise):
    """

    :param mise:
    :return:
    """
    bet = input("How much do you want to bet ? ")
    try:
        bet = float(bet)
    except ValueError:
        print("Error: need a number")
    else:
        if mise < bet:
            print("You only have {}$, bet less ...".format(mise))
            betting(mise)
        else:
            mise = mise - bet
            number = gambling()
            mise += winnings(bet, result(number))
            print("You have now {}$ in your pocket".format(mise))
            return mise


def roulette():
    """

    :return:
    """
    return random.randrange(50)


# Result of your bet based on the roulette
def result(number):
    """

    :param number:
    :return:
    """
    win = roulette()
    if number == win:
        print("{} ! - You have the good number !!".format(win))
        return 1
    elif number % 2 == win % 2:
        print("{} ! - Same parity !".format(win))
        return 0
    else:
        print("{} ! - You lose sorry...".format(win))
        return -1


# Calulating your winnings
def winnings(bet, result):
    """

    :param bet:
    :param result:
    :return:
    """
    if result < 0:
        return 0
    elif result == 0:
        return math.floor(bet / 2)
    else:
        return bet * 3


def init():
    """

    :return:
    """
    mise = input("How much money do you have ? ")

    try:
        mise = float(mise)
    except ValueError:
        print("Error: need a Number")
    else:
        mise = round(mise, 2)  # Arrondi à deux chiffres après la virgule
        return mise


# Casino  won't stop until you have money
def casino():
    """ main casino """
    print("======      Roulette !     ======")
    mise = float(init())

    while mise > 0:
        mise = float(betting(mise))
        print("\n")


# -------------------- CORRECTION ------------------------ #

# Ce fichier abrite le code du ZCasino, un jeu de roulette adapté


def correction():
    """ corrected Casino """
    # Déclaration des variables de départ
    argent = 1000  # On a 1000 $ au début du jeu
    continuer_partie = True  # Booléen qui est vrai tant qu'on doit
    # continuer la partie

    print("Vous vous installez à la table de roulette avec", argent, "$.")

    while continuer_partie:  # Tant qu'on doit continuer la partie
        # on demande à l'utilisateur de saisir le nombre sur
        # lequel il va miser
        nombre_mise = -1
        while nombre_mise < 0 or nombre_mise > 49:
            nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
            # On convertit le nombre misé
            try:
                nombre_mise = int(nombre_mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                nombre_mise = -1
                continue
            if nombre_mise < 0:
                print("Ce nombre est négatif")
            if nombre_mise > 49:
                print("Ce nombre est supérieur à 49")

        # À présent, on sélectionne la somme à miser sur le nombre
        mise = 0
        while mise <= 0 or mise > argent:
            mise = input("Tapez le montant de votre mise : ")
            # On convertit la mise
            try:
                mise = int(mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                mise = -1
                continue
            if mise <= 0:
                print("La mise saisie est négative ou nulle.")
            if mise > argent:
                print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

        # Le nombre misé et la mise ont été sélectionnés par
        # l'utilisateur, on fait tourner la roulette
        numero_gagnant = randrange(50)
        print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

        # On établit le gain du joueur
        if numero_gagnant == nombre_mise:
            print("Félicitations ! Vous obtenez", mise * 3, "$ !")
            argent += mise * 3
        elif numero_gagnant % 2 == nombre_mise % 2:  # ils sont de la même couleur
            mise = ceil(mise * 0.5)
            print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
            argent += mise
        else:
            print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            argent -= mise

        # On interrompt la partie si le joueur est ruiné
        if argent <= 0:
            print("Vous êtes ruiné ! C'est la fin de la partie.")
            continuer_partie = False
        else:
            # On affiche l'argent du joueur
            print("Vous avez à présent", argent, "$")
            quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
            if quitter == "o" or quitter == "O":
                print("Vous quittez le casino avec vos gains.")
                continuer_partie = False

    # On met en pause le système (Windows)
    os.system("pause")
