# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:42:54 2016

@author: sylvain.hareng1
"""

# from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
# from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

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

# ==============================================================================
# ax.plot_surface(X, Y, Z, rstride=20, cstride=4, alpha=0.1)
# cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
# ax.set_xlabel('X')
# ax.set_xlim(-40, 40)
# ax.set_ylabel('Y')
# ax.set_ylim(-40, 40)
# ax.set_zlabel('Z')
# ax.set_zlim(-10, 10)
# ==============================================================================

plt.show()
