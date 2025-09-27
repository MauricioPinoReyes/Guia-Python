from estudiante import Estudiante

lista=[]
est=Estudiante(1,"Angel",30)
lista.append(est)
lista.append(Estudiante(2,"Ximena",32))
lista.append(Estudiante(3,"Diego",25))
lista.append(Estudiante(4,"Camila",21))

while True:
    est.menu()
    opcion=int(input("Ingresa una opción (1-6): "))
    match opcion:
        case 1:
            id=est.leerId()
            objeto=est.buscarEstudiante(id,lista)
            if objeto==None:
                lista.append(est.agregarEstudiante(id))
            else:
                print("El registro está ocupado:",objeto.nombre)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("\nNómina de Estudiantes")
            for item in lista:
                print(item.mostrarEstudiante())
        case 6:
            print("\nHasta la vista...")
            break




