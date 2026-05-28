# Nombre del estudiante: Lisandro Martinez
# Grupo: 75
# Programa: Ingenieria de sistemas
# Código Fuente: Autoría propia

# FUNCION PARA CLASIFICAR EL COMPROMISO

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# MATRIZ DONDE SE GUARDAN LAS SESIONES

sesiones = []

# MENU PRINCIPAL

while True:

    print("\n====================================")
    print("   SISTEMA DE CLASIFICACION")
    print("====================================")
    print("1. Registrar nueva sesion")
    print("2. Mostrar informe")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    # OPCION 1 - REGISTRAR SESION

    if opcion == "1":

        id_cliente = input("Ingrese el ID del cliente: ")

        duracion = int(input("Ingrese la duracion de la sesion en segundos: "))

        clics = int(input("Ingrese la cantidad de clics: "))

        # Guardar en la matriz
        sesiones.append([id_cliente, duracion, clics])

        print("Sesion registrada correctamente.")

    # OPCION 2 - MOSTRAR INFORME

    elif opcion == "2":

        if len(sesiones) == 0:
            print("No hay sesiones registradas.")

        else:

            print("\n====================================")
            print(" INFORME DE COMPROMISO")
            print("====================================")

            for sesion in sesiones:

                id_cliente = sesion[0]
                duracion = sesion[1]
                clics = sesion[2]

                clasificacion = clasificar_compromiso(duracion, clics)

                print("\nCliente:", id_cliente)
                print("Duracion:", duracion, "segundos")
                print("Clics:", clics)
                print("Clasificacion:", clasificacion)
                print("------------------------------------")

    # OPCION 3 - SALIR

    elif opcion == "3":

        print("Programa finalizado.")
        break

    # OPCION INVALIDA

    else:

        print("Opcion invalida. Intente nuevamente.")
