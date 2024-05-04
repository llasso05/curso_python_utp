equipos = []    


def añadir_equipo():
    nombre = input("Ingrese el nombre del equipo a añadir: ")
    if nombre not in equipos:
        equipos.append(nombre)
        print(f"Equipo {nombre} añadido exitosamente al torneo.")
    else:
        print(f"El equipo {nombre} ya está registrado en el torneo.")


def listar_equipos():
    if equipos:
        print("Equipos registrados en el torneo:")
    for equipo in equipos:
        print(equipo)
    else:
        print("No hay equipos registrados en el torneo.")   