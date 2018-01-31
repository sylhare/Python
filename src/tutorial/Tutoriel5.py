# -*- coding: utf-8 -*-

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris"  # '_' Convention pour non accessible depuis l'extérieur de la classe

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à
        l'attribut 'lieu_residence'"""

        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
            self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence,
                              _set_lieu_residence)  # + del objet.lieu_residence, help(objet.lieu_residence))


bernard = Personne("Micado", "Bernard")
bernard.nom
bernard.age
jean = Personne("Micado", "Jean")
jean.lieu_residence
jean.lieu_residence = "Berlin"


class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
            cls.objets_crees))

    combien = classmethod(combien)


Compteur.objets_crees
a = Compteur()  # On crée un premier objet
Compteur.objets_crees
b = Compteur()
Compteur.objets_crees


class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""

        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""


tab = TableauNoir()
tab.surface
tab.ecrire("Coooool ! Ce sont les vacances !")
tab.surface


# Methode Statique
class MStatic:
    """Une classe de test tout simplement"""

    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")

    afficher = staticmethod(afficher)


class Test:
    """Une classe de test tout simplement"""

    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"

    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))


test = Test()
test.afficher_attribut()
dir(test)  # Affiche le nom de tous les attributs et méthodes


class ZDict:
    """Classe enveloppe d'un dictionnaire"""

    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""

        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""

        self._dictionnaire[index] = valeur
