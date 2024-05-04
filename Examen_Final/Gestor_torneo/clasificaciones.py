# clasificaciones.py
from .partidos import resultados

def calcular_clasificaciones():
    clasificaciones = {}

    for equipo1, equipo2, resultado in resultados:
        equipo_ganador = resultado.split('-')[0]
        clasificaciones[equipo_ganador] = clasificaciones.get(equipo_ganador, 0) + 3
    
    if clasificaciones:
        print("Clasificaciones actuales:")
        for equipo, puntos in clasificaciones.items():
            print(f"{equipo}: {puntos} puntos")
    else:
        print("No hay partidos registrados para calcular clasificaciones.")