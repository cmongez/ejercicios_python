# 5)	Cree un sistema de ventas de supermercado en el cual se pueda agregar productos al carro de compras, las opciones del menú serán.
# 1.	Agregar productos
# 2.	Ver canasta
# 3.	Ver total
# 4.	Salir

# •	En agregar productos deberá mostrar un menú con 5 productos y sus precios (creado por usted), cada vez que se seleccione un producto quedará agregado en la lista.
# •	Ver canasta, es mostrar todos los productos seleccionados.
# •	Ver total, es mostrar el total a pagar por el cliente.

# Crear una lista vacía para almacenar los productos seleccionados
productos = []
# Inicializar el total a 0
total = 0

# Definir los precios de los productos
precioArroz = 1200 
precioFideos = 600
precioHarina = 800
precioAgua = 1000 
precioLeche = 900

# Bucle principal del programa
while True:
    # Mostrar el menú principal de opciones
    print("*******MENU*******")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    
    # Solicitar al usuario que seleccione una opción
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        # Si el usuario ingresa un valor que no es un número, mostrar un mensaje de error
        print("Ingrese solo números. \n")
        # Usar continue para volver al inicio del bucle y pedir al usuario que ingrese una opción válida
        continue

    # Opción 1: Agregar productos
    if opcion == 1:
        print("AGREGAR PRODUCTOS")
        # Bucle para mostrar el menú de productos
        while True:
            print("*******PRODUCTOS*******")
            print("1. Arroz $", precioArroz)
            print("2. Fideos $", precioFideos)
            print("3. Harina $", precioHarina)
            print("4. Agua $", precioAgua)
            print("5. Leche $", precioLeche)
            print("6. Salir")

            # Solicitar al usuario que seleccione un producto
            try:
                opcionProducto = int(input("Seleccione una opción: "))
            except ValueError:
                # Si el usuario ingresa un valor que no es un número, mostrar un mensaje de error
                print("Ingrese solo números. \n")
                # Usar continue para volver al inicio del bucle y pedir al usuario que ingrese una opción válida
                continue

            # Agregar el producto seleccionado a la lista y sumar su precio al total
            if opcionProducto == 1:
                total += precioArroz
                productos.append("Arroz")
            elif opcionProducto == 2:
                total += precioFideos
                productos.append("Fideos")
            elif opcionProducto == 3:
                total += precioHarina
                productos.append("Harina")
            elif opcionProducto == 4:
                total += precioAgua
                productos.append("Agua")
            elif opcionProducto == 5:
                total += precioLeche
                productos.append("Leche")
            elif opcionProducto == 6:
                print("Volviendo al menú principal...")
                break
            else:
                print("Seleccione una opción válida. \n")

    # Opción 2: Ver canasta
    elif opcion == 2:
        print("VER CANASTA")
        print("Productos en la canasta:")
        # Mostrar todos los productos en la canasta
        for producto in productos:
            print(producto)
        print()

    # Opción 3: Ver total
    elif opcion == 3:
        print("VER TOTAL")
        # Mostrar el total a pagar
        print("El total a pagar es: $", total, "\n")

    # Opción 4: Salir del programa
    elif opcion == 4:
        print("Saliendo...")
        break

    # Opción inválida
    else:
        print("Seleccione una opción válida. \n")
