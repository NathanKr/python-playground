# from mpl_toolkits.mplot3d import Axes3D i do not see that it is needed
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure() # return matplotlib.figure.Figure instance
ax = fig.gca(projection='3d') #Get current axes, creating one if necessary.

# Make data.
X = np.arange(-5, 5, 0.25) # shape (40,0)
Y = np.arange(-5, 5, 0.25) # shape (40,0)
X, Y = np.meshgrid(X, Y) # following the mesh X.shape is (40,40) and Y.shape is (40,40)
R = np.sqrt(X**2 + Y**2) # R.shape is 40,40
Z = np.sin(R) # R.shape is 40,40

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()