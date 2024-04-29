# Ejercicio 6:Ingrese 3 números enteros por teclado e indique ¿cuántos son menores a cero?

#Pedimos y guardamos los 3 numeros en su variable respectiva
print("Ingrese 3 números enteros")
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

#Creamos un contador para llevar la cuenta de cuantos numeros son menores a cero
cont = 0

#validamos que numeros son menores a cero y aumentamos el contador en caso de serlo. 
if num1 < 0:
    cont = cont + 1
else:
    if num2 < 0:
        cont = cont + 1
    else:
        if num3 < 0:
            cont = cont + 1

#Imprimimos el resultado
print("Son en total ", cont, "menores a 0")
