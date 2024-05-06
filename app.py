lista_destinos = [
    ("monteria", "colombia"),
    ("mar de la plata", "argentina"),
    ("medellin", "colombia")]

lista_viajeros = [("jeffry", 10, lista_destinos[0]),
                  ("tavo", 100, lista_destinos[0]),
                  ("maria", 9, lista_destinos[2])]

def agregar_viajero():
    nombre_persona = input("Ingrese el nombre del pasajero: ")
    cedula_persona = input("Ingrese el número de cédula del pasajero: ")
    ciudad_destino = input("Ingrese la ciudad de destino del pasajero: ")
    pais_destino = input("Ingrese el pais destino del pasajero: " )
    #falta agregarlo bien

    info_viajero = (nombre_persona, cedula_persona, ciudad_destino, pais_destino)

    lista_viajeros.append(info_viajero)
    print(f"La lista de viajeros son {lista_viajeros}")

def agregar_destino():
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    nombre_pais = input("Ingrese el nombre del país al que pertenece la ciudad: ")

    info_destino= (nombre_ciudad, nombre_pais)

    lista_destinos.append(info_destino)
    print(f"La lista de destinos son {lista_destinos}")

def consultar_destino_por_cedula():
    consultar_por_cedula = int(input("Ingrese la cedula: "))
    for i in lista_viajeros:
        if i[1] == consultar_por_cedula:
            nombre = i[0]
            destino = i[2][0]  # Nombre de la ciudad
            pais = i[2][1]  # Nombre del país
            print(f"El pasajero con cédula {consultar_por_cedula} se llama {nombre} y viaja a {destino}, {pais}.")
            return
    print("Cedula no encontrada")

def consultar_numero_pasajeros_a_ciudad_por_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad para consultar la cantidad de pasajeros: ")
    contador = 0
    for i in lista_viajeros:
        ciudad_viaje = i[2][0]  # Accede al nombre de la ciudad en la tupla de destino
        if ciudad_viaje.lower() == ciudad.lower():  # Convertir ambas a minúsculas para comparar
            contador += 1
    print(f"La cantidad de pasajeros que viajan a {ciudad} es: {contador}")

def salir():
    print("Gracias por usar el programa. ¡Hasta luego!")
    exit()

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar viajero.")
        print("2. Agregar destino.")
        print("3. Consultar ciudad y pais destino con cedula.")
        print("4. Consultar numero de pasajeros que viajan a una ciudad.")
        print("5. Consultar numero de pasajeros que viajan a un pais.")
        print("9. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_viajero()
        elif opcion == "2":
            agregar_destino()
        elif opcion == "3":
            consultar_destino_por_cedula()
        elif opcion == "4":
            consultar_numero_pasajeros_a_ciudad_por_ciudad()
        elif opcion =="5":
            print("falta la función")
            #consultar_numero_pasajeros_a_pais_por_pais()
        elif opcion == "9":
            salir()
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

menu()


#agregar a un viajero con tupla.
#hacer la función para consultar pais dado el pais.
