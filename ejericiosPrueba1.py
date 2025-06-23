#4)	Una persona que va de compras a la tienda “Enano, S.A.”, decide llevar un control 
# sobre lo que va comprando, para saber la cantidad de dinero que tendrá que pagar al 
# llegar a la caja. La tienda tiene una promoción del 20% de descuento sobre aquellos 
# artículos cuya etiqueta sea roja. Determinar la cantidad de dinero que esta persona deberá pagar

# HACER ESTE CLICLO PARA VARIOS CLIENTES
# SUGERENCIA: INSERTAR OTRO CICLO DENTRO DE LOS ARTICULOS

""" preguntar al profesor como se puede hacer para mostrar los resultados
por cliente sin arreglos """

""" precioTotal=0
cant_clientes = int(input("Ingrese cantidad de clientes: "))
for x in range(cant_clientes):
    cantArticulos = int(input("Ingrese cantidad de articulos: "))
    for x in range(cantArticulos):
        precio = float(input(f"Ingrese precio del articulo {x+1}: "))
        etiqueta = int(input("Etiqueta roja? 1 para si, 0 para no: "))
        if etiqueta == 1:
            precio = precio * 0.80
        precioTotal += precio

print(f"La cantidad de articulos ingresados es: {cantArticulos} ")
print(f"El precio total de la compra es: {precioTotal} ") """

cant_clientes = int(input("Ingrese cantidad de clientes: "))
# Procesar cada cliente
for cliente_num in range(1, cant_clientes + 1):
    print(f"\n--- Cliente {cliente_num} ---")
    
    # Inicializar total para este cliente
    total_cliente = 0.0
    
    # Pedir cantidad de artículos
    cant_articulos = int(input("Ingrese cantidad de artículos: "))
    
    # Procesar cada artículo
    for art_num in range(1, cant_articulos + 1):
        print(f"\nArtículo {art_num}:")
        
        # Pedir precio y etiqueta
        precio = float(input("Precio del artículo: "))
        etiqueta = int(input("¿Etiqueta roja? (1 para sí, 0 para no): "))
        
        # Aplicar descuento si es etiqueta roja
        if etiqueta == 1:
            precio *= 0.80  # 20% de descuento
        
        # Acumular al total del cliente
        total_cliente += precio
    
    # Mostrar resultados para este cliente
    print(f"\nResumen para el cliente {cliente_num}:")
    print(f"Artículos comprados: {cant_articulos}")
    print(f"Total a pagar: ${total_cliente:.2f}")

print("\nProceso completado para todos los clientes.")