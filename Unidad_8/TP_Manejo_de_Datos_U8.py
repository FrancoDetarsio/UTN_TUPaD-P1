# Práctica Manejo de Datos U8


# 1. Crear archivo inicial con productos:

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120,30\n")
    archivo.write("Cartuchera,300,10\n")
    archivo.write("Carpeta,220,15\n")


# 2. Leer y mostrar productos:

with open("productos.txt", "r") as archivo:

    for linea in archivo: # cada linea se va a pasar a formato de lista, por lo cual podemos invocar sus elementos con indice
        linea = linea.strip().split(",")
        print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")


# 3. Agregar productos desde teclado:

producto = input("Ingrese el nombre del producto que quiera agregar: ").strip().capitalize() # .capitalize() hará solo la primera letra mayuscula
precio = input(f"Ingrese el precio para {producto}: ").strip()
cantidad = input(f"Ingrese la cantidad existente de {producto}: ").strip()

with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto},{precio},{cantidad}\n")


# 4. Cargar productos en una lista de diccionarios:

productos = []

with open("productos.txt", "r") as archivo:

    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        item = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        productos.append(item)

for i in productos:
    print(i)

print("==================================================\n")


# 5. Buscar producto por nombre:

nombre = input("Ingrese el el nombre de un producto que quiera consultar: ").strip().capitalize() # .capitalize() hará solo la primera letra mayuscula, para poder hacer match con la lista

bandera = '' # bandera que usaremos en caso que no se encuentre el producto ingresado

for i in productos:
    if i['nombre'] == nombre:
        print(f"Nombre: {i['nombre']} | Precio: {i['precio']} | Cantidad: {i['cantidad']}\n")
        bandera = '+'

if bandera == '':
    print("El producto ingresado no existe en la lista.\n")


# 6. Guardar los productos actualizados:

with open("productos.txt", "w") as archivo:
    # pasamos linea por linea de la lista usando su indice y su key
    for i in productos:
        archivo.write(f"{i['nombre']}, {i['precio']}, {i['cantidad']}\n")


#  Última lectura para comprobar que se haya guardado correctamente
with open("productos.txt", "r") as archivo:

    for linea in archivo:
        linea = linea.strip().split(",")
        print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")