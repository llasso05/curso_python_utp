
# Inicializamos una lista vacía para almacenar las calificaciones ingresadas por el usuario.
calificaciones = []

# Iniciamos un bucle infinito que permitirá al usuario ingresar múltiples calificaciones.
while True:
    # Solicitamos al usuario que ingrese una calificación o que escriba 'fin' para terminar.
    entrada = input("Introduce una calificación o escribe 'fin' para terminar: ")
    # Si el usuario escribe 'fin', salimos del bucle.
    if entrada.lower() == 'fin':
        break

    # Intentamos convertir la entrada del usuario a un número de punto flotante.
    try:
        calificacion = float(entrada)
        # Si la conversión es exitosa, añadimos la calificación a la lista.
        calificaciones.append(calificacion)
        # Si la conversión falla, atrapamos la excepción y notificamos al usuario.
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

    # Verificamos si la lista de calificaciones está vacía.
    if not calificaciones:
        # Si está vacía, informamos al usuario y el programa termina aquí.
        print("No se ingresaron calificaciones.")
    
    else:
        # Si la lista no está vacía, calculamos el promedio de las calificaciones.
        try:
            promedio = sum(calificaciones) / len(calificaciones)
            # Mostramos el promedio con dos decimales de precisión.
            print(f"El promedio de las calificaciones es: {promedio:.2f}")
            # Añadimos un manejo de excepción por si ocurre algún otro error inesperado.
        except ZeroDivisionError:
            print("No hay calificaciones para calcular el promedio.")

