from Matematicas.circulo import areaCirculo, perimetroCirculo
from Matematicas.rectangulo import areaRectangulo, perimetroRectangulo
from Matematicas.triangulo import areaTriangulo, perimetroTriangulo

def main():
    while True:
        figura = input('Seleccione entre Circulo, Triangulo o Rectangulo ')
        if figura  == 'Circulo':
            radioCirculo = int(input('Inserte Radio del Circulo: '))
            print(type(radioCirculo))
            areaFinal = areaCirculo(radioCirculo)
            perimetroFinal = perimetroCirculo(radioCirculo)
            print(f'El area del circulo es {areaFinal} y el perimetro {perimetroFinal}')
            break

        elif figura == "Triangulo":
            longitudTriangulo = int(input('Inserte Longitud del lado mas largo del Triangulo: '))
            alturaTriangulo = int(input('Inserte Altura del Triangulo: '))
            areaFinal = areaTriangulo(longitudTriangulo, alturaTriangulo)
            print("Inserte las longitudes de los lados restantes:")
            lado2 = int(input("longitud del lado 2 "))
            lado3 = int(input("longitud del lado 3 "))
            perimetroFinal = perimetroTriangulo(longitudTriangulo, lado2, lado3)
            print(f'El area del triangulo es {areaFinal} y el perimetro {perimetroFinal}')
            break

        elif figura == "Rectangulo":
            largoRectangulo = int(input('Inserte Largo del Rectangulo: '))
            anchoRectangulo = int(input('Inserte Ancho del Rectangulo: '))
            areaFinal = areaRectangulo(largoRectangulo, anchoRectangulo)
            perimetroFinal = perimetroRectangulo(largoRectangulo, anchoRectangulo)
            print(f'El area del triangulo es {areaFinal} y el perimetro {perimetroFinal}')
            break

        else:
            print("Por favor introduzca una opcion entre 'Rectangulo', 'Triangulo' o 'Circulo' ")
            continue

if __name__ == "__main__":
    main()