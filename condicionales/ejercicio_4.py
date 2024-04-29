# Ejercicio 4: Ingrese por teclado un número entero mayor a 1 y menor a 101 por teclado, luego indique si es par o impar.
num = int(input("Ingrese por teclado un número entero mayor a 1 y menor a 101: "))

if num > 1 and num < 101:
    resultado = num%2

    if resultado==0:
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("El numero debe ser mayor a 1 y menor a 101")
