from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre:str, peso:float, edad:int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def calcular_flete(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_peso(self):
        return self._peso
    
    def obtener_edad(self):
        return self._edad