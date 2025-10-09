from estudiante import Estudiante
from asignatura import Asignatura

asignatura = Asignatura("Ingles",5.5,6.3)
estudiante = Estudiante(1,"Ariel","Artes",asignatura)

while True:
    estudiante.menu()
    opcion=int(input("Ingresa una opción (1-5): "))
    match opcion:
        case 1:
            print(estudiante.mostrarEstudiante())
        case 2:
            estudiante.cambiarAsignatura()
        case 3:
            estudiante.cambiarCarrera()
        case 4:
            estudiante.cambiarNotas()
        case 5:
            break
print("\nSalida del Sistema...")

import sys
print(sys.version)