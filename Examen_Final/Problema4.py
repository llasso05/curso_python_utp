# test_torneo.py
from Gestor_torneo import equipos, partidos, clasificaciones

def menu():
    while True:
        print("\nMenú del Gestor del Torneo")
        print("1. Añadir equipo")
        print("2. Listar equipos")
        print("3. Registrar partido")
        print("4. Mostrar resultados de partidos")
        print("5. Calcular clasificaciones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            equipos.añadir_equipo()
        elif opcion == '2':
            equipos.listar_equipos()
        elif opcion == '3':
            partidos.registrar_partido()
        elif opcion == '4':
            partidos.obtener_resultados()
        elif opcion == '5':
            clasificaciones.calcular_clasificaciones()
        elif opcion == '6':
            print("Saliendo del gestor del torneo.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()