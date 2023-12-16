# config.py
import random

class RNJesus:
    """
    Clase para generar números aleatorios.
    Proporciona métodos estáticos para diferentes tipos de generación de números aleatorios.
    """

    @staticmethod
    def rng_scale() -> float:
        """
        Genera un número flotante aleatorio entre 0 y 1.

        Returns:
            float: Número aleatorio generado.
        """
        return random.random()
    
    @staticmethod
    def rng_randint(a: int, b: int) -> int:
        """
        Genera un número entero aleatorio entre a y b.

        Args:
            a (int): Límite inferior del rango (inclusive).
            b (int): Límite superior del rango (inclusive).

        Returns:
            int: Número entero aleatorio generado.
        """
        return random.randint(a, b)

    @staticmethod
    def set_seed(seed: int) -> None:
        """
        Establece una semilla para la generación de números aleatorios.

        Args:
            seed (int): La semilla para el generador de números aleatorios.
        """
        random.seed(seed)
