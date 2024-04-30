# Ejercicio 12: 
# Se requiere implementar un sistema para el mesón de 
# CineDuoc, en el cual, va desde el sistema de venta de 
# boletos, hasta los agregados (palomitas y bebidas.). 
# Una simulación del sistema comienza con consultar al cliente 
# si pertenece a Duoc (estudiante o funcionario), el cliente 
# muestra la placa o identificación (en caso de tener) por lo que 
# el vendedor registra en el sistema True o False (Pertenece, no 
# pertenece). Luego le consulta que entrada desea: Las 
# posibles entradas son: 
# Estreno → $4.800 
# Normal → $2.900 
# El cliente al seleccionar una, también debe indicar la cantidad 
# que desea, luego el sistema le consultará si desea agregar 
# palomitas de maíz a su pedido, si la respuesta es “si”, 
# entonces el sistema muestra las siguientes promociones: 
# Palomitas Pequeña → $2.500 
# Palomitas Mediana → $4.500 
# Palomitas Grande → $7.800 
# Una vez que ingresa el tipo, también debe seleccionar la 
# cantidad. 
# Finalmente, se le consulta si desea agregar bebidas al 
# sistema de la misma forma: 
# Bebida Pequeña → $1.000 
# Bebida Mediana → $1.250 
# Bebida Grande → $2.000 
# El sistema deberá mostrar el total a pagar por el cliente, 
# solicitar el efectivo e indicar el vuelto necesario para el cliente. 
# Adicionalmente el sistema hará un descuento automático si el 
# cliente pertenece a Duoc, el descuento es de 30% y sólo se 
# aplica a las entradas compradas (no a las Palomitas ni 
# Bebidas).

#INICIALIZAMOS ALGUNAS VARIABLES
totalBebidas = 0
totalPalomitas = 0


#Preguntamos si pertenece al Duoc y guardamos esa respuesta para usarla mas tarde
pertenece = bool(int(input("¿El cliente pertenece al Duoc? : 1) Si / 2) No")))


#Preguntamos el tipo de entradas
print("¿Qué tipo de entradas desea?: ")
print("1. Estreno → $4.800") 
print("2. Normal → $2.900")
opcEntradas = int(input("Seleccione una opción: "))

#asignamos el valor de la entrada dependiendo del tipo seleccionado 
if opcEntradas == 1:
    valorEntradas = 4800
elif opcEntradas == 2:
    valorEntradas = 2900

#preguntamos la cantidad de entradas
cantEntradas = int(input("Indique la cantidad de entradas: "))

#Calculamos el monto total de las entradas multiplicando el valor segun el tipo por la cantidad
totalEntradas = cantEntradas * valorEntradas

#preguntamos si quiere palomitas
respPalomitas = input("¿Desea agregar palomitas de maíz? si/no: ")

if respPalomitas == "si":
    #Mostramos las opciones de las palomitas
    print("1. Palomitas Pequeña → $2.500") 
    print("2. Palomitas Mediana → $4.500") 
    print("3. Palomitas Grande → $7.800")
    opcPalomitas = int(input("Seleccione una opción: "))

    #Asignamos el valor de las palomitas segun el tipo seleccionado
    if opcPalomitas == 1:
        valorPalomitas = 2500
    elif opcPalomitas == 2:
        valorPalomitas = 4500
    elif opcPalomitas == 3:
        valorPalomitas = 7800

    #preguntamos la cantidad de palomitas
    cantPalomitas = int(input("Ingrese la cantidad de palomitas que desea: "))

    #Calculamos el monto total de las palomitas multiplicando el valor segun el tipo por la cantidad
    totalPalomitas = cantPalomitas * valorPalomitas

#Preguntamos si quiere bebidas
respBebidas = input("¿Desea agregar bebida? si/no: ")

if respBebidas == "si": 
    #Mostramos las opciones de las bebidas
    print("1. Bebida Pequeña → $1.000") 
    print("2. Bebida Mediana → $1.250") 
    print("3. Bebida Grande → $2.000") 
    #Asignamos el valor de las bebidas segun el tipo seleccionado
    opcBebidas = int(input("Seleccione una opción: "))
    #Asignamos el valor de las bebidas segun el tipo seleccionado
    if opcBebidas == 1:
        valorBebidas = 1000
    elif opcBebidas == 2:
        valorBebidas = 1250
    elif opcBebidas == 3:
        valorBebidas = 2000
    #preguntamos la cantidad de bebidas
    cantBebidas = int(input("Ingrese la cantidad de bebidas que desea: "))
    #Calculamos el monto total de las bebidas multiplicando el valor segun el tipo por la cantidad
    totalBebidas = cantBebidas * valorBebidas
    

#Si pertenece a DUOC calculamos el descuento 
if pertenece == 1:
    descuento = totalEntradas * 0.30
    #restamos el descuento al total Entradas
    totalEntradas = totalEntradas - descuento
    print("Se le hizo un descuento del 30% por pertenecer")


#Obtenemos el total sumando las palomitas con las bebidad y las entradas.
# totalPalomitas y totalBebidas tienen que estar inicializadas en 0 por si acaso deciden no llevar ninguna de las dos estas variables tengan un valor. 
totalAPagar = totalPalomitas + totalBebidas + totalEntradas

print("El total a pagar es de: ", totalAPagar)

#solicitamoe el efectivo
efectivo = float(input("Ingrese el efectivo: "))

#verificamos los casos para el vuelto. 
if efectivo > totalAPagar:
    vuelto = efectivo - totalAPagar
    print("Su vuelto es de: ", vuelto)
elif totalAPagar > efectivo:
    print("Le falta dinero, GUARDIAS")
else:
    print("Monto exacto, gracias")



