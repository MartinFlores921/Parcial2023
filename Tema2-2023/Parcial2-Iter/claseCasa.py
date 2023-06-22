from claseInmueble import Inmueble

class Casa(Inmueble):
    __metros: int
    
    def __init__(self, localidad, direccion, superficieCubierta, met):
        super().__init__(localidad, direccion, superficieCubierta)
        self.__metros= met
    
    def __str__(self):
        return super().__str__() + f"Metros: {self.__metros}"
    
    def getMetros(self):
        return self.__metros
    
    def getPrecioConstruccion(self):
        return self.__metros * 1.80 * 20000
    