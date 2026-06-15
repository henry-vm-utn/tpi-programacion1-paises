import csv

ARCHIVO_CSV = "paises.csv"


# Trabajo Practico Integrador - Programacion I
# Gestion de datos de paises en Python

# El programa trabaja con una lista de diccionarios.
# Cada diccionario representa un pais con nombre, poblacion,
# superficie y continente.


# Esta funcion sirve para comparar textos ignorando espacios,
# mayusculas y minusculas.
def normalizar_texto(texto):
    return texto.strip().lower()


# Esta funcion arma el diccionario de un pais.
def crear_pais(nombre, poblacion, superficie, continente):
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    return pais


# Esta funcion busca un pais por nombre exacto.
# Si lo encuentra, devuelve la posicion.
# Si no lo encuentra, devuelve -1.
def buscar_posicion_pais(paises, nombre):
    nombre_buscado = normalizar_texto(nombre)

    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == nombre_buscado:
            return i

    return -1


# Esta funcion lee el archivo CSV y carga los paises en una lista.
def cargar_paises_csv(nombre_archivo):
    paises = []
    columnas_necesarias = ["nombre", "poblacion", "superficie", "continente"]

    try:
        with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames is None:
                print("Error: el archivo CSV esta vacio.")
                return paises

            for columna in columnas_necesarias:
                if columna not in lector.fieldnames:
                    print("Error: falta la columna", columna, "en el archivo CSV.")
                    return paises

            numero_linea = 1

            for fila in lector:
                numero_linea = numero_linea + 1

                try:
                    nombre = fila["nombre"].strip()
                    poblacion_texto = fila["poblacion"].strip()
                    superficie_texto = fila["superficie"].strip()
                    continente = fila["continente"].strip()

                    # No se cargan filas con campos vacios.
                    if nombre == "" or poblacion_texto == "" or superficie_texto == "" or continente == "":
                        print("Aviso: se salto la linea", numero_linea, "porque tiene campos vacios.")
                    else:
                        poblacion = int(poblacion_texto)
                        superficie = int(superficie_texto)

                        # Para este trabajo no aceptamos datos negativos ni cero.
                        if poblacion <= 0 or superficie <= 0:
                            print("Aviso: se salto la linea", numero_linea, "porque tiene valores no validos.")
                        else:
                            pais = crear_pais(nombre, poblacion, superficie, continente)
                            paises.append(pais)

                except ValueError:
                    print("Aviso: se salto la linea", numero_linea, "por error de formato numerico.")

    except FileNotFoundError:
        print("Error: no se encontro el archivo", nombre_archivo)
        print("Verifique que paises.csv este en la misma carpeta que main.py.")

    return paises


# Esta funcion guarda los datos actualizados en el archivo CSV.
def guardar_paises_csv(nombre_archivo, paises):
    columnas = ["nombre", "poblacion", "superficie", "continente"]

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()

            for pais in paises:
                escritor.writerow(pais)

        return True

    except Exception:
        print("Error: no se pudo guardar el archivo CSV.")
        return False


# Esta funcion pide texto y controla que no quede vacio.
def pedir_texto(mensaje):
    texto = input(mensaje).strip()

    while texto == "":
        print("Error: el campo no puede quedar vacio.")
        texto = input(mensaje).strip()

    return texto


# Esta funcion pide un numero entero.
# Si el usuario escribe texto, vuelve a pedir el dato.
def pedir_entero(mensaje):
    dato_correcto = False
    numero = 0

    while dato_correcto == False:
        try:
            numero = int(input(mensaje).strip())
            dato_correcto = True
        except ValueError:
            print("Error: debe ingresar un numero entero valido.")

    return numero


# Esta funcion pide un entero mayor que cero.
def pedir_entero_mayor_cero(mensaje):
    numero = pedir_entero(mensaje)

    while numero <= 0:
        print("Error: debe ingresar un numero mayor que cero.")
        numero = pedir_entero(mensaje)

    return numero


# Esta funcion pide un entero igual o mayor que cero.
# Se usa para los rangos de filtros.
def pedir_entero_no_negativo(mensaje):
    numero = pedir_entero(mensaje)

    while numero < 0:
        print("Error: debe ingresar un numero igual o mayor que cero.")
        numero = pedir_entero(mensaje)

    return numero


