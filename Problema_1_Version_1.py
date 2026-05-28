# Nombre del estudiante: Lisandro Martinez
# Grupo: 75
# Programa: Ingenieria de sistemas
# Código Fuente: Autoría propia

# MATRIZ DE DATOS
# Formato:
# [ID Cliente, Duracion en segundos, Numero de clics]

sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 190, 10],
    [105, 80, 1]
]

# FUNCION PARA CLASIFICAR EL COMPROMISO

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# GENERACION DEL INFORME

print("==============================================")
print(" INFORME DE COMPROMISO DE SESIONES")
print("==============================================")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Duracion:", duracion, "segundos")
    print("Clics:", clics)
    print("Clasificacion:", clasificacion)
    print("----------------------------------------------")