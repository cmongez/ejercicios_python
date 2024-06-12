usuarios=[["cesar","123"],
          ["Pauli","456"],
          ["Pri","789"]
          ]

while True:
    print("1. Inicio sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")
    opcion=int(input("Elija una opción"))
    

    if opcion ==1:
        print("iniciar sesion")
        nombreUsuario=input("nombre de usuario")
        contraseña=input("ingrese la contraseña")
        for elemento  in usuarios:
            print(elemento[0])
            if elemento[0] == nombreUsuario and elemento[1] == contraseña:
                print("usted a iniciado sesion con éxito")
                break


    elif opcion==2:
        print("Registar usuario")
        nombreUsuario=input("nombre de usuario")
        contraseña=input("ingrese la contraseña")
        usuario=[nombreUsuario,contraseña]
        usuarios.append(usuario)
        print(usuarios)
    elif opcion==3:
        print("eliminar usuario")
        nombreUsuario=input("nombre de usuario")
        for elemento in usuarios:
            if elemento[0]==nombreUsuario:

    elif opcion==4:
        print("Salir") 
        break
