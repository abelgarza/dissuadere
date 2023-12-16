import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main.game import Game
from main.environment import Environment
from main.agent import Agent
from main.visualization import MapVisualizer3D

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Dissuadere Game")

        # UI Elements
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

        # Matplotlib Figure para la visualización
        self.visualizer = MapVisualizer3D()
        self.canvas = FigureCanvasTkAgg(self.visualizer.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=1)

        # Instancia del Juego
        self.game = None

    def start_game(self):
        num_nodes = 25  # Valor que podría obtenerse de la UI
        environment = Environment(num_nodes)
        agents = [Agent("Agent1"), Agent("Agent2")]  # Configuración de agentes
        self.game = Game(agents, environment)
        self.visualizer.set_environment(environment)

        # Iniciar simulación y actualizar visualización
        self.update_visualization()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()