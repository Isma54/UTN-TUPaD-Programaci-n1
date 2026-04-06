#Ejercicio 3 - Agenda de Turnos con Nombres
lunes1= ""
lunes2= ""
lunes3= ""
lunes4= ""

martes1= ""
martes2= ""
martes3= ""

nombre= input("Ingrese su nombre: ").strip()
while not nombre.isalpha():
    print("Error: Ingrese solo letras")
    nombre= input("Ingrese su nombre: ").strip()
while True:
    print("")
    print(""" --Menú Clinica-- 
1_ Reservar turno
2_ Cancelar turno
3_ Ver agenda del día
4_ Ver resumen general
5_ Cerrar sistema""")
    opcion= input("Seleccione una de las opciones disponibles: ").strip()
    match opcion:
        case "1":
            print("")
            print("""[Escoja el dia del turno]
1_ Lunes
2_ Martes """)
            dia= input("Turno: ").strip()
            while not dia == "1" and not dia == "2":
                print("Día no valido, intente nuevamente")
                print("")
                print("""[Escoja el dia del turno]
1_ Lunes
2_ Martes """)
                dia= input("Turno: ").strip()
            nombre_paciente= input("Nombre del paciente: ").strip().capitalize()
            while not nombre_paciente.isalpha():
                print("Error: Ingrese solo letras")
                nombre_paciente= input("Nombre del paciente: ").strip().capitalize()
            if dia == "1":
                if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente or lunes4 == nombre_paciente:
                    print(f"El paciente {nombre_paciente} ya posee un turno para el Lunes")
                else:
                    if lunes1 == "":
                        lunes1 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    elif lunes2 == "":
                        lunes2 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    elif lunes3 == "":
                        lunes3 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    elif lunes4 == "":
                        lunes4 = nombre_paciente
                        print(f"Turno para {nombre_paciente}, cargado con exito")
                    else:
                        print("Por el momento no contamos con turnos disponibles para el día Lunes")
                    
            elif dia == "2":
                if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                    print(f"El paciente {nombre_paciente} ya posee un turno para el Martes")
                else:
                    if martes1 == "":
                        martes1 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    elif martes2 == "":
                        martes2 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    elif martes3 == "":
                        martes3 = nombre_paciente
                        print(f"Turno para {nombre_paciente} cargado con exito")
                    else:
                        print("Por el momento no contamos con turnos disponibles para el día Martes")

        case "2":
            print("")
            print("""[Escoja el dia del turno a cancelar]
1_ Lunes
2_ Martes """)
            dia= input("Turno: ").strip()
            while not dia == "1" and not dia == "2":
                print("Día no valido, intente nuevamente")
                print("")
                print("""[Escoja el dia del turno a cancelar]
1_ Lunes
2_ Martes """)
                dia= input("Turno: ").strip()
            nombre_paciente= input("Nombre del paciente: ").strip().capitalize()
            while not nombre_paciente.isalpha():
                print("Error: Ingrese solo letras")
                nombre_paciente= input("Nombre del paciente: ").strip().capitalize()
            if dia == "1":
                if lunes1 == nombre_paciente:
                    lunes1 = ""
                    print("Turno cancelado con exito")
                elif lunes2 == nombre_paciente:
                    lunes2 = ""
                    print("Turno cancelado con exito")
                elif lunes3 == nombre_paciente:
                    lunes3 = ""
                    print("Turno cancelado con exito")
                elif lunes4 == nombre_paciente:
                    lunes4 = ""
                    print("Turno cancelado con exito")
                else:
                    print(f"El paciente {nombre_paciente} no posee un turno para el día Lunes")
                    
            elif dia == "2":
                if martes1 == nombre_paciente:
                    martes1 = ""
                    print("Turno cancelado con exito")
                elif martes2 == nombre_paciente:
                    martes2 = ""
                    print("Turno cancelado con exito")
                elif martes3 == nombre_paciente:
                    martes3 = ""
                    print("Turno cancelado con exito")
                else:
                    print(f"El paciente {nombre_paciente} no posee un turno para el día Martes")

        case "3":
            print("")
            print("""[Escoja el dia para ver turnos]
1_ Lunes
2_ Martes """)
            dia= input("Turno: ").strip()
            while not dia == "1" and not dia == "2":
                print("Día no valido, intente nuevamente")
                print("")
                print("""Escoja el dia para ver turnos
1_ Lunes
2_ Martes """)
                dia= input("Turno: ").strip()

            if dia == "1":
                print("Turno 1:", lunes1 if not lunes1 == "" else "(libre)")
                print("Turno 2:", lunes2 if not lunes2 == "" else "(libre)")
                print("Turno 3:", lunes3 if not lunes3 == "" else "(libre)")
                print("Turno 4:", lunes4 if not lunes4 == "" else "(libre)")
            elif dia == "2":
                print("Turno 1:", martes1 if not martes1 == "" else "(libre)")
                print("Turno 2:", martes2 if not martes2 == "" else "(libre)")
                print("Turno 3:", martes3 if not martes3 == "" else "(libre)")

        case "4":
            lunes_libres= 4
            lunes_ocupados= 0

            martes_libres= 3
            martes_ocupados= 0

            if not lunes1 == "": lunes_ocupados += 1
            if not lunes2 == "": lunes_ocupados += 1
            if not lunes3 == "": lunes_ocupados += 1
            if not lunes4 == "": lunes_ocupados += 1
            lunes_libres -= lunes_ocupados

            if not martes1 == "": martes_ocupados += 1
            if not martes2 == "": martes_ocupados += 1
            if not martes3 == "": martes_ocupados += 1
            martes_libres -= martes_ocupados

            print("")
            print("[Resumen General]")
            print(f"""LUNES
-Ocupados: {lunes_ocupados}
-Libres: {lunes_libres}""")
            print("")
            print(f"""MARTES
-Ocupados: {martes_ocupados}
-Libres: {martes_libres}""")

        case "5":
            print("¡Hasta luego!")
            print("")
            break
        case _:
            print("Error: La opcion seleccionada está fuera de rango, intente con otra opción")