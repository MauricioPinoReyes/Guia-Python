from conexion import DAO
import funciones

dao = DAO()

def menuPrincipal():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Listar Estudiantes ")
        print("2. Listado de Estudiantes y Notas ")
        print("3. Listado de Estudiantes y Notas Menores a 4 ")
        print("4. Promedio de un Estudiante por ID ")
        print("5. Agregar Estudiante ")
        print("6. Agregar Nota ")
        print("7. Actualizar Estudiante ")
        print("8. Salir")
        
        #opc = int(input("Ingrese una opción (1-8): "))
        opc = funciones.ingresarNumero("Ingrese una opción (1-8): ")
        if opc < 1 or opc > 8:
            print("Opción inválida")
        elif opc == 8:
            print("Salida del Sistema OK")
            dao.cerrarConexion()
            break
        else:
            ejecutarOpcionMenu(opc)


def ejecutarOpcionMenu(opc):
    if opc == 1:
        try:
            estudiantes = dao.obtenerEstudiantes()
            if len(estudiantes) > 0:
                funciones.listarEstudiantes(estudiantes)
            else:
                print("La tabla no tiene estudiantes")
        except Exception as e:
            print("Error al listar estudiantes:", e)

    elif opc == 2:
        try:
            estudiantesConNota = dao.obtenerEstudiantesConNotas()
            if len(estudiantesConNota) > 0:
                funciones.listarEstudiantesConNotas(estudiantesConNota)
            else:
                print("La tabla no tiene estudiantes")
        except Exception as e:
            print("Error al listar estudiantes con notas:", e)

    elif opc == 3:
        try:
            estudiantesConNota = dao.obtenerEstudiantesConNotas()
            if len(estudiantesConNota) > 0:
                funciones.listarEstudiantesConNotaMenorA4(estudiantesConNota)
            else:
                print("La tabla no tiene estudiantes")
        except Exception as e:
            print("Error al listar estudiantes con nota menor a 4:", e)

    elif opc == 4:
        try:
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            promediosEstudiante = dao.obtenerPromediosEstudiantePorId(id_estudiante)
            funciones.mostrarPromediosEstudiantePorId(promediosEstudiante)
        except Exception as e:
            print("Error al calcular promedio:", e)


    elif opc==5:
        estudiante=funciones.leerDatosEstudiante()
        try:
            dao.agregarEstudiante(estudiante)
        except Exception as e:
            print("Error al ingresar estudiante:", e)

    elif opc==6:
        nota=funciones.leerDatosNota()
        try:
            dao.agregarNota(nota)
        except Exception as e:
            print("Error al ingresar nota:", e)
    
    elif opc==7:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
        estudiante=dao.buscarEstudiante(id_estudiante)
        if estudiante!=None:
            estudiante=funciones.leerDatosNuevosEstudiante(estudiante)
            dao.actualizarEstudiante(estudiante)
        else:
            print("El estudiante no Existe en la BBDD")                

menuPrincipal()