from modelos.animal_exotico import Animal_Exotico 
from abc import ABC, abstractmethod 

class Boa_Constrictor(Animal_Exotico, ABC):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float, ratones_comidos: int) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = ratones_comidos
        self.data = []
        
    def obtener_ratones_comidos(self):
        return self._ratones_comidos

    def hacer_sonido(self):
        return "¡Tsss!"
    
    def calcular_flete(self):
        return f"El costo de importar el animal {self._nombre} es de $ {round((self._peso*self._impuestos),2)}"
    
    def contar_ratones(self):
        self._ratones_comidos = self._ratones_comidos + 1
        return self._ratones_comidos
    
    def comer_ratones(self):
        if self._ratones_comidos >= 10:
            return "La boa está llena"
        self._ratones_comidos += 1
        return self._ratones_comidos
    