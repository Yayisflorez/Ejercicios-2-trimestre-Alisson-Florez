import random
import time

dinero = 0
recompensa_por_pregunta = 500000
comodines_disponibles = {
    "1": True,
    "2": True,
    "3": True,
}

preguntas = {

    1: [
        {'pregunta': '¿Qué color resulta de mezclar azul y amarillo?',
         'opciones': ['a) Rojo', 'b) Verde', 'c) Naranja', 'd) Marrón'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuántas patas tiene una araña?',
         'opciones': ['a) 6', 'b) 8', 'c) 10', 'd) 4'],
         'respuesta': 'b'}
    ],
    2: [
        {'pregunta': '¿Qué animal dice “muu”?',
         'opciones': ['a) Gato', 'b) Vaca', 'c) Cerdo', 'd) Caballo'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuántas letras tiene el abecedario español?',
         'opciones': ['a) 26', 'b) 27', 'c) 28', 'd) 25'],
         'respuesta': 'b'}
    ],
    3: [
        {'pregunta': '¿Qué país es famoso por la Torre Eiffel?',
         'opciones': ['a) Italia', 'b) Francia', 'c) Alemania', 'd) Reino Unido'],
         'respuesta': 'b'},
        {'pregunta': '¿Cuál es el quinto planeta del sistema solar?',
         'opciones': ['a) Júpiter', 'b) Marte', 'c) Saturno', 'd) Venus'],
         'respuesta': 'a'}
    ],
    4: [
        {'pregunta': '¿Quién escribió “Don Quijote de la Mancha”?',
         'opciones': ['a) Miguel de Cervantes', 'b) Gabriel García Márquez', 'c) Lope de Vega', 'd) Jorge Luis Borges'],
         'respuesta': 'a'},
        {'pregunta': '¿Cuál es la moneda oficial de Japón?',
         'opciones': ['a) Yuan', 'b) Yen', 'c) Won', 'd) Rupia'],
         'respuesta': 'b'}
    ],
    5: [  
        {'pregunta': '¿Quién formuló la ley de la gravitación universal?',
         'opciones': ['a) Kepler', 'b) Newton', 'c) Galileo', 'd) Einstein'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué órgano del cuerpo humano produce insulina?',
         'opciones': ['a) Hígado', 'b) Estómago', 'c) Páncreas', 'd) Riñón'],
         'respuesta': 'c'}
    ],
    6: [  
        {'pregunta': '¿Cuál es el idioma más hablado del mundo por cantidad de hablantes nativos?',
         'opciones': ['a) Inglés', 'b) Hindi', 'c) Español', 'd) Mandarín'],
         'respuesta': 'd'},
        {'pregunta': '¿Qué país fue el primero en llegar al espacio?',
         'opciones': ['a) EE.UU.', 'b) Alemania', 'c) Unión Soviética', 'd) China'],
         'respuesta': 'c'}
    ],
    7: [  
        {'pregunta': '¿Cuántos elementos hay en la tabla periódica actual (2025)?',
         'opciones': ['a) 118', 'b) 116', 'c) 120', 'd) 114'],
         'respuesta': 'a'},
        {'pregunta': '¿Cuál es el único mamífero capaz de volar?',
         'opciones': ['a) Murciélago', 'b) Ardilla voladora', 'c) Águila', 'd) Colibrí'],
         'respuesta': 'a'}
    ],
    8: [ 
        {'pregunta': '¿Qué matemático murió resolviendo la conjetura de Fermat?',
         'opciones': ['a) Euler', 'b) Andrew Wiles', 'c) Pierre de Fermat', 'd) ninguno'],
         'respuesta': 'd'},  # Wiles la resolvió, no murió por ello
        {'pregunta': '¿Qué científico propuso la paradoja del gato que está vivo y muerto a la vez?',
         'opciones': ['a) Schrödinger', 'b) Bohr', 'c) Heisenberg', 'd) Dirac'],
         'respuesta': 'a'}
    ],
    9: [  
        {'pregunta': '¿Cuál es el número primo más pequeño mayor que 100?',
         'opciones': ['a) 101', 'b) 103', 'c) 107', 'd) 109'],
         'respuesta': 'a'},
        {'pregunta': '¿Quién pintó “La escuela de Atenas”?',
         'opciones': ['a) Miguel Ángel', 'b) Rafael', 'c) Da Vinci', 'd) Tiziano'],
         'respuesta': 'b'}
    ],
    10: [  
        {'pregunta': '¿Cuál es el nombre del elemento con símbolo "Og"?',
         'opciones': ['a) Organesio', 'b) Oganesón', 'c) Oganissio', 'd) Ognicio'],
         'respuesta': 'b'},
        {'pregunta': '¿Qué año cayó el Imperio Bizantino con la toma de Constantinopla?',
         'opciones': ['a) 1453', 'b) 1492', 'c) 1517', 'd) 1400'],
         'respuesta': 'a'}
    ]
}

print("\n" + "="*60)
print("¡Bienvenido/a al juego: ¿Quién quiere ser millonario?! 🧠💰")
print("="*60 + "\n")

print("👉 Responde correctamente todas las preguntas para ganar mucho dinero.\n")
print("⚠️ Pero si fallas una... ¡lo perderás todo!\n")
print("🔧 Tienes 3 comodines disponibles para ayudarte en el camino.\n")

nombre_jugador = input("🎤 Concursante, ¡digita tu nombre!: ")

inicio = input(f"\n{nombre_jugador}, ¿estás listo/a para comenzar? (si/no): ").lower()

time.sleep(1)

if inicio == "si":
    print("\n ¡Comenzamos en! ")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("¡Empieza el juego!")

    nivel = 1
    while nivel in preguntas:
        pregunta = preguntas[nivel][0]
        correcta = pregunta['respuesta']
        opciones_actuales = pregunta['opciones']
        primera_vez = True

        while True:
            if primera_vez:
                print(f"\n==== Nivel {nivel} ====\n")
                print(pregunta['pregunta'])
                time.sleep(1)
                for op in opciones_actuales:
                    print(op)
                    time.sleep(1)
                primera_vez = False

            entrada = input('\nEscribe la respuesta correcta (a, b, c o d) o marca "m" para usar un comodín: ').lower()

            if entrada in ['a', 'b', 'c', 'd']:
                if entrada == correcta:
                    dinero += recompensa_por_pregunta
                    print("¡Correcto!\n")
                    print(f"Dinero acumulado: ${dinero}\n")
                    break
                else:
                    print(f"\nIncorrecto. La respuesta correcta era '{correcta}'.")
                    print("Perdiste todo tu dinero.")
                    exit()

            elif entrada == "m":
                if comodines_disponibles["1"] == False:
                    if comodines_disponibles["2"] == False:
                        if comodines_disponibles["3"] == False:
                            print("Ya no tienes comodines disponibles.")
                            continue

                print("\n -Comodines disponibles: \n")
                if comodines_disponibles["1"]:
                    print("1 - Llamar a un amigo, te dará una respuesta al azar\n")
                if comodines_disponibles["2"]:
                    print("2 - 50/50, dos incorrectas se van. Queda la buena y la mala.\n")
                if comodines_disponibles["3"]:
                    print("3 - Cambio de pregunta, te damos otra del mismo nivel.\n")

                eleccion = input("¿Qué comodín quieres usar? (1, 2 o 3): ")
                if eleccion in comodines_disponibles and comodines_disponibles[eleccion]:
                    comodines_disponibles[eleccion] = False

                    if eleccion == "1":
                        print("Llamando a un amigo...")
                        time.sleep(2)
                        sugerencia = random.choice(['a', 'b', 'c', 'd'])
                        print(f"Tu amigo dice que cree que la respuesta es: '{sugerencia}'")
                        comodin_usado1 = True
                        time.sleep(1)

                    elif eleccion == "2":
                        print("Se eliminan dos respuestas incorrectas")
                        letras = ['a', 'b', 'c', 'd']
                        opciones_incorrectas = []
                        for letra in letras:
                            if letra != correcta:
                                opciones_incorrectas.append(letra)

                        eliminadas = random.sample(opciones_incorrectas, 2)
                        opciones_actuales = [ ]
                        for op in pregunta['opciones']:
                                if op[0] == correcta:
                                    opciones_actuales.append(op)
                                elif op[0] not in eliminadas:
                                    opciones_actuales.append(op)

                        print("\n Opciones después del 50/50:")
                        time.sleep(1)
                        for op in opciones_actuales:
                            print(op)
                            time.sleep(1)
                        
                    elif eleccion == "3":
                        print("\n Nueva pregunta:")
                        nueva = pregunta
                        while nueva == pregunta:
                         nueva = preguntas[nivel][1]
                        pregunta = nueva
                        correcta = pregunta['respuesta']
                        opciones_actuales = pregunta['opciones']
                        primera_vez = True
                    
                else:
                    print("Comodín no disponible o ya usado.")
            else:
                print("¡Error!...Escribe a, b, c, d o m para comodín.")

        nivel += 1

    print(f"\n¡Felicidades, {nombre_jugador}! Completaste todos los niveles. Ganaste un total de: ${dinero}")
    print("Gracias por jugar.")
else:
    print("Juego cancelado :(")
    print("Tal vez la próxima vez. ¡Hasta luego!")
