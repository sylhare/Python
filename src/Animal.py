# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:44:17 2017


@author: sylhare

"""
class Test:
    """
    Here is a custom test class with default methods that can be implemented
    It is based on the link upper in the description

    """

    ## Basics ##
    def __init__(self, name, color):
        """
        It is called if we create a class like x = Test()
        to initialize an instance

        """
        self.example = "this is an example"

    def __str__(self):
        """
        Called by str(x)
        Aso called for print(x) with x as the class
        the “informal” value as a string, also call with print(x)

        """

    def __repr__(self):
        """
        Called by repr(x)
        the “official” representation as a string

        """

    def __bytes__(self):
        """
        called by bytes(x)
        the “informal” value as a byte array

        """

    ## Computed Attributes ##

    def __getattributes__(self, prop):
        """
        called with x.example
        See difference on link on the top
        to get a computed attribute (unconditionally)

        """


    def __getattr__(self, prop):
        """
        called with x.example
        See difference on link on the top
        to get a computed attribute (fallback)

        """

    def __setattr__(self, prop, value):
        """
        x.example = value
        To set an attribute

        """

    def __delattr__(self, prop):
        """
        del x.example
        To delete an attribute

        """

    def __dir__(self):
        """
        dir(x)
        To list all attributes and methods

        """

    ## Classes That Act Like Functions
    def __my_instance__(self):
        """
        my_instance(x)
        to “call” an instance like a function

        """

    def __len__(self):
        """
        if class is a container for a set of value s
        len(s)
        the number of items

        """

    def __containes__(self):
        """
        With s as a container for a set of values
        element in s

        """

    ## Classes That Act Like Iterators

    ## Classes That Act Like Sets

    ## Classes That Act Like Dictionaries

    ## Classes That Act Like Numbers

    ## Classes That Can Be Compared

    ## Classes That Can Be Serialized

    ## Classes That Can Be Used in a with Block



### Example ###
class Animal:
    """
    Test class to create an animal class in python

    """
    def __init__(self, name, color):
        """
        to initialize the Animal Class

        """
        self.__name__ = name
        self.__color__ = color

    def __str__(self):
        """
        Return a string with the animal characteristics

        """
        return "{0} of color {1}".format(self.__name__, self.__color__)

    def __getattr__(self, key):
        if key == 'name':
            return self.__name__

        if key == 'color':
            return self.__color__

class Magic:
    """
    Magical test class
    """
    def __init__(self, magic):
        """
        to initialize the magic Class

        """
        self.__magic__ = magic    
    
    @staticmethod # Means that it doesn't use any attributes of the class
    def magic_word(word):
        print("abracada " + word)


class Cat(Animal):
    """
    SubClass of Animal
    Inheriting its method
    Used to implement Cat's methods

    """
    def __init__(self, name, color):
        super().__init__(self, name, color)

    @staticmethod
    def purr():
        print("Purr...")

class Dog(Animal):
    """
    Used to implement Dog's methods

    """
    @staticmethod
    def bark():
        print("Woof!")

class Bird(Animal, Magic):
    """
    Used to implement Bird's methods inheriting Animal and Magic methods

    """
    @staticmethod
    def tweet():
        print("piiip")


# Custom Class tests
thunder = Bird("Thunder", "yellow")
thunder.magic_word('... bra!')

animal = Animal("zet", "brown")
print (str(animal))

dog = Dog("Ford", "brown")
print(dog.name)
dog.bark()


# Built-In Class Attributes
"""
__dict__: Dictionary containing the class's namespace.

__doc__: Class documentation string or none, if undefined.

__name__: Class name.

__module__: Module name in which the class is defined. This attribute is
"__main__" in interactive mode.

__bases__: A possibly empty tuple containing the base classes,
in the order of their occurrence in the base class list.

"""
print ("Animal.__doc__:", str(Animal.__doc__))
print ("Animal.__name__:", Animal.__name__)
print ("Animal.__module__:", str(Animal.__module__))
print ("Animal.__bases__:", str(Animal.__bases__))
print ("Animal.__dict__:", str(Animal.__dict__))
