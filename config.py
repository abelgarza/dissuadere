# config.py
import random

class RNJesus:
    @staticmethod
    def rng_scale() -> float:
        return random.random()
    
    @staticmethod
    def rng_randint(a: int, b: int) -> int:
        return random.randint(a, b)