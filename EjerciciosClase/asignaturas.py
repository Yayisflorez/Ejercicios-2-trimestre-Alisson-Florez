asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

i = 0
while i < len(asignaturas):
    asignatura = asignaturas[i]
    nota = float(input(f"Introduce la nota de {asignatura}: "))
    if nota >= 3:
        asignaturas.remove(asignatura)
    else:
        i += 1 
        

print("\nTienes que repetir las siguientes asignaturas:")

for asignatura in asignaturas:
    print(asignatura)

