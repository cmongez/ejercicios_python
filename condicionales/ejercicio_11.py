# Ejercicio 11: 
# Usted es el encargado de generar un sistema de compra, el cual 
# consiste en: 
# Seleccionar si desea el producto o no, en el caso de llevar el producto, el 
# total de la compra debe ir aumentando dependiendo de cuantos 
# productos lleve y el valor de cada uno de ellos, también debe ingresar si 
# el cliente es preferencial o no, en el caso de ser preferencial, al final al 
# momento de pagar se debe realizar un descuento del 25% del total de la 
# compra, finalmente se solicita que ingrese el efectivo, debe calcular 
# cuánto es el vuelto del cliente en el caso de que el efectivo sea mayor al 
# total a pagar, del caso contrario verificar que el monto no sea inferior al 
# total a pagar o enviar una salida por pantalla que diga “ Dinero 
# insuficiente, Guardias!”. 
# Los productos detallados son los siguientes: 
# Agua → $ 600 
# Azúcar→ $1200 
# Aceite → $1500 
# Arroz → $1250 
# Fideos → $ 790 
# Bebida→ $1780 
# Chocolate → $2500 
# Pan molde → $1340


totalVenta = 0

#Realizamos la pregunta uno a uno de si va a llevar el producto y de ser "si", solicitamos la cantidad a llevar

#***********AGUA***************
print("Producto: Agua → $ 600 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantas agua desea llevar?: "))
    #calculamos el total del producto multiplicando la cantidad por el precio
    #aca utilizaremos las variables cantidad y totalProducto para todos los condicionales ya que su valor lo vamos a estar sobreescribiendo siempre.
    totalProducto = cantidad * 600
    
    #Aca acumulamos en total ventas el total que llevamos con el total dle producto actual y esto se repite para todos los productos.
    totalVenta = totalVenta + totalProducto

#***********Azúcar***************
print("# Azúcar→ $1200 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantas azucar desea llevar?: "))
    totalProducto = cantidad * 1200
    totalVenta = totalVenta + totalProducto

#***********Aceite***************
print("Producto: Aceite → $ 1500 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantos aceite desea llevar?: "))
    totalProducto = cantidad * 1500
    totalVenta = totalVenta + totalProducto

print("Producto: Arroz → $ 1250 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantos arroz desea llevar?: "))
    totalProducto = cantidad * 1250
    totalVenta = totalVenta + totalProducto

print("Producto: Fideos → $ 790 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantos fideos desea llevar?: "))
    totalProducto = cantidad * 790
    totalVenta = totalVenta + totalProducto

print("Producto: Bebida → $ 1780 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantas bebidas desea llevar?: "))
    totalProducto = cantidad * 1780
    totalVenta = totalVenta + totalProducto


print("Producto: Chocolate → $ 2500 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantos chocolates desea llevar?: "))
    totalProducto = cantidad * 2500
    totalVenta = totalVenta + totalProducto

print("Producto: Pan de molde → $ 1340 ")
respuesta = input("¿Desea llevar el producto? responda si/no: ")

if respuesta == "si":
    cantidad = int(input("¿Cuantos pan de molde desea llevar?: "))
    totalProducto = cantidad * 1340
    totalVenta = totalVenta + totalProducto

#Preguntamos si el cliente es preferencial o no
esPreferencial = input("¿Es un cliente preferencial? responda si/no:")

#Si es preferencial calculamos y aplicamos el descuento
if esPreferencial == "si":
    #calculamos el descuento del 25%
    descuento = totalVenta * 0.25
    #aplicamos el descuento
    totalVenta = totalVenta - descuento

#Imprimimos el total de la venta
print("El total de la venta es de: ", totalVenta)

#Solicitamos el efectivo
efectivo = float(input("Ingrese la cantidad de efectivo: "))

#Si el efectivo es mayor que la venta calculamos el vuelto
if efectivo > totalVenta:
    vuelto = efectivo - totalVenta
    print("Su vuelto es de : ", vuelto)
    print("Gracias por su compra")
#Si el efectivo es menor al total de la venta llamamos a lo contrario
elif efectivo < totalVenta:
    print("Dinero insuficiente, Guardias!")

#Por ultimo sabemos que si no es mayor ni menor entonces es igual
else:
    print("Gracias por su compra")



