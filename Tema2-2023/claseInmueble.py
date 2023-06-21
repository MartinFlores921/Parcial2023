import abc
from abc import ABC

class Inmueble(ABC):
    __localidad: str
    __direccion: str
    __superficieCubierta:int
    
    def __init__(self, loc, dir, super):
        self.__localidad= loc
        self.__direccion= dir
        self.__superficieCubierta= super
    
    def __str__(self):
      return f"Localidad {self.__localidad}, Direccion: {self.__direccion}, SuperficieCubierta: {self.__superficieCubierta}"
    
    
    def getLocalidad(self):
        return self.__localidad
    
    def getDireccion(self):
        return self.__direccion
    
    def getSuperficieCubierta(self):
        return self.__superficieCubierta
    
    def getImporte(self):
        return self.__superficieCubierta * 15 * self.getPrecioConstruccion()
    
    @abc.abstractclassmethod
    def getPrecioConstruccion():
        pass
    
    
    