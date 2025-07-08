"""
Leer dos números y mostrarlos de manera ascendente
Debes crear una función para leer los números y otra
función para ordenarlos
Ejemplo:
1) Si se reciben los números 10 y 20, debe devolver 10,20
2) Si se reciben los números 100 y 50, debe devolver 50,100
"""

def leerNumero():
    return float(input("Ingresa un número: "))

def ordenarNumeros(a,b):
    if a < b:
        return a,b
    else:
        return b,a

def leerRespuesta():
    return input("Desea continuar (S/N): ").upper()

def main():
    while True:
        (a,b)=ordenarNumeros(leerNumero(),leerNumero())
        print("El orden ascendente es: ",a,",",b)
        if leerRespuesta()=="N":
            break
# PP
main()




