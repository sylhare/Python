# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:40:46 2017
"""


def func(arg):
    """

    :param arg:
    """
    if not isinstance(arg, (list, tuple)):
        arg = [arg]
    print(arg)


func('abc')
func(['abc', '123'])
