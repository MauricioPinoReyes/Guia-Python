
#1. Asociación - Proveedor-Producto (Página 10)
# ASOCIACIÓN BIDIRECCIONAL (Página 10)
class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Asociación bidireccional

class Producto:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.proveedor = None  # Asociación bidireccional

    def asignar_proveedor(self, proveedor):
        """Método que implementa el verbo de la asociación"""
        self.proveedor = proveedor
        proveedor.productos.append(self)

"""  Nuevos fundamentos:

Navegabilidad: Bidireccional (ambas clases se conocen mutuamente)

Verbo implícito: "suministra" (Proveedor suministra Productos)

Cardinalidad: 1..* (Un proveedor suministra muchos productos)

2. Agregación - Inventario-Producto (Página 10-11)
Documento: "El objeto base utiliza al objeto incluido para poder "
"funcionar y su tiempo de vida no está condicionado al tiempo de vida que lo incluye"        """

#################################################################################
################################################################################

# AGREGACIÓN (rombo vacío ◇) - Página 10
class Inventario:
    def __init__(self):
        self.productos = []  # Agregación: productos existen independientemente
    
    def agregar_producto(self, producto):
        """El inventario utiliza productos pero no los posee exclusivamente"""
        if producto not in self.productos:
            self.productos.append(producto)
    
    def quitar_producto(self, producto):
        """Los productos siguen existiendo después de quitarlos del inventario"""
        if producto in self.productos:
            self.productos.remove(producto)
            # El producto continúa existiendo independientemente



#################################################################################
################################################################################


#3. Composición - Inventario-Movimiento (Página 10-11)
# COMPOSICIÓN (rombo lleno ◆)
class Inventario:
    def __init__(self):
        self.movimientos = []  # Composición: movimientos no existen sin inventario
    
    def registrar_movimiento(self, tipo, cantidad, producto):
        """Los movimientos son creados y destruidos con el inventario"""
        movimiento = Movimiento(tipo, cantidad, producto)
        self.movimientos.append(movimiento)
        
        # Si el inventario se destruye, todos los movimientos pierden sentido
        return movimiento
    
    def limpiar_movimientos(self):
        """Los movimientos no tienen significado fuera del contexto del inventario"""
        self.movimientos.clear()

# 4. Dependencia - Reporte-Inventario (Página 11)        

# DEPENDENCIA (Página 11) - Ocultamiento de detalles
class ReporteExistencias:
    def generar_reporte(self, inventario):  # Dependencia temporal
        """Usa el inventario pero oculta los detalles de implementación"""
        # Solo necesita la interfaz pública del inventario
        return self._formatear_datos(inventario.obtener_productos())
    
    def _formatear_datos(self, productos):  # Método privado (-)
        """Ocultamiento de detalles de implementación"""
        return [f"{p.codigo}: {p.stock}" for p in productos]
    

########################################################### 
####### Diferencia entre Agregación y Composición   ####### 
###########################################################  

# Agregación (Rombo vacío ◇)

class Inventario:
    def __init__(self):
        self.productos = []  # AGREGACIÓN: Los productos existen independientemente

# Los productos se crean FUERA del inventario
producto1 = Producto("P001", "Laptop", 1000)
producto2 = Producto("P002", "Mouse", 50)

inventario = Inventario()
inventario.productos.append(producto1)  # Agregamos productos existentes
inventario.productos.append(producto2)

# Si el inventario se destruye, los productos siguen existiendo
del inventario
print(producto1.descripcion)  # ✅ "Laptop" - Sigue existiendo


#####################################################################################
#####################################################################################

# Composición (Rombo lleno ◆)

class Inventario:
    def __init__(self):
        self.movimientos = []  # COMPOSICIÓN: Los movimientos NO existen sin inventario

    def registrar_movimiento(self, tipo, cantidad, producto):
        # Los movimientos se crean DENTRO del inventario
        movimiento = Movimiento(tipo, cantidad, producto)
        self.movimientos.append(movimiento)
        return movimiento

inventario = Inventario()
movimiento = inventario.registrar_movimiento("entrada", 10, producto1)

# Si el inventario se destruye, los movimientos pierden sentido
del inventario
# movimiento.tipo  # ❌ ERROR: El movimiento ya no tiene contexto válido


#########################################################
############## Ejemplo Practico #########################
#########################################################

# AGREGACIÓN - Los productos existen antes y después del inventario
producto_existente = Producto("P003", "Teclado", 80)

inventario = Inventario()
inventario.productos.append(producto_existente)  # Agregación

# El producto sigue existiendo independientemente
inventario_alternativo = Inventario()
inventario_alternativo.productos.append(producto_existente)  # Mismo producto en otro inventario

