from paciente import Paciente
from doctor import Doctor


paciente = Paciente("Pepe","Cerrillos","123434343","Resfriado")
doctor = Doctor(1234,"Murillo","Medicina General",4,paciente)

while True:
    doctor.menu()
    opcion=int(input("Ingrese una opción (1-6): "))
    match opcion:
        case 1:
            print(doctor.mostrarDoctor())
        case 2:
            doctor.cambiarNombreDoctor()  
        case 3:
            nombre = input("Ingrese nombre del paciente: ")
            doctor.buscarPacientePorNombre(nombre)
        case 4:
            comuna = input("Ingrese nombre de la comuna: ")
            doctor.buscarPacientePorComuna(comuna)
        case 5:
            doctor.cambiarDiagnostico()
        case 6:
            break             
print("\nGracias por operar con el Sistema...")        