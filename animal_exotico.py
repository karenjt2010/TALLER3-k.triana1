from modelos.animal import Animal
from abc import ABC, abstractmethod

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen:str, impuestos:float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def obtener_pais_origen(self):
        return self._pais_origen
    
    def obtener_impuestos(self):
        return self._impuestos
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def calcular_flete(self):
        pass

    def comer(self):
        pass

    def obtener_kilos_comidos(self):
        pass
    
  