# COMPOSICIÓN - Los movimientos son parte integral del inventario
movimiento1 = inventario.registrar_movimiento("entrada", 5, producto_existente)
movimiento2 = inventario.registrar_movimiento("salida", 2, producto_existente)

# Los movimientos son exclusivos de ESTE inventario
# No pueden transferirse a otro inventario porque pierden sentido


""" Analogía de la Vida Real
Agregación (Como una Biblioteca y sus Libros)
La biblioteca contiene libros

Los libros existen antes de entrar a la biblioteca

Si cierra la biblioteca, los libros se trasladan a otra

Composición (Como una Casa y sus Habitaciones)
La casa está compuesta por habitaciones

Las habitaciones se construyen CON la casa

Si demueles la casa, las habitaciones también desaparecen """

#######################################################
##### ¿Por qué es Asociación y NO Composición? #######
#####################################################

# Razón Fundamental
# Porque los Productos y Proveedores tienen vida independiente:

# Los productos existen ANTES y DESPUÉS de la relación
proveedor = Proveedor("TechCorp", "contacto@tech.com")
producto = Producto("P001", "Laptop", 1000)  # ✅ Producto creado INDEPENDIENTEMENTE

# Establecemos la relación ASOCIATIVA
producto.proveedor = proveedor
proveedor.productos.append(producto)

# Si el proveedor desaparece, el producto sigue existiendo
del proveedor
print(producto.descripcion)  # ✅ "Laptop" - El producto SOBREVIVE

# El producto puede cambiar de proveedor
nuevo_proveedor = Proveedor("NuevoTech", "info@nuevotech.com")
producto.proveedor = nuevo_proveedor  # ✅ Relación CAMBIABLE


############################################################
##### Composición vs Asociación - La Prueba Definitiva #######
###########################################################

# Si fuera Composición (Incorrecto ❌):

class Proveedor:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto
        self.productos = []  # ❌ Esto sugeriría composición (pero sería incorrecto)

    def crear_producto(self, codigo, descripcion, precio):
        # ❌ Los productos se crearían DENTRO del proveedor (composición)
        producto = Producto(codigo, descripcion, precio)
        self.productos.append(producto)
        return producto

# Uso incorrecto (composición)
proveedor = Proveedor("TechCorp", "contacto@tech.com")
producto = proveedor.crear_producto("P001", "Laptop", 1000)  # ❌ Producto creado por proveedor

# Si el proveedor se elimina, el producto moriría (¡pero no debería!)
del proveedor
# producto.descripcion  # ❌ Esto fallaría en composición (pero en realidad no debería)

# Asociación Correcta (✅):

# Los productos se crean INDEPENDIENTEMENTE
producto1 = Producto("P001", "Laptop", 1000)
producto2 = Producto("P002", "Mouse", 50)

proveedor = Proveedor("TechCorp", "contacto@tech.com")

# Se ESTABLECEN relaciones asociativas
producto1.proveedor = proveedor
proveedor.productos.append(producto1)

producto2.proveedor = proveedor  
proveedor.productos.append(producto2)

# Relaciones FLEXIBLES y REVERSIBLES
otro_proveedor = Proveedor("OtraEmpresa", "info@otra.com")
producto2.proveedor = otro_proveedor  # ✅ Cambio de proveedor

# Pruebas que Confirman que es Asociación

# Prueba 1: Vida Independiente

# Los productos existen sin proveedor
producto_sin_proveedor = Producto("P003", "Teclado", 80)
print(producto_sin_proveedor.descripcion)  # ✅ Funciona perfectamente

# Los proveedores existen sin productos
proveedor_sin_productos = Proveedor("Nuevo", "info@nuevo.com")
print(proveedor_sin_productos.nombre)  # ✅ Funciona perfectamente

# Prueba 2: Relación Múltiple

# Un producto puede tener múltiples relaciones (con diferentes proveedores en el tiempo)
producto = Producto("P004", "Monitor", 300)

proveedor_a = Proveedor("ProveedorA", "a@ejemplo.com")
proveedor_b = Proveedor("ProveedorB", "b@ejemplo.com")

# Cambio de proveedor a lo largo del tiempo
producto.proveedor = proveedor_a
# ... luego ...
producto.proveedor = proveedor_b  # ✅ Relación CAMBIABLE

# Prueba 3: Cardinalidad Múltiple

# Un proveedor tiene MUCHOS productos
proveedor = Proveedor("Distribuidor", "contacto@dist.com")

producto1 = Producto("P005", "Tablet", 400)
producto2 = Producto("P006", "Cargador", 30)
producto3 = Producto("P007", "Funda", 20)

proveedor.productos.extend([producto1, producto2, producto3])  # ✅ 1 a muchos

# Un producto tiene UN proveedor (pero podría cambiar)
producto1.proveedor = proveedor

