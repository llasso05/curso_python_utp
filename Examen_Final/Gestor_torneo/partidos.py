# partidos.py
resultados = []

def registrar_partido():
    equipo1 = input("Ingrese el nombre del primer equipo: ")
    equipo2 = input("Ingrese el nombre del segundo equipo: ")
    resultado = input("Ingrese el resultado del partido (ejemplo 'Tigres-Águilas'): ")
    resultados.append((equipo1, equipo2, resultado))
    print(f"Partido registrado: {equipo1} vs {equipo2}, resultado:{resultado}")

def obtener_resultados():
    if resultados:
        print("Resultados de los partidos registrados:")
        for equipo1, equipo2, resultado in resultados:
            print(f"{equipo1} vs {equipo2} - Resultado: {resultado}")
    else:
        print("No hay resultados de partidos para mostrar.")


    