# main\agent.py

class Agent:
    def __init__(self, model: str, health: float, balance: float):
        self.model = model
        self.incentive_score = 0
        self.health = health
        self.balance = balance
        self.current_state = {} # o algo para dar un resumen de esos dos parámetros por tick
        self.position = None
        
    def take_action(self, environment):
        # Aquí va la lógica de acción del agente
        # Por ejemplo, moverse a un nodo adyacente o interactuar con el entorno
        pass

    def observe_environment(self):
        # Logic to observe and update current state
        pass

    def communicate(self, other_agents):
        # Communication logic and update communication log
        pass

    def decide_action(self):
        # Use AI model or other logic to decide action
        pass

    def perform_action(self, action):
        # Perform the decided action
        pass

    def update_incentive_score(self):
        # Update incentive score based on current state and actions
        pass
