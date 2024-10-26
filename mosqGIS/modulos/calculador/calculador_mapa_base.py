"""
Este módulo contiene la clase `CalculadorMapaBase`, que sirve como una clase base abstracta para
calcular mapas.

Clases:
    CalculadorMapaBase: Una clase base abstracta para gestionar el cálculo de mapas.
"""

from abc import ABC, abstractmethod

class CalculadorMapaBase(ABC):
    def __init__(self, carpeta_recortadas):
        """
        Inicializa la clase CalculadorMapaBase.

        Args:
            carpeta_recortadas (str): Ruta a la carpeta que contiene las imágenes recortadas.
        """
        self.carpeta_recortadas = carpeta_recortadas

    @abstractmethod
    def calcular_mapa(self):
        """
        Metodo abstracto para calcular el mapa. Las subclases deben implementar este metodo.

        Raises:
            NotImplementedError: Si el metodo no es implementado por una subclase.
        """
        pass
    