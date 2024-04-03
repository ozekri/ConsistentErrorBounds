import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définir les paramètres du cône exponentiel
r_max = 1  # Rayon maximal du cône
h_max = 1  # Hauteur maximale du cône
theta_max = np.pi / 2  # Angle maximal

# Générer des données pour le cône exponentiel
theta = np.linspace(0, theta_max, 100)
r = r_max * np.exp(theta)
h = h_max * theta / theta_max

# Convertir en coordonnées cartésiennes
x = r * np.cos(theta)
y = r * np.sin(theta)
z = h

# Créer une grille pour la surface
theta_grid, h_grid = np.meshgrid(theta, h)
x_surface = r_max * np.exp(theta_grid) * np.cos(theta_grid)
y_surface = r_max * np.exp(theta_grid) * np.sin(theta_grid)
z_surface = h_grid

# Plot de la surface du cône exponentiel
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_surface, y_surface, z_surface, cmap='viridis')

# Paramètres esthétiques
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Surface du Cône Exponentiel')

ax.set_xlim(-2,2)

plt.show()
