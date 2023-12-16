# main/environment.py
from .config import RNJesus
import networkx as nx
import matplotlib.pyplot as plt


class Environment:
    """
    Clase para representar el entorno del juego, incluyendo la generación y manejo del mapa.
    """

    def __init__(self, num_nodes: int):
        """
        Inicializa un entorno con un número especificado de nodos.

        Args:
            num_nodes (int): Número de nodos en el mapa.
        """
        self.num_nodes = num_nodes
        self.map = self.generate_map()

    def generate_map(self) -> nx.Graph:
        """
        Genera un mapa como un grafo con nodos y aristas.

        Returns:
            nx.Graph: Un grafo que representa el mapa del juego.
        """
        G = nx.Graph()
        for i in range(self.num_nodes):
            G.add_node(i, resources=self.assign_resources())

        self.create_edges(G)
        return G

    def assign_resources(self) -> dict:
        """
        Asigna recursos aleatorios a un nodo.

        Returns:
            dict: Un diccionario de recursos asignados al nodo.
        """
        
        return {
            "cost": RNJesus.rng_scale(),
            "income": RNJesus.rng_scale(),
            "damage": RNJesus.rng_scale(),
            "science": RNJesus.rng_scale()
        }

    def create_edges(self, G: nx.Graph) -> None:
        """
        Crea aristas entre nodos en el grafo basado en una probabilidad.

        Args:
            G (nx.Graph): El grafo donde se añadirán las aristas.
        """
        for a in range(self.num_nodes):
            for b in range(a + 1, self.num_nodes):
                if RNJesus.rng_scale() <= 0.3:  # Probabilidad de crear una arista
                    G.add_edge(a, b)

    def map_state(self) -> str:
        """
        Retorna el estado actual del mapa para observación.

        Returns:
            str: Una representación en cadena del estado del mapa.
        """
        return nx.info(self.map)

    def update(self) -> None:
        """
        Actualiza el estado del mapa. Aquí se puede añadir lógica para cambios dinámicos en el mapa.
        """
        pass