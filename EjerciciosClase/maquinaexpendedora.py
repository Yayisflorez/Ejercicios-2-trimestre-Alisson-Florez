total = 0

print("selecciona una opcion")
print("1. Café ($3.000)")
print("2. Té ($2.500)")
print("3. Jugo ($3.500)")
print("0. Finalizar compra")

while True:
    opcion = int(input("Seleccione una opción (0 para salir): "))

    match opcion:
        case 1:
            print("Café seleccionado - Valor: $3.000")
            total += 3000
        case 2:
            print("Té seleccionado - Valor: $2.500")
            total += 2500
        case 3:
            print("Jugo seleccionado - Valor: $3.500")
            total += 3500
        case 0:
            print("Compra finalizada.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")

print(f"Total a pagar: ${total}")