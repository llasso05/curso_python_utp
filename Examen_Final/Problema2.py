# Inicializamos un diccionario vacío para el inventario.
inventario = {}

def añadir_producto(nombre, precio, cantidad):
    """
    Añade un producto al inventario o actualiza uno existente.
    Args:
    nombre (str): Nombre del producto.
    precio (float): Precio del producto.
    cantidad (int): Cantidad del producto en stock.
    """
    if nombre in inventario:
        # Si el producto ya existe, actualiza su precio y cantidad.
        inventario[nombre]['precio'] = precio
        inventario[nombre]['cantidad'] += cantidad
    else:
        # Si el producto no existe, crea una nueva entrada en el diccionario.
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}

def mostrar_inventario():
    """
    Imprime todos los productos en el inventario con sus detalles.
    """
    for nombre, detalles in inventario.items():
        print(f"Producto: {nombre}, Precio: ${detalles['precio']:.2f}, Cantidad en stock: {detalles['cantidad']}")

# Añadiendo productos al inventario
añadir_producto('Manzanas', 0.99, 100)
añadir_producto('Naranjas', 1.49, 50)
# Mostrando el inventario
mostrar_inventario()