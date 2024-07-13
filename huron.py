from modelos.animal_exotico import Animal_Exotico
from abc import ABC, abstractmethod 

class Huron(Animal_Exotico,ABC):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    def hacer_sonido(self):
        return "¡Eek Eek!"
    
    def calcular_flete(self):
        return f"El costo de importar el animal {self._nombre} es de $ {round((self._peso*self._impuestos),2)}"
    

    