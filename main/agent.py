# main\agent.py


from main import enviroment

class Agent:
    def __init__(self, name):
        self.name = name
        self.state = {1: "+", 2: "-"}  # Posibles estados del agente
        self.memoria = []  # Historial de acciones o interacciones

    def observe(self, environment):
        # Observar y procesar información del entorno
        pass

    def act(self):
        # Realizar acciones en el entorno
        pass

    def communicate(self, other_agent, message):
        # Comunicarse con otro agente
        other_agent.receive_message(message)

    def receive_message(self, message):
        # Recibir un mensaje de otro agente
        self.memoria.append(message)