#==========================
#===========CASO 1=========
#==========================

while True:
    try:
        edad = int(input("Ingrese edad de la persona: "))
        while edad < 0:
            print("Error. Debe ingresar una edad igual o mayor a 0")
            edad = int(input("Ingrese edad de la persona: "))  # ¡Nuevo input para corregir!
        break  # Sale del bucle si la edad es válida
    except ValueError:
        print("El valor debe ser un número entero.")

#==========================
#===========CASO 2=========
#==========================

while True:
    try:
        edad = int(input("Ingrese edad de la persona: "))
        if edad >= 0:
            break  # Edad válida, salir del bucle
        print("Error. Debe ingresar una edad igual o mayor a 0")
    except ValueError:
        print("El valor debe ser un número entero.")