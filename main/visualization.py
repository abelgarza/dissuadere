import matplotlib.pyplot as plt
import networkx as nx

class MapVisualizer3D:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def set_environment(self, environment):
        self.environment = environment

    def update(self, game):
        self.ax.clear()
        G = self.environment.map  # El grafo de la red

        # Dibujar los nodos y las aristas del grafo
        pos = nx.spring_layout(G)  # Puedes cambiar a otro layout si lo prefieres
        nx.draw_networkx_nodes(G, pos, ax=self.ax, node_color='lightblue', edgecolors='black')
        nx.draw_networkx_edges(G, pos, ax=self.ax, edge_color='gray')

        # Dibujar los agentes en sus respectivas posiciones
        for agent in game.agents:
            if agent.position in pos:
                nx.draw_networkx_nodes(G, pos, ax=self.ax, nodelist=[agent.position], node_color='red')

        self.ax.set_title("Estado Actual del Juego")
        plt.show()