from claseLista import Lista
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
    list.mostrarLista()
    print("{}".format(list.getTope()))
    Inmueble5= Casa("Caucete", "Barrio Argentina", 430, 120)
    print("INCISO 1")
    pos= int(input("Ingrese una Posicion para Insertar el Inmueble: \n"))
    list.insertarInmueble(pos-1, Inmueble5)
    list.mostrarLista()
    print("INCISO 2")
    Inmueble6= Departamento("Pocito", "Barrio Centenario", 467, 5, 9, 3, 4)
    list.AgregarAlFinal(Inmueble6)
    print("A continuacion se muestra la Lista con el Inmueble agregado al final")
    list.mostrarLista()
    print("INCISO 3")
    cant= int(input("Ingrese la Cantidad de Dormitorios \n"))
    list.mostrarDormitorios(cant)
    print("INCISO 4")
    list.mostrarDepartamento()
    print("INCISO 5")
    dir= input("Ingrese una Localidad para eliminar ese inmueble \n")
    list.eliminar(dir)
    print("A continuacion se muestra la Lista luego de si hubo alguna eliminacion: ")
    list.mostrarLista()
    print("Inciso 7")
    list.mostrarMayor()
    print("Inciso 6")
    
    
    
    """Lote de Prueba
    Para el Inciso 3:
    assert.in(elemento a buscar, objeto)
    Para el Inciso 4
    *Barrio Sarmiento: 
    -PrecioConstruccion: 6* 17000= 102000
    -Importe: 200* 15* 102.000= 306.000.000
    *Barrio Ayres del Libertador:
    -PrecionConstruccion: 9* 17000=153.000
    -Importe: 400 * 15 * 153.000 = 918.000
    *Barrio Centenario:
    -PrecioConstruccion: 5 * 17000 = 85.000
    -Importe: 467 * 15 *85000 = 595.425.000
    
    
    
    """