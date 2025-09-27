from empleado import Empleado
from sueldo import Sueldo

# FORMA 1
sue=Sueldo(529000,100000)
emp=Empleado(1,"Gutiérrez","Javier","Docente",sue)
print(emp.mostrarEmpleado())

# FORMA
emp=Empleado(2,"Molina","Alfredo","Supervisor",Sueldo(800000,50000))
print(emp.mostrarEmpleado())
