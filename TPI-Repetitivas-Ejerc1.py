#Ejercicio 1 - Caja del Kiosco
cliente = input("Coloque su nombre: ").strip()
while not cliente.isalpha():
    print("Por favor ingrese solo letras")
    cliente = input("Coloque su nombre: ").strip()   

cantidad_productos = input("Ingrese la cantidad de productos que desea agregar: ").strip()
while not cantidad_productos.isdigit() or int(cantidad_productos) == 0:
    print("Por favor ingrese solo números positivos")
    cantidad_productos = input("Ingrese la cantidad de productos que desea agregar: ").strip()

total_con_descuento= 0
total_sin_descuento= 0
ahorro_total= 0

for i in range(int(cantidad_productos)):
    precio_str= input(f"Coloque el precio del producto {i+1}: ").strip()
    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Por favor ingrese solo números positivos")
        precio_str= input(f"Coloque el precio del producto {i+1}: ").strip()

    precio= int(precio_str)
    total_sin_descuento += precio

    while True:
        desicion= input("Dicho producto tiene descuento? (S/N): ").upper()
        match desicion:
            case "S":
                precio_descuento= precio*0.90
                total_con_descuento += precio_descuento
                ahorro= precio - precio_descuento
                ahorro_total += ahorro
                break
            case "N":
                total_con_descuento += precio
                break
            case _:
                print("Por favor ingrese una de las dos opciones disponibles")

promedio_producto=(total_con_descuento) / int(cantidad_productos)

print(f"""
Cliente: {cliente}
Total sin descuento: {total_sin_descuento}
Total con descuento: {total_con_descuento:.2f}
Ahorro total: {ahorro_total:.2f}
Promedio por producto: {promedio_producto:.2f}""")
