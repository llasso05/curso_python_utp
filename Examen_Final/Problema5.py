
# gestion_cuenta.py
from cuenta.cuenta import Cuenta

def main():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = Cuenta(titular)
    while True:
        print("\nMenú de Operaciones")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == '2':
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == '3':
            cuenta.mostrar_saldo()
        elif opcion == '4':
            print("Gracias por utilizar el sistema de gestión de cuentas.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")  


if __name__ == "__main__":
    main()