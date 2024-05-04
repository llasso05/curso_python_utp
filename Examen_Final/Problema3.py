# Inicialización del diccionario para la agenda telefónica.
agenda = {}

def añadir_contacto(nombre, telefono):
    """
    Añade o actualiza un contacto en la agenda.
    Args:
    nombre (str): Nombre del contacto.
    telefono (str): Teléfono del contacto.
    """
    agenda[nombre] = telefono
    print(f"Contacto {nombre} añadido/actualizado con éxito.")

def buscar_contacto(nombre):
    """
    Busca un contacto por su nombre y muestra su número de teléfono.
    Args:
    nombre (str): Nombre del contacto a buscar.
    """
    try:
        print(f"El número de {nombre} es {agenda[nombre]}")
    except KeyError:
        print(f"Contacto {nombre} no encontrado en la agenda.")

def eliminar_contacto(nombre):
    """
    Elimina un contacto de la agenda.
    Args:
    nombre (str): Nombre del contacto a eliminar.
    """
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"Contacto {nombre} no encontrado en la agenda.")

# Añadiendo algunos contactos
añadir_contacto('Alice', '123-456-7890')
añadir_contacto('Bob', '987-654-3210')
# Buscando un contacto
buscar_contacto('Alice')
# Eliminando un contacto
eliminar_contacto('Bob')
# Intentando eliminar un contacto que no existe
eliminar_contacto('Charlie')
