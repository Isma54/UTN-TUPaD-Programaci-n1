#Ejercicio 2 - "Acceso al Campus y Menú Seguro"
intentos= 0
salir= False
usuario_correcto= "alumno"
clave_correcta= "python123"
for i in range (1,4):
    print(f"Intento {i}/3")
    usuario= input("Usuario: ")
    clave= input("Clave: ")
    print("")
    if usuario == usuario_correcto and clave == clave_correcta:
      while True:
          print("""-CAMPUS-
1) Estado
2) Cambiar clave
3) Mensaje
4) Salir """)
          opcion= input("Opción: ").strip()
          if opcion == "1" and opcion.isdigit():
             print("Estado de inscripción: Inscripto")
          elif opcion == "2" and opcion.isdigit():
             clave_nueva= input("Escriba la nueva clave (la clave debe tener un minimo de 6 carácteres):").strip()
             confirmacion= input("Vuelva a escribir su nueva clave: ").strip()
             print("")
             if clave_nueva == confirmacion:
                if len(clave_nueva) > 6:
                   print("Clave cambiada con exito")
                   print("")
                else:
                   print("Su clave no supera los 6 carácteres, pruebe con otra")
                   print("")
             else:
                print("Las claves no coinciden, intente nuevamente")
                print("")
             
          elif opcion == "3" and opcion.isdigit():
             print("=============================================================================================================================")
             print("Si no puedes volar, corre; si no puedes correr, camina; si no puedes caminar, gatea, pero hagas lo que hagas, sigue adelante.")
             print("=============================================================================================================================")
             print("")
          elif opcion == "4" and opcion.isdigit():
             salir= True
             print("¡Hasta pronto!")
             break
          else:
             print("Error: la opcion seleccionada no es valida")
             print("")
    else:
       print("Error: Las credenciales no son validas")
       intentos += 1

    if salir == True:
       break
if intentos == 3:
   print("Cuenta bloqueada")       
         