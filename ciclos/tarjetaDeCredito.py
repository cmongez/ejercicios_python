# Inicializamos las variables
totalCompras = 0
saldo = -100000

#Añadimos un bucle para repetir el menu hasta que elijan la opcion salir.
while True:
    print("*****MENU*****")
    print("1) Pagar Tarjeta de Credito")
    print("2) Comprar")
    print("3) Salir")
    print("")
    opcion = int(input("Selecciona una opción: "))
    
    #Seleccionamos la opción
    if opcion == 1:
        print("**Pagar Tarjeta**")
        #Añadimos un bucle while que repetiremos hasta que la cantidad ingresada sea válida.
        while True:
            #Añadimos un bloque try except para atrapar error de datos en el input.
            try:
                #Pedimos la cantidad de compras para poder usar nuestro bucle For
                montoAPagar = int(input("Ingresa un monto para realizar el pago de la tarjeta de crédito: "))
            except:
                print("Error: por favor, ingrese solo numeros. ")

            if montoAPagar < 0:
                print("El monto a pagar debe ser mayor o igual a 0.")

            elif montoAPagar > saldo*-1:
                print("El monto a pagar no puede exceder el saldo actual de la tarjeta.")

            else:
                saldo = saldo + montoAPagar
                print("Pago realizado con exito, su saldo actual es de: ", saldo)
                break

    elif opcion == 2:
        print("**Registrar compra**")
        
        #Añadimos un bucle while que repetiremos hasta que la cantidad ingresada sea válida.
        while True:
            #Añadimos un bloque try except para atrapar error de datos en el input.
            try:
                #Pedimos la cantidad de compras para poder usar nuestro bucle For
                cantCompras = int(input("Ingresa la cantidad de compras a registrar: "))
            except:
                print("Error: por favor, ingrese solo numeros. ")

            #Si la cantidad de compras es mayor que cero salimos del bucle con un break, sino repetimos.
            if cantCompras > 0:
                break
            else:
                print("La cantidad de compras debe ser mayor que 0.")

        #Añadimos un bucle for que durara dependiendo de la cantidad de compras a registrar 
        for i in range(cantCompras):
            #Añadimos un bucle while que repetiremos hasta que la cantidad ingresada sea válida.
            while True:
                #Añadimos un bloque try except para atrapar error de datos en el input.
                try:
                    valorCompra = float(input(f"Ingresa el valor de la compra nro {i+1}: "))

                except:
                    print("Error: por favor, ingrese solo numeros. ")

                #Si el valor de la compra es mayor que cero salimos del bucle con un break, sino repetimos.
                if valorCompra > 0:
                    break
                else:
                    print("El valor de la compra debe ser mayor que 0")
            #Una vez validado todo en esa compra lo sumamos al total de las compras
            totalCompras = totalCompras + valorCompra
        #Una vez salgamos del bucle for procedemos a restar el total de las compras a nuestro saldo    
        saldo = saldo - totalCompras
        #Dado que ya usamos el monto del total de las compras y lo restamos al saldo debemos reiniciar esa variable a cero
        totalCompras = 0

    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Selecciona una opción válida.")

print(totalCompras)
print(saldo)
