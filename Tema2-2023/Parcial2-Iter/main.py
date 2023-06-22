from claseLista import  Lista
from claseDepartamento import Departamento
from claseCasa import Casa
if __name__ == "__main__":
    list= Lista()
    Inmueble1= Departamento("Capital", "Barrio Sarmiento", 200, 6, 4, 25, 3)
    Inmueble2= Casa("Santa Lucia", "Barrio Medalla",143, 55)
    Inmueble3= Departamento("Rivadavia", "Barrio Ayres del Libertador", 400, 9, 8, 1, 5)
    Inmueble4= Casa("Rawson", "Barrio Villa Krause", 245, 400)
    list.CargarInmueble(Inmueble1)
    list.CargarInmueble(Inmueble2)
    list.CargarInmueble(Inmueble3)
    list.CargarInmueble(Inmueble4)
    print("La lista es: \n")
    for inmueble in list:
        print(inmueble)
    print("INCISO 1")
    Inmueble5= Casa("Caucete", "Barrio Argentina", 430, 120)
    pos= int(input("Ingrese una Posicion \n"))
    list.insertarInmueble(pos-1, Inmueble5)
    for inmueble in list:
        print(inmueble)
    print("INCISO 2")
    Inmueble6= Departamento("Pocito", "Barrio Centenario", 467, 5, 9, 3, 4)
    list.AgregarAlFinal(Inmueble6)
    for inmueble in list:
        print(inmueble)
    print("INCISO 3")
    cant= int(input("Ingrese la Cantidad de Dormitorios \n"))
    for inmueble in list:
      list.mostrarDormitorios(inmueble,cant)
    print("Inciso 4")
    for inmueble in list:
        list.mostrarDepto(inmueble)
    print("Inciso 5")
    max= 0
    for inmueble in list:
        max= list.mayor(inmueble)
    print("El Maximo es: {}".format(max))
        