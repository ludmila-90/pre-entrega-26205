lista_productos = []

opcion = ""

while opcion != "5":
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nuevo_producto = input("Nombre del producto: ").strip().title()
        lista_productos.append(nuevo_producto)
        print(f"Se agregó {nuevo_producto} exitosamente")

    elif opcion == "2":
        if len(lista_productos) == 0:
            print("No hay productos guardados.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")
            for producto in lista_productos:
                print(f"{producto}")
    
    elif opcion == "3":
        producto_buscado = input("Producto buscado: ").strip().title()
        if producto_buscado in lista_productos:
            print("\n--- PRODUCTO ENCONTRADO ---")
            print(f"{producto_buscado}")
        else:
            print("Producto inexistente.")

    elif opcion == "4":
        producto_a_eliminar = input("Producto a eliminar: ").strip().title()
        if producto_a_eliminar in lista_productos:
            lista_productos.remove(producto_a_eliminar)
            print("\n--- PRODUCTOS ELIMINADOS ---")
            print(f"{producto_a_eliminar} fue eliminado de la lista.")
        else:
            print("Producto inexistente.")
    
    elif opcion == "5":
        print("Gracias por utilizar nuestro sistema.")

    else:
        print("Opción inexistente, vuelva a intentar.")