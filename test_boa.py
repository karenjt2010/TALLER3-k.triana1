import unittest
from modelos.boa_constrictor import Boa_Constrictor

class Test_Boa(unittest.TestCase):
    def test_init(self):
        boa = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 5 )
        self.assertEqual(boa.obtener_impuestos(), 150000)
        self.assertEqual(boa.obtener_ratones_comidos(), 5)
        
    def test_hacer_sonido(self):
        boa = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 5 )
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")
     
    def test_calcular_flete(self):
        boa = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 5 )
        self.assertEqual(boa.calcular_flete(), "El costo de importar el animal Ramona es de $ 15000000")   

    def test_contar_ratones(self):
        boa = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 5 )
        self.assertEqual(boa.contar_ratones(), 6)
        
    def test_modificar_ratones(self):
        boa = Boa_Constrictor("Ramona", 100, 8, "Colombia",150000, 10)
        self.assertEqual(boa.comer_ratones(),"La boa está llena")
        