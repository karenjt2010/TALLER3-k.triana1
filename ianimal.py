from abc import ABC, abstractmethod

class iAnimal(ABC):
   
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
    