#Ejercicio 4- Escape Room: La Bóveda
energia= 100
tiempo= 12
cerraduras_abiertas= 0
alarma = False
codigo_parcial= ""
forzar_seguidas= 0

agente= input("Ingrese su nombre: ").strip().capitalize()
while not agente.isalpha():
    print("Error: Ingrese solo letras")
    agente= input("Ingrese su nombre: ").strip().capitalize()
print(f"Bienvenido {agente}")
print("Sos un agente y tu misión es intentar abrir una boveda con 3 candados, pero la energía y el tiempo son limitado. Si logras abrirlo antes que el tiempo termine o te quedes sin energía, ganás.")
print("")
print("..Buena suerte..")

while True:
    if alarma == True and tiempo <= 3:
        print("")
        print("--JUEGO TERMINADO--")
        print("[DERROTA]")
        print("Hoy no es tu día agente, el sistema se bloqueó. Suerte para la próxima")
        break
    elif energia <= 0 or tiempo <= 0:
        print("")
        print("--JUEGO TERMINADO--")
        print("[DERROTA]")
        print("Que mala suerte tienes agente, la próxima vez revisa tu estado. Suerte para la próxima")
        break
    elif cerraduras_abiertas == 3:
        print("")
        print("--JUEGO TERMINADO--")
        print("[VICTORIA]")
        print("Felicidades agente ¡Haz ganado!")
        break
    else:
        print("")
        print("""--MENÚ DE ACCIONES-- 
[1] Forzar cerradura (costo: -20 energía, -2 tiempo)
[2] Hackear panel (costo: -10 energía, -3 tiempo)
[3] Descansar (Costo: +15 energía, -1 tiempo, si alarma ON: -10 energía extra)
[4] Consultar estado""")
        desicion= input("¿Qué vas hacer agente?: ").strip()
        if desicion.isdigit():
            if desicion == "1":
                energia -= 20
                tiempo -= 2
                forzar_seguidas += 1
                if forzar_seguidas == 3:
                    alarma= True
                    print("¡Se trabó la cerradura y la alarma se activó!")
                    print("")
                else:
                    if energia < 40:
                        opcion= ""
                        while not (opcion == "1" or opcion == "2" or opcion == "3"):
                            opcion= input("Elige con cuidado, hay riesgo de alarma (1, 2 o 3): ").strip()
                            if not opcion.isdigit():
                                print("Por favor, seleccione una de las opciones mencionadas en el mensaje")
                                opcion= ""

                        if opcion == "3":
                            if alarma:
                                print("La alarma ya estaba activada, el ruido sigue aturdiéndote.. ")
                            else:
                                alarma = True
                                print("¡La alarma se activó!")

                    if not alarma:
                        cerraduras_abiertas += 1
                        print("¡Haz abierto una cerradura!")
                    else:
                        print("La alarma esta activa ¡La acción falló!")    
            
            elif desicion =="2":
                forzar_seguidas = 0
                energia -= 10
                tiempo -= 3
                print("Iniciando el hackeo...")
                for a in range(4):
                    print(f"Paso {a+1}: Hackeando...")
                    codigo_parcial += "Y"
                    print("[" + "#" * (a+1) + "." * (4 - (a+1)) + f"] {(a+1)*25}%")

                    if len(codigo_parcial) >= 8 and cerraduras_abiertas <= 3:
                        if (a+1) == 4:
                            print("¡Se abrió una cerradura con exito!")
                            cerraduras_abiertas += 1
                            print("Hackeo completado")
                    
            elif desicion == "3":
                forzar_seguidas = 0
                if not alarma:
                    energia += 15
                    tiempo  -= 1
                    print("Descansas un poco..")
                else:
                    energia -= 10
                    print("No logras descansar por la alarma ¡Date prisa!")
        
            elif desicion == "4":
                print("")
                print("--ESTADO--")
                print(f"[ENERGÍA]: {energia}")
                print(f"[TIEMPO]:{tiempo}")
                print(f"[CERRADURAS ABIERTAS]: {cerraduras_abiertas}/3")

            else:
                print("Error: La opcion colocada no se encuentra en el menú, intente nuevamente")
        else:
            print("Error: Solo se aceptan números positivos")