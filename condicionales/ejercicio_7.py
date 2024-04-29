# Ejercicio 7:Se pide identificar el tipo de triángulo, para ello, ingrese el lado a, b y c, luego indique si es isósceles, equilátero o rectángulo.
# Es isósceles, si dos lados son iguales.
# Es equilátero, si sus tres lados son iguales.
# Es escaleno, si sus tres lados son diferentes.

#Solicitamos los lados del triangulo.
print("Ingrese 3 números enteros")
ladoA = int(input("Ingrese el lado a: "))
ladoB = int(input("Ingrese el lado b: "))
ladoC = int(input("Ingrese el lado c: "))

#Creamos un contador para ir contando cuantos lados iguales tiene el triangulo
cont = 0

if ladoA == ladoB:
    cont = cont + 1

if ladoB == ladoC:
    cont = cont + 1

if ladoC == ladoA:
    cont = cont + 1

#Si el contador es cero quiere decir que no se cumplio ninguna condición, po lo tanto el triagulo no tiene ningun lado igual
if cont == 0:
    print("El triangulo es escaleno")
#Si el contador es 1 quiere decir que al menos uno de nuestras condiciones se cumplio y por lo tanto al menos 2 lados son iguales.
elif cont == 1:
    print("El triangulo es isosceles")
#Si el contador es 3 quiere decir que todos los condicionales se cumplieron y que todos los lados son iguales.
elif cont == 3:
    print("El triangulo es equilatero")
