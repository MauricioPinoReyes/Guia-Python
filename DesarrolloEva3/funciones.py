def listarEstudiantes(estudiantes):
    print("\nListado de Estudiantes\n")
    c=1
    for estudiante in estudiantes:
        datos="{0}. Id: {1} | Rut: {2} | Nombres: {3} | Apellidos: {4} | Estado: {5} "
        print(datos.format(c,estudiante[0],estudiante[1],estudiante[2],estudiante[3],mostrarEstado(estudiante[4])))
        c+=1
    print("")  

def mostrarEstado(estado):
    if estado==1:
        return "Activo"
    else:
        return "Inactivo"     

def listarEstudiantesConNotas(estudiantesconNota):
    print("\nListado de Estudiantes con Calificaciones\n")
    c = 1
    for estudiante in estudiantesconNota:
        datos = "{0}. | Nombre: {1} {2} | Asignatura: {3} | Nota: {4}"
        print(datos.format(c, estudiante[1], estudiante[2], estudiante[3], estudiante[4]))
        c += 1
    print("")


def listarEstudiantesConNotaMenorA4(estudiantesconNota):
    print("\nListado de Estudiantes con Nota < 4.0\n")
    c = 1
    for estudiante in estudiantesconNota:
        if estudiante[4] < 4.0:  
            datos = "{0}. | Nombre Estudiante : {1} {2} | Nota: {3}"
            print(datos.format(c, estudiante[1], estudiante[2], estudiante[4]))
            c += 1
    print("")        


def mostrarPromediosEstudiantePorId(promediosEstudiante):
    print("\nPromedios del Estudiante por Id\n")
    if promediosEstudiante:
        for promedio in promediosEstudiante:
            datos = "Nombre: {0} {1} | Asignatura: {2} | Promedio: {3}"
            print(datos.format(promedio[0], promedio[1], promedio[2], promedio[3]))
    else:
        print("No se encontraron registros para el estudiante indicado.")
    print("")


def leerDatosEstudiante():
    rut=input("Rut: ")
    nombres=input("Nombres: ")
    apellidos=input("Apellidos: ")
    estado= validarEstado()
    estudiante=(rut,apellidos,nombres,estado)
    return estudiante     

def leerDatosNota():
    id_estudiante=int(input("Id Estudiante: "))
    asignatura=input("Asignatura: ")
    nota=float(input("Nota: "))
    nota=(id_estudiante,asignatura,nota)
    return nota  

def leerDatosNuevosEstudiante(estudiante):
    id = estudiante[0]
    rut = estudiante[1]
    nombres = estudiante[2]
    apellidos = estudiante[3]
    estado = estudiante[4]
    
    print("Datos actuales del estudiante:", estudiante)
    
    while True:
        print("\n--- MODIFICAR ESTUDIANTE ---")
        print("Id:", id)
        print("1. Modificar Rut:", rut)
        print("2. Modificar Nombres:", nombres)
        print("3. Modificar Apellidos:", apellidos)
        print("4. Modificar Estado:", estado)
        print("5. Guardar cambios y retornar")
        
        opc = ingresarNumero("Ingrese una opción (1-5): ")
        
        if opc == 1:
            rut = input("Nuevo rut: ")
        elif opc == 2:
            nombres = input("Nuevos nombres: ") 
        elif opc == 3:
            apellidos = input("Nuevos apellidos: ") 
        elif opc == 4:
            estado = validarEstado() 
        elif opc == 5:
            estudiante_actualizado = (id, rut, nombres, apellidos, estado)
            print("Datos a guardar:", estudiante_actualizado) 
            break
        else:
            print("Opción inválida")
    
    return estudiante_actualizado


def ingresarNumero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except Exception:
            print(" Debe ingresar un número.")

def validarEstado():
    while True:
        estado = ingresarNumero("Estado (1=Activo, 2=Inactivo): ")
        if estado in [1, 2]:
            return estado
        print("Error: El estado debe ser 1 (Activo) o 2 (Inactivo)")            