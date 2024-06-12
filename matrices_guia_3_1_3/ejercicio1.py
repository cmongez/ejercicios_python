# 1. Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for, mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:

# 	 3	10	 4	16
# 	 1	 7 	 8	-7
# 	 9	-1	 3	 9

arregloNumerico = []

for i in range(3):
    fila = []
    for j in range(4):
        numero = int(input("Ingrese el numero: "))
        fila.append(numero)
    arregloNumerico.append(fila)

for filaArreglo in arregloNumerico:
    for num in filaArreglo:
        print(num, end="   ")
    print()