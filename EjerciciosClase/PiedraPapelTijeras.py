import random

opciones = ["piedra", "papel", "tijera"]
jugador1=0
jugador2=0

total_rondas = int(input("¿Cuántas rondas deseas jugar?: "))

for ronda in range(1, total_rondas + 1):
    print(f"Ronda: {ronda} de {total_rondas}")

    jugador = input("Jugadora (piedra,papel,tijera): ").lower()

    while jugador not in opciones:

        jugador = input("Opción inválida. Elige piedra, papel o tijera: ").lower()

    compu= random.choice(opciones)
    
    print(f"Jugadora: {jugador.capitalize()}")
    print(f" Computadora: {compu.capitalize()}")

    if jugador == compu:
        print("Empate")
    elif (
        (jugador == "piedra" and compu == "tijera") or
        (jugador == "papel" and compu == "piedra") or
        (jugador == "tijera" and compu == "papel")

    ):
        
        jugador1 += 1
        print("Jugadora ha ganado esta ronda ")
     
    else:
        jugador2 += 1
        print("Computadora ha ganado esta ronda")

        
    print(f"Puntaje: {jugador1} (Jugador) - {jugador2} (Computadora)")
    print(f"Rondas restantes: {total_rondas - ronda}")


print("   Resultado Final  ")
if jugador1 > jugador2:
    print("¡El jugador ha ganado el juego!")
elif jugador2 > jugador1:
   print("La computadora ha ganado el juego.")

else:
    print("El juego terminó en empate.")