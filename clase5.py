# function to add student score
def agregar_nota(cedula, nota):
    # ruta del archivo
    filename = f"nota_estudiante_{cedula}.txt"
    # try catch para escribir el archivo
    try:
        with open(filename, "a") as file:
            file.write(str(nota) + "\n")
    except IOError: # catch open file errors
        print("Error: No se puede escribir el archivo.")

# main function
def main():
    # main loop
    while True:

        cedula = input("Ingrese numero de cedula o escriba 'Salir' para cerrar la ventana: ")
        # progam exit
        if cedula.lower() == 'salir':
            break
        # try catch cedula
        try:
            cedula = str(cedula)
        except ValueError:
            print('Inserte un numero de cedula correcto. ')
            continue

        nota = input('Ingrese nota del estudiante: ')
        # try catch nota
        try:
            nota = float(nota)
        except ValueError: # catch type conversion errors
            print("Error: Por favor ingrese una nota correcta.")
            continue
            
        agregar_nota(cedula, nota)

if __name__ =="__main__":
    main()