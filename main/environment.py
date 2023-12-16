# main\environment.py
import networkx as nx
from config import RNJesus

class Environment:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.map = self.generate_map()

    def generate_map(self):
        G = nx.Graph()
        for i in range(self.num_nodes):
            G.add_node(i, resources=self.assign_resources())

        # Asegurando que la red sea conexa
        for a in range(self.num_nodes):
            for b in range(a + 1, self.num_nodes):
                if RNJesus.rng_scale() < 0.5:  # Probabilidad de crear una arista
                    G.add_edge(a, b)

        return G

    def assign_resources(self):
        return {
            "cost": RNJesus.rng_scale(),
            "food": RNJesus.rng_scale(),
            "science": RNJesus.rng_scale(),
            "toxic": RNJesus.rng_scale()
        }


    def map_state(self):
        # Retorna el estado actual del mapa para observación
        return nx.info(self.map)

    def update(self):
        # Aquí puedes añadir lógica para actualizar el mapa en cada tick
        pass