#3.	Función que reciba un número entre 1 y 999 y devuelva el número separado en 
# unidad, decena y centena, si por ejemplo recibe:
#a.	El 238, debe devolver el 2, 3 y 8
#b.	El 97, debe devolver 0, 9 y 7
#c.	El 8, debe devolver 0, 0 y 8

def ingresarNumero():
    while True:
        numero = int(input("Ingrese numero: "))
        if 1 <= numero <= 999:
            return numero
        else:
            print("Número fuera de rango. Intente de nuevo.")

def separarNumero(numero):
    centenas = numero // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10
    
    return centenas, decenas, unidades

def main():    
    numero = ingresarNumero()
    c, d, u = separarNumero(numero)
    print(f"{c}, {d} y {u}")

##PP
main()