from modelos.boa_constrictor import Boa_Constrictor
from modelos.huron import Huron
from abc import ABC, abstractmethod 

boa1 = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 5 )
boa2 = Boa_Constrictor("Josefa", 200, 15, "Brasil",190000, 8 )
huron1 = Huron("Pedro", 15, 6, "Colombia",150000)
huron2 = Huron("Juan", 10, 3, "Peru",120000)
lista_animales = [boa1, boa2, huron1, huron2]

class Guarderia(Boa_Constrictor, Huron, ABC):
    def alimentar_boa(boa:Boa_Constrictor):
        if boa in lista_animales:
            return Boa_Constrictor.comer_ratones(boa)
        raise ValueError ("Esta Boa no existe!")