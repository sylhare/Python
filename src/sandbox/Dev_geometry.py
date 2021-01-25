# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:17:36 2016

@author: sylhare
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

x1 = np.arange(-5, 5, 1)
y1 = np.arange(-5, 5, 0.5)


def disc(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return (1 + x) ** 2 + (1 + y) ** 2


def cone(x, y, z):
    """

    :param x:
    :param y:
    :param z:
    :return:
    """
    return np.sqrt((1 + x) ** 2 + (1 + y) ** 2)


x, y = np.mgrid[-20:20:10j, -20:20:10j]
z = disc(x, y)
plt.figure(1)
plt.subplot(211)
plt.contour(x, y, z, colors='k')
plt.show()

# --------------------------------------

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-30, 30, 0.1)
Y = np.arange(-30, 30, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.log(X ** 2 + Y ** 2)

# 3D plot; coolwarm for the color
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(0, 6)

# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
