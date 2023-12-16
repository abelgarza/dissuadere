import pygame
from .environment import Environment
from .agent import Agent

class Game:
    """
    Clase principal para gestionar la lógica del juego.
    """

    def __init__(self, agents: list, environment: Environment):
        """
        Inicializa el juego con agentes y un entorno.
        """
        self.agents = agents
        self.environment = environment
        self.is_running = True

    def run_turn(self):
        """
        Ejecuta las acciones de cada agente en un turno.
        """
        for agent in self.agents:
            agent.take_action(self.environment)

    def run_game(self):
        """
        Ejecuta el ciclo principal del juego.
        """
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.run_turn()
            pygame.display.flip()

def main_menu(game: Game):
    """
    Código para mostrar el menú principal y recoger las configuraciones del usuario.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Dissuadere Game')

    # Configuración inicial del juego
    # Aquí se puede añadir lógica para configurar el juego

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Aquí se puede añadir lógica para mostrar opciones del menú
            # y configurar el juego antes de empezar

        pygame.display.flip()

    pygame.quit()

    # Iniciar el ciclo principal del juego
    game.run_game()

if __name__ == "__main__":
    environment = Environment(...)  # Configura el entorno
    agents = [Agent("Agent1", is_ai=False), Agent("Agent2", is_ai=True, ai_model_path="path/to/model")]  # Crea agentes
    game = Game(agents, environment)
    main_menu(game)