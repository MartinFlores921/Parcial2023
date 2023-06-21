import unittest
from claseInmueble import Inmueble
from claseDepartamento import Departamento
from claseCasa import Casa
class TestImporte(unittest.TestCase):
    __inmueble: object
    def setUp(self):
        self.__inmueble= Departamento("9 de Julio", "san martin 120 oeste",250, 5, 7, 9, 8)
    def test_ImporteVenta(self):
        imp = self.__inmueble.getImporte()
        self.assertEqual(imp, 31.35)
if __name__ == "__main__":
        unittest.main()
        
                      