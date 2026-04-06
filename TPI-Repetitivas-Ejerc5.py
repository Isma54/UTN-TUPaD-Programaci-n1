#Ejercicio 5 - Escape Room: La Arena del Gladiador
print("Bienvenido gladiador")
nombre_jugador= input("¿Cuál es tu nombre?: ").strip().capitalize()
while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_jugador= input("¿Cuál es tu nombre?: ").strip().capitalize()

vida_gladiador= 100
vida_enemigo= 100
pociones_vida= 3
daño_base= 15
daño_enemigo= 12
turno_gladiador= True
primer_turno= True

while vida_gladiador > 0 and vida_enemigo > 0:
    print("")
    if primer_turno:
        print("== INICIO DEL COMBATE ==")
    else:
        print("== NUEVO TURNO ==")
    
    print(f"{nombre_jugador} (HP: {vida_gladiador}) VS Enemigo ({vida_enemigo}) | Pociones: {pociones_vida}")
    print("""[1] Ataque pesado
[2] Ráfaga veloz
[3] Curar """)
    opcion= input("Opción: ")
    if opcion.isdigit():
        if opcion == "1":
            if vida_enemigo < 20:
                daño_critico= daño_base * 1.5
                vida_enemigo -= daño_critico
                print("")
                print(f"[GOLPE CRITICO]")
                print(f"¡Atacaste al enemigo por {daño_critico} puntos de daño!")
                print("")
                if vida_enemigo <= 0:
                    pass
                else:
                    vida_gladiador -= daño_enemigo
                    print("¡El enemigo te atacó por 12 puntos de daño!")
                    primer_turno = False
            else:
                vida_enemigo -= daño_base
                print(f"¡Atacaste al enemigo por {daño_base} puntos de daño!")
                print("")
                if vida_enemigo <= 0:
                    pass
                else:
                    vida_gladiador -= daño_enemigo
                    print("¡El enemigo te atacó por 12 puntos de daño!")
                    primer_turno = False

        elif opcion == "2":
            print("Inicias una ráfaga de golpes")
            for i in range(3):
                vida_enemigo -= 5
                print("Golpe conectado por 5 de daño")
            print("")
            vida_gladiador -= daño_enemigo
            print("¡El enemigo te atacó por 12 puntos de daño!")
            primer_turno = False

        elif opcion == "3":
            if pociones_vida > 0:
                vida_gladiador += 30
                pociones_vida -= 1
                print("Usaste una pocion de curación")
                print("+30 HP")
                print("")
                vida_gladiador -= daño_enemigo
                print("¡El enemigo te atacó por 12 puntos de daño!")
                primer_turno = False
            else:
                print("¡No te quedan pociones!")
                print("")
                vida_gladiador -= daño_enemigo
                print("¡El enemigo te atacó por 12 puntos de daño!")
                primer_turno = False
        else:
            print("Error: Selección fuera de rango")
    else:
        print("Error: Solo se permiten números positivos")

if vida_enemigo <=0:
    print("")
    print("¡VICTORIA!")
    print(f"{nombre_jugador} ha ganado la batalla")
else:
    print("")
    print("DERROTA")
    print("Has caído en combate...")