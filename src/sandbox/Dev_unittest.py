# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:02:51 2016

@author: sylhare
"""
import random
import unittest

class RandomTest(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10)) #Créer un attribut d'instance pour être réutilisé par les fonctions
    
    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste) #Prends un élèment au hasard de la liste
        self.assertIn(elt, self.liste)  # Vérifie que 'elt' est dans 'liste'
        
#    def test_choice_failed(self): #Testing this function will give an "F" for failed
#        """Test le fonctionnement de la fonction 'random.choice'."""
#        elt = random.choice(self.liste)
#        self.assertIn(elt, ('a', 'b', 'c'))    

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10))) #Check if the two elements are equal

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)
            
    def test_sample_error(self):
        #self.assertRaises(ValueError, random.sample, self.liste, 20) #Same as below
        with self.assertRaises(ValueError): #Verify that this error is raised for that result
            random.sample(self.liste, 20) #Fail for something <= 10

        
unittest.main() #Pour lancer le test "." si validé, "F" si pas bonne valeur obtenue, "E" si obtenue une erreur. Plus récapitulatif du nombre de tests
#python.exe -m unittest #To run the tests