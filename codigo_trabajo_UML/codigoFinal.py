class Proveedor:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto
        self.productos = []  # Asociación con Producto

class Producto:
    def __init__(self, codigo, descripcion, precio, stock_inicial=0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.proveedor = None  # Asociación con Proveedor

class Movimiento:
    def __init__(self, tipo, cantidad, producto):
        self.tipo = tipo  # "entrada" o "salida"
        self.cantidad = cantidad
        self.producto = producto

class Inventario:
    def __init__(self):
        self.productos = []  # Agregación: Productos existen independientemente
        self.movimientos = []  # Composición: Movimientos no existen sin inventario
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def quitar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
    
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def registrar_movimiento(self, tipo, cantidad, producto):
        if tipo == "entrada":
            producto.stock += cantidad
        elif tipo == "salida":
            if producto.stock >= cantidad:
                producto.stock -= cantidad
            else:
                print("Error: Stock insuficiente")
                return None
        
        movimiento = Movimiento(tipo, cantidad, producto)  # Creación interna (composición)
        self.movimientos.append(movimiento)
        return movimiento

class ReporteExistencias:
    def generar_reporte(self, inventario):  # Dependencia: usa Inventario temporalmente
        print("\n=== REPORTE DE EXISTENCIAS ===")
        print(f"{'Código':<10} {'Descripción':<20} {'Precio':<10} {'Stock':<10} {'Proveedor':<15}")
        print("-" * 70)
        for producto in inventario.productos:
            proveedor_nombre = producto.proveedor.nombre if producto.proveedor else "N/A"
            print(f"{producto.codigo:<10} {producto.descripcion:<20} ${producto.precio:<9} {producto.stock:<10} {proveedor_nombre:<15}")
    
    def generar_reporte_movimientos(self, inventario):  # Otra dependencia
        print("\n=== MOVIMIENTOS RECIENTES ===")
        print(f"{'Tipo':<10} {'Cantidad':<10} {'Producto':<20} {'Código':<10}")
        print("-" * 50)
        for mov in inventario.movimientos[-10:]:  # Solo usa, no almacena
            print(f"{mov.tipo:<10} {mov.cantidad:<10} {mov.producto.descripcion:<20} {mov.producto.codigo:<10}")

# Función principal de la aplicación
def main():
    inventario = Inventario()
    
    # Crear algunos proveedores y productos de ejemplo
    proveedor1 = Proveedor("TechCorp", "contacto@tech.com")
    proveedor2 = Proveedor("ElectroParts", "info@electroparts.com")
    
    producto1 = Producto("P001", "Laptop Gaming", 1200, 15)
    producto2 = Producto("P002", "Monitor 24\"", 300, 25)
    producto3 = Producto("P003", "Teclado Mecánico", 80, 40)
    
    # Establecer asociaciones
    producto1.proveedor = proveedor1
    producto2.proveedor = proveedor1
    producto3.proveedor = proveedor2
    proveedor1.productos.extend([producto1, producto2])
    proveedor2.productos.append(producto3)
    
    # Agregar productos al inventario (agregación)
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)
    
    # Registrar algunos movimientos (composición)
    inventario.registrar_movimiento("entrada", 10, producto1)
    inventario.registrar_movimiento("salida", 5, producto1)
    inventario.registrar_movimiento("entrada", 15, producto2)
    inventario.registrar_movimiento("salida", 8, producto3)
    
    reporte = ReporteExistencias()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Ver reporte de existencias")
        print("2. Ver movimientos recientes")
        print("3. Registrar entrada de productos")
        print("4. Registrar salida de productos")
        print("5. Agregar nuevo producto")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            reporte.generar_reporte(inventario)
        
        elif opcion == "2":
            reporte.generar_reporte_movimientos(inventario)
        
        elif opcion == "3":
            codigo = input("Código del producto: ")
            producto = inventario.buscar_producto(codigo)
            if producto:
                try:
                    cantidad = int(input("Cantidad a ingresar: "))
                    inventario.registrar_movimiento("entrada", cantidad, producto)
                    print(f"Se registró la entrada de {cantidad} unidades de {producto.descripcion}")
                except ValueError:
                    print("Error: La cantidad debe ser un número entero")
            else:
                print("Error: Producto no encontrado")
        
        elif opcion == "4":
            codigo = input("Código del producto: ")
            producto = inventario.buscar_producto(codigo)
            if producto:
                try:
                    cantidad = int(input("Cantidad a retirar: "))
                    movimiento = inventario.registrar_movimiento("salida", cantidad, producto)
                    if movimiento:
                        print(f"Se registró la salida de {cantidad} unidades de {producto.descripcion}")
                except ValueError:
                    print("Error: La cantidad debe ser un número entero")
            else:
                print("Error: Producto no encontrado")
        
        elif opcion == "5":
            codigo = input("Código del nuevo producto: ")
            descripcion = input("Descripción: ")
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                
                nuevo_producto = Producto(codigo, descripcion, precio, stock)
                
                # Preguntar si se asociará a un proveedor existente
                agregar_proveedor = input("¿Asociar a proveedor existente? (s/n): ").lower()
                if agregar_proveedor == 's':
                    nombre_proveedor = input("Nombre del proveedor: ")
                    # Buscar si el proveedor ya existe
                    proveedor_existente = None
                    for p in [proveedor1, proveedor2]:
                        if p.nombre.lower() == nombre_proveedor.lower():
                            proveedor_existente = p
                            break
                    
                    if proveedor_existente:
                        nuevo_producto.proveedor = proveedor_existente
                        proveedor_existente.productos.append(nuevo_producto)
                        print(f"Producto asociado al proveedor {proveedor_existente.nombre}")
                    else:
                        print("Proveedor no encontrado. El producto se creará sin proveedor.")
                
                inventario.agregar_producto(nuevo_producto)
                print(f"Producto {descripcion} agregado al inventario")
                
            except ValueError:
                print("Error: El precio debe ser un número y el stock un entero")
        
        elif opcion == "6":
            print("¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()