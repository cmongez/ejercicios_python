# Ejercicio 1:Ingrese por teclado un número positivo y muestre su tabla de multiplicar (considere que la tabla sea de 1 a 10).

num = int(input("Ingrese por teclado un número positivo: "))

if num > 0:
    print(num,"* 1 =",num*1)
    print(num,"* 2 =",num*2)
    print(num,"* 3 =",num*3)
    print(num,"* 4 =",num*4)
    print(num,"* 5 =",num*5)
    print(num,"* 6 =",num*6)
    print(num,"* 7 =",num*7)
    print(num,"* 8 =",num*8)
    print(num,"* 9 =",num*9)
    print(num,"* 10 =",num*10)
else:
    print("El numero debe ser positivo")
