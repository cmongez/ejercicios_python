# 3)	Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower() y upper() ) .
# Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.

# Crear una lista vacía para almacenar los nombres
nombres = []

# Bucle para agregar nombres
while True:
    # Solicitar un nombre al usuario
    nombre = input("Ingrese nombre: ")
    nombres.append(nombre)
    
    # Preguntar si desea agregar otro nombre
    while True:
        respuesta = input("¿Desea agregar otro nombre? (si/no): ").lower()
        
        if respuesta == "no":
            break
        elif respuesta == "si":
            break
        else:
            print("Ingresa una respuesta válida (si/no).")
    
    # Si la respuesta es "no", salir del bucle principal
    if respuesta == "no":
        break

# Inicializar nombreMasCorto con el primer elemento de la lista
nombreMasCorto = nombres[0]

# Encontrar el nombre con la menor cantidad de caracteres
for nombre in nombres:
    if len(nombre) < len(nombreMasCorto):
        nombreMasCorto = nombre

# Mostrar el nombre más corto
print("El nombre más corto es: ", nombreMasCorto)

# Eliminar el nombre más corto de la lista
nombres.remove(nombreMasCorto)

# Mostrar la lista de nombres después de eliminar el nombre con menos caracteres
print("Lista de nombres después de eliminar el nombre con menos caracteres:")
print(nombres)
