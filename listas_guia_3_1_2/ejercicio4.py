# 4)	Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para confirmar la eliminación, deberán escribir la contraseña correspondiente de cada usuario.

# 1.	Inicio sesión.
# 2.	Registrar usuario
# 3.	Eliminar usuario.
# 4.	Salir.

# La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente, o un error de caso contrario.

# Crear una lista vacía para almacenar los usuarios
usuarios = []

while True:
    print("*********Menu********")
    print("1. Inicio sesión.")
    print("2. Registrar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")

    # Solicitar al usuario que seleccione una opción
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese solo números.\n")
        # Usamos continue para volver al inicio del bucle y pedir al usuario que ingrese una opción válida
        continue

    # Opción 1: Iniciar sesión
    if opcion == 1:
        print("INICIAR SESIÓN")
        nombreUsuario = input("Ingrese el nombre de usuario: ")
        contrasenia = input("Ingrese la contraseña del usuario: ")

        # Verificar si las credenciales son válidas
        inicioExitoso = False 
        for usuario in usuarios:
            if nombreUsuario == usuario[0] and contrasenia == usuario[1]:
                inicioExitoso = True
                break
        
        # Mostrar mensaje de éxito o error
        if inicioExitoso == True:
            print("Se ha iniciado sesión correctamente.\n")
        else:
            print("Usuario o contraseña incorrectos.\n")

    # Opción 2: Registrar usuario
    elif opcion == 2:
        print("REGISTRAR USUARIO")
        nombreUsuario = input("Ingrese el nombre de usuario: ")

        # Verificar si el nombre de usuario ya existe
        usuarioExistente = False
        for usuario in usuarios:
            if nombreUsuario == usuario[0]:
                usuarioExistente = True
                print("El nombre de usuario ya existe. Por favor, elija otro.\n")
                break

        # Si el usuario no existe, solicitar la contraseña y registrar al usuario
        if usuarioExistente == False:
            contrasenia = input("Ingrese la contraseña del usuario: ")
            nuevoUsuario = [nombreUsuario, contrasenia]
            usuarios.append(nuevoUsuario)
            print("Usuario registrado exitosamente.\n")
            print(usuarios)

    # Opción 3: Eliminar usuario
    elif opcion == 3:
        print("ELIMINAR USUARIO")
        nombreUsuario = input("Ingrese el nombre de usuario a eliminar: ")
        usuarioEncontrado = False

        # Buscar el usuario en la lista
        for usuario in usuarios:
            if nombreUsuario == usuario[0]:
                usuarioEncontrado = True
                contrasenia = input("Ingrese la contraseña del usuario a eliminar: ")
                # Verificar si la contraseña es correcta antes de eliminar al usuario
                if contrasenia == usuario[1]:
                    usuarios.remove(usuario)
                    print("Usuario eliminado exitosamente.\n")
                    break
                else:
                    print("Contraseña incorrecta.\n")
                    break
        # Si el usuario no se encuentra en la lista
        if usuarioEncontrado == False:
            print("Usuario a eliminar no encontrado.\n")

    # Opción 4: Salir del programa
    elif opcion == 4:
        print("Saliendo...")
        break

    # Opción inválida
    else:
        print("Seleccione una opción válida.\n")
