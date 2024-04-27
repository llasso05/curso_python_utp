# Este bucle se ejecuta hasta que el usuario decide salir
while True:
    # Imprime el menú de opciones para el usuario
    print("\nAdministrador de Ventas")
    print("1. Agregar Venta")
    print("2. Mostrar Ventas Totales")
    print("3. Salir")
    
    # Solicita al usuario que ingrese una opción
    opcion = input("Elija una opción (1, 2, 3): ")

    # Si el usuario quiere agregar una venta
    if opcion == '1':
        # Solicita al usuario que ingrese el monto de la venta
        monto = float(input("Ingrese el monto de la venta: "))
        
        # Abre el archivo sales.txt en modo de escritura al final del archivo ('a' = append)
        # y escribe el monto de la venta en una nueva línea
        with open('sales.txt', 'a') as archivo:
            archivo.write(f"{monto}\n")
        
        # Confirma al usuario que la venta fue agregada
        print("Venta agregada exitosamente.")
        
    # Si el usuario quiere mostrar las ventas totales
    elif opcion == '2':
        try:
            # Abre el archivo sales.txt en modo de lectura y lee todas las líneas
            with open('sales.txt', 'r') as archivo:
                ventas = archivo.readlines()
                
                # Calcula el total sumando todas las ventas (convirtiendo cada venta a float)
                total = sum(float(venta) for venta in ventas)
        except FileNotFoundError:
            # Si el archivo sales.txt no existe, entonces el total de ventas es 0.0
            total = 0.0
        
        # Imprime el total de ventas
        print(f"Ventas totales: ${total:.2f}")
        
    # Si el usuario quiere salir
    elif opcion == '3':
        break
    else:
        # Si el usuario ingresa una opción inválida, le pide que intente de nuevo
        print("Opción inválida. Intente de nuevo.")
