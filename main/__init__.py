# main/__init__.py
from .game import main_menu, Game
from .agent import Agent
from .environment import Environment

def initialize_game():
    """
    Inicializa y configura los componentes necesarios para el juego.
    """
    environment = Environment(...)  # Configurar según sea necesario
    agents = [Agent("Agent1", is_ai=False), Agent("Agent2", is_ai=True, ai_model_path="path/to/model")]
    
    return Game(agents, environment)

if __name__ == "__main__":
    game = initialize_game()
    main_menu(game)  # Asumiendo que main_menu puede aceptar un objeto Game si es necesario
