
from estudiante import Estudiante
from nota import Nota
from rut import Rut
from carrera import Carrera
from fecha import Fecha

def agregarEstudiante():
    listaEstudiantes = [] 
    while True:
        rutEstudiante = int(input("Ingrese rut del estudiante: "))
        dv = input("Ingrese digito verificador del estudiante: ")
        rut = Rut(rutEstudiante, dv)
        nombre = input("Ingrese nombre del estudiante: ")
        carreraEstudiante = input("Ingrese carrera del estudiante: ")
        carrera = Carrera(carreraEstudiante)
        estudiante = Estudiante(rut, nombre, carrera)
        listaEstudiantes.append(estudiante)
        
        salida = input("Desea ingresar otro estudiante? S/N: ")
        if salida.upper() == "N":
            break
    
    return listaEstudiantes  

estudiantes = agregarEstudiante()

for x in estudiantes:
    print(x.mostrarEstudiante())

#print(estudiantes)



""" listaNotas=[]
rut=Rut(12345678,"9")
carrera=Carrera("Ingeniería Informática")
fecha=Fecha(20,10,2021)
no=Nota(rut,"Jose Luis",carrera,11,5.2,"Inglés",1,fecha)
listaNotas.append(no)

fecha=Fecha(30,10,2021)
no=Nota(rut,"Jose Luis",carrera,11,5.2,"Inglés",2,fecha)
listaNotas.append(no)

for x in listaNotas:
    print(x.mostrarNota()) """
    
