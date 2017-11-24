# -*- coding: utf-8 -*-
"""

https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-proprietes-9

"""

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    #Le double underscore : __ permet de définir les méthodes spéciales (héritées d'objet)
    def __init__(self, name, firstName):
        """Constructeur de notre classe"""
        self.name = name
        self.firstName = firstName
        self.age = 33
        self._lieu_residence = "Paris" # La convention veut qu'on n'accède pas, depuis l'extérieur de la classe, à un attribut commençant par un souligné _
        
    def _get_lieu_residence(self): # On n'accède pas, depuis l'extérieur de la classe, à une méthode commençant par un souligné _
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut 'lieu_residence'"""
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
        
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.firstName, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
        
    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété (get en premier, set en deuxième)
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence) # Une propriété peut être utilisé plus naturellement en dehors de la classe
    #nom_propriete = propriete(methode_accesseur, methode_mutateur, methode_suppression, methode_aide)    
   
    def __del__(self): #Permet de modifier le comportement de Python lorsqu'un élèment est supprimé
        """Méthode appelée quand l'objet est supprimé"""
        print("-----> C'est la fin ! Objet me supprime !")
        
    def __repr__(self): #Ne prend aue self en paramètre pour afficher l'objet
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.name, self.firstName, self.age)  
                
    def __str__(self): #Même but que __repr__ mais pour un print
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.firstName, self.name, self.age)
   
Simon = Personne("Clarkson", "Simon")  #Puisque property, pas besoin de get et set pour assigner les valeurs
Simon.name
Simon.firstName
Simon.age
Simon #Affiche par la fonction __repr__
print(Simon) #Affiche par la fonction __str__
chaine = str(Simon)
chaine #Affiche grâce à la fonction __str__

class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
     Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""
     
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
        
    def save(self):
        print('saved')
        
    def __getattr__(self, attributeName):
        """Si Python ne trouve pas l'attribut nommé attributeName, il appelle cette méthode. On affiche une alerte"""         
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(attributeName))
        #print(self.c) #renvoie self.c pour tout attribut
         
    def __setattr__(self, nom_attr, val_attr): #Permet d'ajouter une valeur aux auttributs.
        """Méthode appelée quand on fait objet.nom_attr = val_attr. On se charge d'enregistrer l'objet"""
        object.__setattr__(self, nom_attr, val_attr)
        self.save()
        
    def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")


pro=Protege()
pro.b
pro.e #Pas d'attribut e défini donc __getattr__
object.__delattr__(pro,'a') #Supprime l'attribut a, avec del on a une erreur

class MaClasse():
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.val = 1
        self.nom="Ma Classe"
    
objet = MaClasse() # On crée une instance de notre classe
getattr(objet, "nom") # Semblable à objet.nom
setattr(objet, "nom", "Mon nouveau nom de classe") # = objet.nom = val ou objet.__setattr__("nom", val)
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon
   

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
        
    def __delitem__(self, index): 
        """Delete the element at dictionnaire[inedx]"""
        del self._dictionnaire[index]
        
        
ma_liste = [1, 2, 3, 4, 5]
8 in ma_liste #Renvoie TRUE si 8 dans la liste sinon FALSE
ma_liste.__contains__(8) #Equivalent d'au dessus
ma_liste.__len__() #Donne la longueur de la liste


class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec) #Pour l'avoir au format MM:SS
        
    def __add__(self, entier):
        """L'objet à ajouter est un ENTIER, le nombre de secondes"""

        nouvelle_duree = Duree() # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec # On ajoute la durée
        nouvelle_duree.sec += entier

        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60 #Division euclydienne
            nouvelle_duree.sec = nouvelle_duree.sec % 60 #Modulo = reste de la division euclydienne
        return nouvelle_duree  # On renvoie la nouvelle durée  
    
    def __radd__(self, entier): #Permet de définir un entier + l'objet durree (Add fait l'opération duree + entier)
        return self + entier    
        
    def __iadd__(self, objet_a_ajouter): #Surcharge l'opération objet += entier
        """L'objet à ajouter est un entier, le nombre de secondes"""

        self.sec += objet_a_ajouter
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        return self    
        
    def __sub__(self, entier): #Surcharge de l'opérateur - (soustraction)
        self.sec -= entier  
        return self
   
    def __mul__(self, entier): #Surcharge de l'opérateur * (multiplication)
        self.sec *= entier  
        return self
        
    def __truediv__(self, entier): #Surcharge de l'opérateur / (division)
        self.sec = self.sec/entier 
        return self
        
    def __floordiv__(self, entier):  #Surcharge de l'opérateur // (division entière) 
        return (self.sec // entier)  
        
    def __mod__(self, entier):  #Surcharge de l'opérateur % (modulo)
        return (self.sec % entier) 

    def __pow__(self, entier):  #Surcharge de l'opérateur ** (puissance)
        return (self.sec ** entier)           
    
    #Les Methodes de Comparaison
    def __eq__(self, autre_duree): #Opérateur d'égalité (equal). Renvoie True si self et objet_a_comparer sont égaux, False sinon.
        """Test si self et autre_duree sont égales"""

        return self.sec == autre_duree.sec and self.min == autre_duree.min

    def __gt__(self, autre_duree): #Teste si self est strictement supérieur (greather than) à objet_a_comparer.
        """Test si self > autre_duree"""  # On calcule le nombre de secondes de self et autre_duree

        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2
        
    #Methode ne fonctionneront pas, ol faudrait scinder seconde et minute par modulo 60 du nombres pour aue ça marche    
    def __ne__(self, objet_a_comparer):
        #Différent de (non equal). Renvoie True si self et objet_a_comparer sont différents, False sinon.
        return self != objet_a_comparer
        
    def __ge__(self, objet_a_comparer):
        #Teste si self est supérieur ou égal (greater or equal) à objet_a_comparer.
        return self >= objet_a_comparer
        
    def __lt__(self, objet_a_comparer):
        #Teste si self est strictement inférieur (lower than) à objet_a_comparer.
        return self < objet_a_comparer       
        
    def __le__(self, objet_a_comparer):    
        #Teste si self est inférieur ou égal (lower or equal) à objet_a_comparer.
        return self <= objet_a_comparer
        
d1 = Duree(3, 5)
print(d1)
d1+=128

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5
   
    def __getstate__(self): #Appeler au moment de serialiser l'objet - recupère l'attribut spéciale __dict__
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr
    
    def __setstate__(self, dict_attr): #Modification du dictionnaire d'attribut après la serialisation, peut renvoyer autre chose que le dictionnaire
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr