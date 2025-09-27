
from nota import Nota
from rut import Rut
from carrera import Carrera
from fecha import Fecha


listaNotas=[]
rut=Rut(12345678,"9")
carrera=Carrera("Ingeniería Informática")
fecha=Fecha(20,10,2021)
no=Nota(rut,"Jose Luis",carrera,11,5.2,"Inglés",1,fecha)
listaNotas.append(no)

fecha=Fecha(30,10,2021)
no=Nota(rut,"Jose Luis",carrera,11,5.2,"Inglés",2,fecha)
listaNotas.append(no)

for x in listaNotas:
    print(x.mostrarNota())
    
