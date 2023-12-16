# main/visualization.py

from .environment import Environment

import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class MapVisualizer3D:
    def __init__(self, environment):
        self.environment = environment

    def render(self):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Colocación de los nodos
        for node, data in self.environment.map.nodes(data=True):
            x, y, z = self._calculate_node_position(node)
            ax.scatter(x, y, z, color='b', s=100)  # Puedes cambiar el tamaño y color

        # Dibujar aristas
        for edge in self.environment.map.edges():
            start_pos = self._calculate_node_position(edge[0])
            end_pos = self._calculate_node_position(edge[1])
            ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], [start_pos[2], end_pos[2]], color='gray')

        plt.show()

    def _calculate_node_position(self, node_id):
        num_nodes = self.environment.num_nodes
        # Distribución uniforme de ángulos y alturas
        phi = np.arccos(1 - 2 * (node_id + 0.5) / num_nodes)  # Ángulo polar
        theta = np.pi * (1 + 5**0.5) * (node_id + 0.5)  # Ángulo azimutal

        x = np.cos(theta) * np.sin(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(phi)

        # Escalar para ajustar el tamaño de la esfera
        scale = 10
        return (scale * x, scale * y, scale * z)

# Resto del código...
