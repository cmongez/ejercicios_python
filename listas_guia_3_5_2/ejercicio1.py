# 1) Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla.

#Creamos una lista vacia donde guardaremos los nombres
nombres = []

#Solicitamos uno a uno los tres nombres
nombre1 = input("Ingrese el primer nombre: ")
#Usamos el append para agregar uno a uno los nombres a la lista
nombres.append(nombre1)
nombre2 = input("Ingrese el segundo nombre: ")
nombres.append(nombre2)
nombre3 = input("Ingrese el tercer nombre: ")
nombres.append(nombre3)

#Inicializamos una variable que a futuro guardara el nombre mas largo
nombreMasLargo = ''
#Iteramos con un for de range 3 ya que sabemos que son solo 3 nombres
for i in range(3):
    #Si el largo del nombre iterado es mayor que el largo del nombreMarLargo quiere decir que el nombre iterado es ahora el nombre mas largo
    if len(nombres[i])> len(nombreMasLargo):
        nombreMasLargo = nombres[i]

print("El nombre mas largo de la lista es: ", nombreMasLargo)
