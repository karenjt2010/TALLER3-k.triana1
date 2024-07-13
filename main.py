from modelos.animal import Animal
from modelos.ianimal import iAnimal
from modelos.animal_exotico import Animal_Exotico
from modelos.huron import Huron
from modelos.boa_constrictor import Boa_Constrictor

#Crear Huron
huron_1 = Huron("Manolo", 20.5, 3,"Nueva Zelanda", 150.30)
huron_2 = Huron("Federica", 12.5, 1,"Perú", 80.3)
huron_3 = Huron("Pedro", 18.7, 6,"Colombia", 100.15)

# Crear Boa
boa_1 = Boa_Constrictor("Estela", 140.5, 2,"Brasil", 150.30, 7)
boa_2 = Boa_Constrictor("Ludovico", 85.6, 1,"Ecuador", 95.8, 2)
boa_3 = Boa_Constrictor("pachita", 210.20, 5,"Colombia", 201.4, 20)

print(Huron.hacer_sonido(huron_1))
print(Huron.calcular_flete(huron_3))
print(Boa_Constrictor.calcular_flete(boa_1))
print(Boa_Constrictor.hacer_sonido(boa_2))
print(Boa_Constrictor.contar_ratones(boa_1))
Boa_Constrictor.contar_ratones(boa_3)
print(Boa_Constrictor.contar_ratones(boa_3))
print(Boa_Constrictor.obtener_nombre(boa_1))
