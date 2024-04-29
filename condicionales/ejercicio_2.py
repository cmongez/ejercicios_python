#Ejercicio 2:Ingrese por teclado dos números enteros positivos, súmelos y entregue su resultado

num1 = int(input("Ingrese el primer numero entero positivo: "))
num2 = int(input("Ingrese el segundo numero entero positivo: "))

if num1>0:
    if num2 >0:
        suma = num1 + num2
        print("El resultado de la suma es: ", suma)
    else:
        print("El segundo numero debe ser positivo")
else:
    print("El primer numero debe ser positivo")







