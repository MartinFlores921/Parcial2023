from claseInmueble import Inmueble

class Departamento(Inmueble):
    __cantDormitorio: int
    __nroMonoblock: int
    __nroDepto: int
    __piso: int
    
    def __init__(self, localidad, direccion, superficieCubierta, cantD, nroMono, nroDep, piso ):
        super().__init__(localidad, direccion, superficieCubierta)
        self.__cantDormitorio= cantD
        self.__nroMonoblock= nroMono
        self.__nroDepto = nroDep
        self.__piso= piso
    
    def __str__(self):
        return super().__str__() + f"CantDor: {self.__cantDormitorio}, NroMono:{self.__nroMonoblock}, NroDepto:{self.__nroDepto}, Piso:{self.__piso}"
    
    def getCantDormitorio(self):
        return self.__cantDormitorio
    
    def getNroMonoblock(self):
        return self.__nroMonoblock
    
    def getNroDepto(self):
        return self.__nroDepto
    
    def getPiso(self):
        return self.__piso
    
    def getPrecioConstruccion(self):
        return self.__cantDormitorio * 17000
    
    
    