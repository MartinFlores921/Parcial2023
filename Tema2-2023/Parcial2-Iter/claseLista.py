from claseNodo import Nodo
from claseDepartamento import Departamento
class Lista:
    __comienzo:Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo=None
        self.__actual= None
        self.__tope=0
        self.__indice=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    
    def CargarInmueble(self, inmueble):
        nodo= Nodo(inmueble)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__actual= nodo
        self.__tope +=1
    
    def insertarInmueble(self,posicion, inmueble):
        if posicion < 0 or posicion > self.__tope:
             raise Exception("Posicion No Valida")
        else:
            nuevo= Nodo(inmueble)
            if posicion == 0:
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo= nuevo
            else:
              cont=0
              anterior = self.__comienzo
              posterior= self.__comienzo
              while posterior !=None and cont < posicion:
                anterior= posterior
                posterior= posterior.getSiguiente()
                cont +=1
              anterior.setSiguiente(nuevo)
              nuevo.setSiguiente(posterior)
            self.__tope +=1
      
    def AgregarAlFinal(self, inmueble):
        nuevo= Nodo(inmueble)
        if self.__comienzo == None:
            self.__comienzo= nuevo
            self.__tope +=1
        else:
            aux= self.__comienzo
            while aux.getSiguiente() != None:
                aux= aux.getSiguiente()
            aux.setSiguiente(nuevo)
            self.__tope +=1
    
    def mostrarDormitorios(self, inm, cant):
        if isinstance(inm, Departamento):
            if inm.getCantDormitorio() < cant:
                print("{}, Importe:{}".format(inm, inm.getImporte()))
    
    def mostrarDepto(self, inm):
        if isinstance(inm, Departamento):
            print("Direccion:{}, SupCub:{}, Importe: {}".format(inm.getDireccion(), inm.getSuperficieCubierta(), inm.getImporte()))
    
    def mayor(self, inm):
        max= 0
        if max < inm.getImporte():
            max = inm.getImporte()
        return max
            