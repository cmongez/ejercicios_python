datos_personales = []
while True:
    nombre = input("Ingrese un nombre: ")
    if nombre.lower() == "fin":
        break
    edad = int(input("Ingrese la edad: "))
    datos_personales.append((nombre, edad))
    edades_unicas = {edad for _, edad in datos_personales}
    print("Edades únicas presentes:", edades_unicas)