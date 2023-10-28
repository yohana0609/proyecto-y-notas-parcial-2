from guizero import App, Box, PushButton, TextBox, Text, ListBox, Window
#Se importan los módulos necesarios de la biblioteca "guizero" para crear la interfaz.

app = App("Punto de Venta")
#Se crea una instancia de la aplicación con el nombre de "Punto de Venta".
productos = []
#Se crea una lista vacía llamada productos para almacenar los detalles de los productos.

def agregar_producto():
    codigo = int(codigo_input.value)
    if any(producto[0] == codigo for producto in productos):
        detalle_producto.value = "Ya existe un producto con este código."
    else:
        descripcion = descripcion_input.value
        ubicacion = ubicacion_input.value
        precio = float(precio_input.value)
        cantidad = int(cantidad_input.value)
        proveedor = proveedor_input.value
        productos.append((codigo, descripcion, ubicacion, precio, cantidad, proveedor))
        actualizar_lista_productos()
        detalle_producto.value = "Producto agregado correctamente"
#Esta función se llama cuando se presiona el botón "Agregar Producto". 
#Recopila información sobre un nuevo producto ingresado por el usuario y lo agrega a la lista productos.

def eliminar_producto():
    seleccion = lista_productos.value
    if seleccion is not None:
        productos[:] = [producto for producto in productos if producto[0] != seleccion]
        actualizar_lista_productos()
        detalle_producto.value = "Producto eliminado"
    else:
        detalle_producto.value = "Selecciona un producto para eliminar"
#Esta función se llama cuando se presiona el botón "Eliminar Producto". 
#Permite al usuario seleccionar un producto de una lista y eliminarlo de la lista productos.

def actualizar_lista_productos():
    lista_productos.clear()
    for producto in productos:
        lista_productos.append(producto[0])
#Esta función actualiza la lista de productos en la interfaz,mostrando solo los códigos de los productos.

def mostrar_detalle_producto():
    seleccion = lista_productos.value
    detalles = ""
    for producto in productos:
        if producto[0] == seleccion:
            detalles = f"Descripción: {producto[1]}\nUbicación: {producto[2]}\nPrecio: $ {producto[3]}\nCantidad: {producto[4]}\nProveedor: {producto[5]}"
            break
    detalle_producto.value = detalles
#Muestra los detalles de un producto seleccionado por el usuario en un cuadro de texto en la interfaz.

def actualizar_producto():
    seleccion = lista_productos.value
    if seleccion is not None:
        for i, producto in enumerate(productos):
            if producto[0] == seleccion:
                productos[i] = (
                    int(codigo_input.value),
                    descripcion_input.value,
                    ubicacion_input.value,
                    float(precio_input.value),
                    int(cantidad_input.value),
                    proveedor_input.value
                )
                detalle_producto.value = "Producto actualizado"
                break
    else:
        detalle_producto.value = "Selecciona un producto para actualizar"
#Permite al usuario actualizar la información de un producto existente seleccionado en la lista.


registro_box = Box(app, layout="grid")
detalle_box = Box(app, layout="grid")
#Se crean dos cajas para organizar los elementos de la interfaz de usuario
#una para el registro de productos
#otra para mostrar detalles y acciones relacionadas con los productos.

def crear_campo_etiqueta(row, label):
    Text(registro_box, text=label, grid=[0, row])
    return TextBox(registro_box, grid=[1, row])
#Esta función se utiliza para crear etiquetas de campo y campos de entrada en la interfaz gráfica.

codigo_input = crear_campo_etiqueta(0, "Código:")
descripcion_input = crear_campo_etiqueta(1, "Descripción:")
ubicacion_input = crear_campo_etiqueta(2, "Ubicación:")
precio_input = crear_campo_etiqueta(3, "Precio:")
cantidad_input = crear_campo_etiqueta(4, "Cantidad:")
proveedor_input = crear_campo_etiqueta(5, "Proveedor:")
#Se crean campos de entrada para el código, etc.

codigo_input.text_color = "blue"
descripcion_input.text_color = "green"
ubicacion_input.text_color = "purple"
precio_input.text_color = "blue"
cantidad_input.text_color = "green"
proveedor_input.text_color = "purple"
#cambia el color del texto dentro de los recuadros

agregar_button = PushButton(registro_box, text="Agregar Producto", command=agregar_producto, grid=[0, 6, 2, 1])
eliminar_button = PushButton(registro_box, text="Eliminar Producto", command=eliminar_producto, grid=[0, 7, 2, 1])
actualizar_button = PushButton(registro_box, text="Actualizar Producto", command=actualizar_producto, grid=[0, 8, 2, 1])
#Se crean botones respectivamente para realizar cada acción.

agregar_button.bg = "pink"
eliminar_button.bg = "pink"  
actualizar_button.bg = "pink"  
# Cambiar el color de fondo de los botones

lista_productos = ListBox(detalle_box, command=mostrar_detalle_producto, grid=[0, 0])
detalle_producto = Text(detalle_box, grid=[1, 0])
#Se crea una lista de productos y un cuadro de texto para mostrar los detalles del producto.

app.display()
#Se inicia la aplicación y se muestra la interfaz gráfica al usuario.