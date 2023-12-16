class Agent:
    def __init__(self, name):
        self.name = name
        self.state = {1: "+", 2: "-"}
        self.memoria = []
    
    
    # Get State. Es la capacidad de observar no solo a otros agentes, sino de recrusos y "orografía"/"Gestalt" del mapa
    # Out-fáctico. Esto incluye comunicación como mensaje a otros agentes, o acciones como tomar un recurso o poseer cierto lugar en el mapa
    # In-fáctico. Los otros objetos no entregan inputs fácticos al self, solo otros agentes.

# Clase que crea objetos distintos a los agentes, esto incluye por ejemplo: recursos, mapa (estoy pensando que el mapa será una red aleatoria en 
# forma de matriz en donde ciertos nodos representen la posición actual de cada agente, así mismo cada nodo tiene la capacidad de tener o no recursos,
# o ser habitable o no, o tener costo de habitaibilidad o un costo continuo por ser poseida u ocupada...), un reloj o tick en el juego, porque si se juega 
# por una persona esta le permita jugar por turnos, y a agentes como modelos de IA iterar

# Clase que crea el ejecutable, configuracion y control
# Un menú inicial que nos permita cargar las configuraciones (parámetros necesarios en def anteriores) deseadas para el ejecutable