print("#-----------------------------#")
print("#--| sistema de descuentos |--#")
print("#-----------------------------#")
print("#--| 1) cliente regular    |--#")
print("#--| 2) cliente premium    |--#")
print("#--| 3) cliente vip        |--#")
print("#-----------------------------#")
opcion = input("seleccione el tipo de cliente: ")
precio = float(input("ingrese el precio del producto: "))
if precio < 0:
    print("error: el precio no puede ser negativo")
elif opcion == "1":
    descuento = 0.05
    total = precio - (precio * descuento)
    print("descuento aplicado: 5%")
    print("precio final:", int(total) if total.is_integer() else total)
elif opcion == "2":
    descuento = 0.10
    total = precio - (precio * descuento)
    print("descuento aplicado: 10%")
    print("precio final:", int(total) if total.is_integer() else total)
elif opcion == "3":
    descuento = 0.20
    total = precio - (precio * descuento)
    print("descuento aplicado: 20%")
    print("precio final:", int(total) if total.is_integer() else total)
else:
    print("opcion no valida")