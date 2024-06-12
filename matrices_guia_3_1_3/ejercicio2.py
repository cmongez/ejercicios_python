# 2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
# Una vez completado, mostrar la siguiente información:
# ●	Número de elementos “amarillo”.
# ●	Número de elementos “rojo”.
# ●	Número de elementos “Naranja”.
# ●	Número de elementos “Verde”.
# ●	Número de elementos “Blanco”

listaNumeros = [[
    ["Amarillo", "Verde", "Blanco"],
    ["Amarillo", "Verde", "Blanco"],
    ["Amarillo", "Verde", "Blanco"],
], [
    ["Amarillo", "Rojo", "Naranja"],
    ["Amarillo", "Rojo", "Naranja"],
    ["Amarillo", "Rojo", "Naranja"],
], [
    ["Rojo", "Naranja", "Blanco"],
    ["Rojo", "Naranja", "Blanco"],
    ["Rojo", "Naranja", "Blanco"],
]]

contAmarillo = 0
contRojo = 0
contNaranja = 0
contVerde = 0
contBlanco = 0

for capa in listaNumeros:
    for fila in capa:
        for color in fila:

            if color == "Amarillo":
                contAmarillo = contAmarillo + 1
            elif color == "Rojo":
                contRojo = contRojo + 1
            elif color == "Naranja":
                contNaranja = contNaranja + 1
            elif color == "Verde":
                contVerde = contVerde + 1
            elif color == "Blanco":
                contBlanco = contBlanco + 1

print("Número de elementos Amarillos: ", contAmarillo)
print("Número de elementos Rojos: ", contRojo)
print("Número de elementos Naranja: ", contNaranja)
print("Número de elementos Verdes: ", contAmarillo)
print("Número de elementos Blancos: ", contBlanco)

            
