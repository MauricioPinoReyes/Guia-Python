#1. Asociación - Proveedor-Producto
#Conceptos POO - 2 (Página 5): Asociación con cardinalidad #####

class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Asociación: 1 proveedor -> * productos

class Producto:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.proveedor = None  # Asociación: * productos -> 1 proveedor


""" Justificación:
Página 5: "La Asociación se especifica que dos clases u objetos "
"están relacionados, pero siendo un elemento independiente del otro"
Cardinalidad: Relación "muchos a muchos" (0..* - 0..*) como se muestra en los ejemplos del documento
Independencia: Los proveedores existen independientemente de los productos y viceversa """



##################################################################################################################
##################################################################################################################



#2. Agregación - Inventario-Producto
# #Conceptos POO - 2 (Página 8): Agregación (rombo sin relleno)
class Inventario:
    def __init__(self):
        self.productos = []  # Agregación: inventario ◇-- producto

    def agregar_producto(self, producto):
        # Los productos existen independientemente del inventario
        self.productos.append(producto)

""" Justificación:

Página 8: "Agregación: El conjunto de elementos relacionados forman un 'TODO', aunque los "
"elementos relacionados podrían existir y 'funcionar' independientemente de él"

Representación: "Línea con un rombo sin relleno en un extremo"

Vida útil independiente: si el inventario desaparece, 
los productos siguen existiendo         """



##################################################################################################################
##################################################################################################################

# Conceptos POO - 2 (Página 8): Composición (rombo con relleno)
class Inventario:
    def __init__(self):
        self.movimientos = []  # Composición: inventario ◆-- movimiento

    def crear_movimiento(self, tipo, cantidad, producto):
        # Los movimientos NO existen sin el inventario (composición)
        movimiento = Movimiento(tipo, cantidad, producto)
        self.movimientos.append(movimiento)
        return movimiento
    
"""  Justificación según el documento:

Página 8: "Composición: los elementos relacionados no podrían existir y 'funcionar'"
" independientemente si no formasen parte de dicho 'TODO'"

Representación: "Línea con un rombo con relleno en un extremo"

Vida útil dependiente: Como en el ejemplo universitario del documento, si el inventario
desaparece, los movimientos también    """

""" Conclusiones basadas en el documento:
La agregación y composición son variantes de la asociación (Pág. 8)

La clave diferenciadora es la independencia de los objetos:

Agregación: Los elementos pueden existir por separado

Composición: Los elementos no pueden existir por separado

La dependencia es más débil que la asociación y no implica posesión

La cardinalidad es esencial para especificar correctamente las relaciones """