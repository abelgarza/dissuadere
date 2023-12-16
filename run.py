# run.py

# Crear dos agentes, A y B
A = Agente("A")
B = Agente("B")

# Ejemplo de comunicación entre A y B
A.enviar_mensaje(B, "Mensaje de A a B")
B.enviar_mensaje(A, "Respuesta de B a A")

# Mostrar mensajes recibidos por A y B
print("Mensajes recibidos por A:", A.mensajes_recibidos)
print("Mensajes recibidos por B:", B.mensajes_recibidos)