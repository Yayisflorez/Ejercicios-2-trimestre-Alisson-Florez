import random

ganadas = 0
perdidas = 0
print(" Juego: persona vs La Banca ")
print("Reglas: Si tu carta es mayor que la de la banca, ganas la ronda.")
print("pierdes 3 veces, ganas 5 veces o decides retirarte.")

while True:
    if ganadas >= 5:
        print("¡Felicidades! Ganaste el juego")
        break
    elif perdidas >= 3:
        print("Has perdido el juego ")
        break
     
    print("¿Deseas jugar esta ronda?")  
    print("1) si")
    print("2) no")
    decision=int(input())

    if decision == 2:
        print("Te has retirado del juego.")
        break
    elif decision == 1:
        carta_jugador = random.randint(1, 13)
        carta_banca = random.randint(1, 13)
        print(f"Tu carta es: {carta_jugador}")
        print(f"Carta de la banca: {carta_banca}")

        
        if carta_jugador > carta_banca:
            ganadas += 1
            print("¡Ganaste esta ronda!")
        elif carta_jugador < carta_banca:
            perdidas += 1
            print("Perdiste esta ronda")
        else:
            print("Empate. No cuenta como ganada ni perdida.")

            print(f"Rondas ganadas: {ganadas}, Rondas perdidas: {perdidas}")
    else:
        print("Opción no válida. Escribe '1' para jugar o '2' para salir.")