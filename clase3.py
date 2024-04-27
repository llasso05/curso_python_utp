"""
Escribir un program en python que le pida al usuario ingresar datos
personales (nombre, apellido, cedula, correo electronico y numero de 
telefono) de N cantidad de personas, el usuario decide cuando deja de
anadir mas registros.
"""



registro = []  # lista vacia
datos = ['Nombre', 'Apellido', 'Cedula', 'Correo Electronico', 'Numero de Telefono']

while True:
    nuevo_registro = input("Deseas agregar un registro? ('Y', 'N') ")

    if nuevo_registro in ("Y", "N"):
        if nuevo_registro == 'N':
            print(registro)
            break

        elif nuevo_registro == 'Y':
            record = {}  # diccionario vacio
            for i in datos:
                llave = i
                item = input(f'Ingrese {i} ')
                record[i] = item

            registro.append(record)  # Append the record 
            print(registro)

    else:
        print('Por favor utiliza Y o N para responder')