# 2)	Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada los nombres y apellidos.

# Crear listas vacías para nombres y apellidos
nombres = []
apellidos = []

# Solicitar nombres y apellidos de la primera persona
nombre1 = input("Ingrese el nombre de la primera persona: ")
apellido1 = input("Ingrese el apellido de la primera persona: ")
nombres.append(nombre1)
apellidos.append(apellido1)

# Solicitar nombres y apellidos de la segunda persona
nombre2 = input("Ingrese el nombre de la segunda persona: ")
apellido2 = input("Ingrese el apellido de la segunda persona: ")
nombres.append(nombre2)
apellidos.append(apellido2)

# Solicitar nombres y apellidos de la tercera persona
nombre3 = input("Ingrese el nombre de la tercera persona: ")
apellido3 = input("Ingrese el apellido de la tercera persona: ")
nombres.append(nombre3)
apellidos.append(apellido3)

# Mostrar los nombres y apellidos de forma ordenada
print("Nombres y Apellidos de forma ordenada:")
for i in range(3):
    print(f"{nombres[i]} {apellidos[i]}")

#Tambien se podrian mostrar accediendo a la posicion del elemento directamente en forma manual
# print(nombres[0], apellidos[0])
# print(nombres[1], apellidos[1])
# print(nombres[2], apellidos[2])
