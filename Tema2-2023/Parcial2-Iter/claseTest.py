import unittest
from claseDepartamento import Departamento
class TestImporte(unittest.TestCase):
    __depto: object
    #__casa: object
    
    def setUp(self):
        self.__depto= Departamento("9 de Julio", "san martin 120 oeste",250, 5, 7, 9, 8)
    
    def test_importeVenta(self):
        importe = self.__depto.getImporte()
        self.assertEqual (importe, 318750000)
if __name__ == "__main__":
    unittest.main()