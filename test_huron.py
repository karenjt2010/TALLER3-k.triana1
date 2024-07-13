import unittest
from modelos.huron import Huron

class Test_Huron(unittest.TestCase):
    def test_init(self):
        huron1 = Huron("Pedro", 15, 6, "Colombia",150000)
        self.assertEqual(huron1.obtener_impuestos(), 150000)
        
    def test_hacer_sonido(self):
        huron1 = Huron("Pedro", 15, 6, "Colombia",150000)
        self.assertEqual(huron1.hacer_sonido(), "¡Eek Eek!")
     
    def test_calcular_flete(self):
        huron1 = Huron("Pedro", 15, 6, "Colombia",150000)
        self.assertEqual(huron1.calcular_flete(), "El costo de importar el animal Pedro es de $ 2250000")   

