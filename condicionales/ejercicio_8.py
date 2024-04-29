# Ejercicio 8:  
# La empresa dedicada a la venta de zapatos, ha decidido 
# fabricar zapatos de hombre para la venta online. Los zapatos 
# tienen un valor de $20.000 (cualquier número), pero podría 
# variar según la demanda. 
# Si la compra es igual o superior a $40.000 el envío es gratis, 
# en caso contario, debe cancelar un monto extra de $3.000 

# Determine el total a pagar por una persona que requiere X 
# cantidad de zapatos. 

#Solicitamos la cantidad de zapatos de la venta
cantZapatos = int(input("Ingrese la cantidad de zapatos: "))

#Multiplicamos la cantidad de zapatos por el valor para obtener el total de la venta
totalVenta = cantZapatos * 20000

#Si el total de la venta es mayor o igual que 40000 el envio es gratis, sino se le suman 3000 de envio
if totalVenta >= 40000:
    print("Su envio es gratis")
else:
    print("Se le sumaran $3000 por el envio")
    #Sumamos 3000 de envio
    totalVenta = totalVenta + 3000
#Imprimimos el resultado
print("El total de su venta es de: $",totalVenta)