# Esta funcion muestra un pais en una sola linea.
def mostrar_pais(pais):
    print(
        "Nombre:", pais["nombre"],
        "| Poblacion:", pais["poblacion"],
        "| Superficie:", pais["superficie"], "km2",
        "| Continente:", pais["continente"]
    )


# Esta funcion muestra una lista de paises.
def mostrar_lista_paises(paises):
    if len(paises) == 0:
        print("No hay paises para mostrar.")
    else:
        for pais in paises:
            mostrar_pais(pais)


# Esta funcion muestra el menu principal del sistema.
def mostrar_menu():
    print()
    print("====================================")
    print("SISTEMA DE GESTION DE DATOS DE PAISES")
    print("====================================")
    print("1. Mostrar todos los paises")
    print("2. Agregar un pais")
    print("3. Actualizar poblacion y superficie")
    print("4. Buscar pais por nombre")
    print("5. Filtrar por continente")
    print("6. Filtrar por rango de poblacion")
    print("7. Filtrar por rango de superficie")
    print("8. Ordenar paises")
    print("9. Mostrar estadisticas")
    print("0. Salir")


# Opcion 1:
# Muestra todos los paises cargados desde el CSV.
def mostrar_todos_los_paises(paises):
    print()
    print("Listado de paises")
    mostrar_lista_paises(paises)


# Opcion 2:
# Agrega un nuevo pais y despues guarda el CSV.
def agregar_pais(paises):
    print()
    print("Agregar pais")

    nombre = pedir_texto("Ingrese nombre del pais: ")

    if buscar_posicion_pais(paises, nombre) != -1:
        print("Error: ese pais ya existe en el sistema.")
        return

    poblacion = pedir_entero_mayor_cero("Ingrese poblacion: ")
    superficie = pedir_entero_mayor_cero("Ingrese superficie en km2: ")
    continente = pedir_texto("Ingrese continente: ")

    nuevo_pais = crear_pais(nombre, poblacion, superficie, continente)
    paises.append(nuevo_pais)

    if guardar_paises_csv(ARCHIVO_CSV, paises):
        print("Pais agregado correctamente.")


# Opcion 3:
# Actualiza la poblacion y la superficie de un pais existente.
def actualizar_pais(paises):
    print()
    print("Actualizar pais")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    nombre = pedir_texto("Ingrese el nombre exacto del pais a actualizar: ")
    posicion = buscar_posicion_pais(paises, nombre)

    if posicion == -1:
        print("No se encontro un pais con ese nombre.")
        return

    print("Datos actuales:")
    mostrar_pais(paises[posicion])

    nueva_poblacion = pedir_entero_mayor_cero("Ingrese nueva poblacion: ")
    nueva_superficie = pedir_entero_mayor_cero("Ingrese nueva superficie en km2: ")

    paises[posicion]["poblacion"] = nueva_poblacion
    paises[posicion]["superficie"] = nueva_superficie

    if guardar_paises_csv(ARCHIVO_CSV, paises):
        print("Datos actualizados correctamente.")


# Opcion 4:
# Busca por nombre exacto o por coincidencia parcial.
def buscar_pais_por_nombre(paises):
    print()
    print("Buscar pais por nombre")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    print("1. Coincidencia exacta")
    print("2. Coincidencia parcial")

    opcion = input("Seleccione una opcion: ").strip()
    texto_busqueda = pedir_texto("Ingrese nombre o parte del nombre: ")
    resultados = []

    if opcion == "1":
        posicion = buscar_posicion_pais(paises, texto_busqueda)

        if posicion != -1:
            resultados.append(paises[posicion])

    elif opcion == "2":
        texto_normalizado = normalizar_texto(texto_busqueda)

        for pais in paises:
            if texto_normalizado in normalizar_texto(pais["nombre"]):
                resultados.append(pais)
    else:
        print("Opcion invalida.")
        return

    if len(resultados) == 0:
        print("No se encontraron resultados.")
    else:
        print("Resultados encontrados:")
        mostrar_lista_paises(resultados)


