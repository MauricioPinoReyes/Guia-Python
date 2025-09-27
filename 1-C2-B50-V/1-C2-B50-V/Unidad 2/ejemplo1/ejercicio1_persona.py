class Persona():
    pass

"""
Una clase (en este caso Python) es un archivo (.py) con el cual vamos a representar
un objeto
Con "pass" le estamos indicando que es una clase vacía o sin implementar, es decir, no 
se han declarado ni atributo ni métodos
"""

# ¿Cómo nos comunicamos con una clase?
# Respuesta: Con una "instancia" desde el MAIN o PP
# instancia: es un atributo de tipo objeto (abstracto) que hace la comunicación

# MAIN o PP
francisco=Persona()
# print(francisco)
francisco.nombre="Francisco"    # con la instancia "francisco" se ha creado el atributo
                                # nombre, el cual tiene el valor inicial "Francisco"
francisco.edad=30               # similar a lo anterior, pero con el atributo "edad"

print("Los datos de la Persona son:")
print("Nombre   :",francisco.nombre)
print("Edad     :",francisco.edad)

katty=Persona()
katty.comuna="Maipu"
