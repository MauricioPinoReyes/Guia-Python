from vehiculo import Vehiculo
from mantencion import Mantencion

veh=Vehiculo(123,"Alexis","BMW","Top",2026,Mantencion("Cambio Frenos","10-08-2025"))

while True:
    veh.menu()
    opcion=int(input("Ingresa una opción (1-5): "))
    match opcion:
        case 1:
            print(veh.mostrarVehiculo())
        case 2:
            veh.cambiarVehiculo()
        case 3:
            id=int(input("ID Vehículo a buscar: "))
            veh.buscarVehiculo(id)
        case 4:
            veh.cambiarMantencion()
        case 5:
            break
print("\nGracias por operar con el Sistema...")


#print(veh.mostrarVehiculo())

#veh=Vehiculo(111,"Angel","Kia","Cerato",2024,Mantencion("Amortiguadores","15-06-2024"))
#print(veh.mostrarVehiculo())
#veh.cambiarVehiculo()
#print(veh.mostrarVehiculo())
# veh.buscarVehiculo(321)

#veh.cambiarMantencion()
#print(veh.mostrarVehiculo())