# Opcion 5:
# Filtra los paises por continente.
def filtrar_por_continente(paises):
    print()
    print("Filtrar por continente")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    continente_buscado = pedir_texto("Ingrese continente: ")
    resultados = []

    for pais in paises:
        if normalizar_texto(pais["continente"]) == normalizar_texto(continente_buscado):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises para ese continente.")
    else:
        print("Resultados encontrados:")
        mostrar_lista_paises(resultados)


# Opcion 6:
# Filtra los paises por un rango de poblacion.
def filtrar_por_rango_poblacion(paises):
    print()
    print("Filtrar por rango de poblacion")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    minimo = pedir_entero_no_negativo("Ingrese poblacion minima: ")
    maximo = pedir_entero_no_negativo("Ingrese poblacion maxima: ")

    if minimo > maximo:
        print("Error: el minimo no puede ser mayor que el maximo.")
        return

    resultados = []

    for pais in paises:
        if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises en ese rango de poblacion.")
    else:
        print("Resultados encontrados:")
        mostrar_lista_paises(resultados)


# Opcion 7:
# Filtra los paises por un rango de superficie.
def filtrar_por_rango_superficie(paises):
    print()
    print("Filtrar por rango de superficie")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    minimo = pedir_entero_no_negativo("Ingrese superficie minima: ")
    maximo = pedir_entero_no_negativo("Ingrese superficie maxima: ")

    if minimo > maximo:
        print("Error: el minimo no puede ser mayor que el maximo.")
        return

    resultados = []

    for pais in paises:
        if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron paises en ese rango de superficie.")
    else:
        print("Resultados encontrados:")
        mostrar_lista_paises(resultados)


# Estas funciones se usan como criterio para ordenar.
def obtener_nombre(pais):
    return pais["nombre"]


def obtener_poblacion(pais):
    return pais["poblacion"]


def obtener_superficie(pais):
    return pais["superficie"]


# Opcion 8:
# Ordena los paises por nombre, poblacion o superficie.
def ordenar_paises(paises):
    print()
    print("Ordenar paises")

    if len(paises) == 0:
        print("Error: no hay paises cargados.")
        return

    print("1. Ordenar por nombre")
    print("2. Ordenar por poblacion")
    print("3. Ordenar por superficie")

    criterio = input("Seleccione criterio: ").strip()

    print("1. Ascendente")
    print("2. Descendente")

    sentido = input("Seleccione sentido: ").strip()

    if sentido == "1":
        descendente = False
    elif sentido == "2":
        descendente = True
    else:
        print("Opcion de sentido invalida.")
        return

    if criterio == "1":
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=descendente)
    elif criterio == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=descendente)
    elif criterio == "3":
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=descendente)
    else:
        print("Opcion de criterio invalida.")
        return

    print("Resultados ordenados:")
    mostrar_lista_paises(paises_ordenados)


# Opcion 9:
# Calcula estadisticas generales sobre los paises cargados.
def mostrar_estadisticas(paises):
    print()
    print("Estadisticas")

    if len(paises) == 0:
        print("No hay datos suficientes para calcular estadisticas.")
        return

    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    cantidad_por_continente = {}

    for pais in paises:
        suma_poblacion = suma_poblacion + pais["poblacion"]
        suma_superficie = suma_superficie + pais["superficie"]

        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] = cantidad_por_continente[continente] + 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("Pais con mayor poblacion:")
    mostrar_pais(pais_mayor_poblacion)

    print("Pais con menor poblacion:")
    mostrar_pais(pais_menor_poblacion)

    print("Promedio de poblacion:", round(promedio_poblacion, 2))
    print("Promedio de superficie:", round(promedio_superficie, 2), "km2")

    print("Cantidad de paises por continente:")
    for continente in cantidad_por_continente:
        print(continente + ":", cantidad_por_continente[continente])


# Bloque principal del programa.
# Aca se carga el CSV y se controla el menu.
def main():
    paises = cargar_paises_csv(ARCHIVO_CSV)

    sistema_activo = True

    while sistema_activo:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            mostrar_todos_los_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais_por_nombre(paises)
        elif opcion == "5":
            filtrar_por_continente(paises)
        elif opcion == "6":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "7":
            filtrar_por_rango_superficie(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Cerrando el sistema. Gracias por usar el programa.")
            sistema_activo = False
        else:
            print("Error: ingrese una opcion valida.")


# Llamamos a la funcion principal para iniciar el programa.
main()
