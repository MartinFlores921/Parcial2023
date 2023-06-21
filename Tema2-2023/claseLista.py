from claseNodo import Nodo
#from claseInmueble import Inmueble

from claseDepartamento import Departamento
from claseCasa import Casa
class Lista:
    __comienzo: Nodo
    __tope: int
    
    def __init__(self):
        self.__comienzo= None
        self.__tope= 0
    
    def CargarInmueble(self, inmueble): #Cuando se muestra, se muestra en orden inverso al ingresado
        nodo= Nodo(inmueble)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__tope +=1
   
    
    """def mostrarLista(self):
        aux= self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(), Departamento):
                    print("Localidad: {}, Direccion: {}, SuperficieCub:{}, CantDor:{}, NroMono: {}, NroDepto:{}, Piso: {}".format(aux.getDato().getLocalidad(), aux.getDato().getDireccion(), aux.getDato().getSuperficieCubierta(), aux.getDato().getCantDormitorio(), aux.getDato().getNroMonoblock(), aux.getDato().getNroDepto(), aux.getDato().getPiso()))
            else: 
                if isinstance(aux.getDato(), Casa):
                    print("Localidad: {}, Direccion: {}, SuperficieCub:{}, Metros: {}".format(aux.getDato().getLocalidad(), aux.getDato().getDireccion(), aux.getDato().getSuperficieCubierta(), aux.getDato().getMetros()))
            aux= aux.getSigueinte()"""
    def mostrarLista(self):
        aux= self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux= aux.getSiguiente()
    
    def getTope(self):
        return self.__tope
    
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
    
    
    def mostrarDepartamento(self):
        aux= self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(), Departamento):
                #dep= Departamento(aux.getDato()) Casteo, hay que hacerlo en el parcial
                print("Direccion:{}, SupeCub: {}, Importe: {}".format(aux.getDato().getDireccion(), aux.getDato().getSuperficieCubierta(), aux.getDato().getImporte()))  
            aux= aux.getSiguiente()
    
    def mostrarDormitorios(self, cant):
        aux= self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(), Departamento):
               # dep= Departamento(aux.getDato())
                if aux.getDato().getCantDormitorio() < cant:
                    print(aux.getDato())
            aux= aux.getSiguiente()
    
    def eliminar(self, localidad):
        aux= self.__comienzo
        encontrado= False
        if aux.getDato().getLocalidad() == localidad:
                encontrado= True
                print("Encontrado y Eliminado")
                self.__comienzo= aux.getSiguiente()
                self.__tope -=1
                del aux
        else:
                ant= aux
                aux= aux.getSiguiente()
                while not encontrado and aux != None:
                    if aux.getDato().getLocalidad() == localidad:
                        encontrado= True
    
                    else:
                        ant= aux
                        aux= aux.getSiguiente()
                if encontrado:
                        print("Encontrado y Eliminado: {}".format(aux.getDato()))
                        ant.setSiguiente(aux.getSiguiente())
                        self.__tope -=1
                        del aux
                else:
                    print("La localidad No Existe")
    
    def mostrarMayor(self):
        aux= self.__comienzo
        max= aux.getDato().getImporte()
        aux= aux.getSiguiente()
        while aux != None:
            if max < aux.getDato().getImporte():
                max= aux.getDato().getImporte()
            aux= aux.getSiguiente()
        
        print("El maximo importe es: {}".format(max))
    
                
                
        
        
            
            
            
                        
    
            
                    
    