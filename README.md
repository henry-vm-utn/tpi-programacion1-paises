# Trabajo Practico Integrador - Programacion 1

## Gestion de Datos de Paises en Python

Este proyecto corresponde al Trabajo Practico Integrador de la materia Programacion 1 de la Tecnicatura Universitaria en Programacion.

El sistema permite gestionar informacion de paises utilizando Python. Los datos se leen desde un archivo CSV y se almacenan internamente en una lista de diccionarios. A partir de esos datos, el programa permite realizar busquedas, filtros, ordenamientos, actualizaciones y calculo de estadisticas basicas.

## Objetivo del proyecto

El objetivo principal es desarrollar una aplicacion por consola que permita aplicar los contenidos vistos en Programacion 1:

* Listas.
* Diccionarios.
* Funciones.
* Condicionales.
* Ciclos.
* Lectura de archivos CSV.
* Validaciones.
* Ordenamientos.
* Estadisticas basicas.

## Estructura del proyecto

```text
tpi-programacion1-paises/
│
├── main.py
├── paises.csv
├── README.md
└── informe_TPI_paises.pdf
```

## Archivos principales

### main.py

Contiene el codigo fuente completo del programa. Incluye el menu principal, las funciones de carga del CSV, busquedas, filtros, ordenamientos, actualizaciones y estadisticas.

### paises.csv

Contiene el dataset base utilizado por el sistema. Cada registro representa un pais con los siguientes campos:

```text
nombre,poblacion,superficie,continente
```

### informe_TPI_paises.pdf

Documento academico y tecnico del proyecto. Incluye marco teorico, decisiones tecnicas, esquema de funcionamiento, capturas, dificultades, conclusiones y links.

## Como ejecutar el programa

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en VS Code.
3. Verificar que `main.py` y `paises.csv` esten en la misma carpeta.
4. Abrir una terminal.
5. Ejecutar:

```bash
python main.py
```

## Funcionalidades del sistema

El programa permite:

1. Mostrar todos los paises cargados.
2. Agregar un nuevo pais.
3. Actualizar poblacion y superficie de un pais existente.
4. Buscar paises por nombre con coincidencia exacta o parcial.
5. Filtrar paises por continente.
6. Filtrar paises por rango de poblacion.
7. Filtrar paises por rango de superficie.
8. Ordenar paises por nombre, poblacion o superficie.
9. Mostrar estadisticas generales.

## Validaciones incluidas

El sistema controla:

* Campos vacios al agregar datos.
* Numeros invalidos al ingresar poblacion o superficie.
* Valores negativos.
* Busquedas sin resultados.
* Filtros sin resultados.
* Errores de formato dentro del archivo CSV.
* Archivo CSV inexistente o con columnas incorrectas.

## Ejemplos de uso

### Buscar por nombre parcial

Entrada:

```text
Opcion: 4
Tipo de busqueda: 2
Texto ingresado: an
```

Salida esperada:

```text
Resultados encontrados:
Nombre: Argentina | Poblacion: 45376763 | Superficie: 2780400 km2 | Continente: America
Nombre: Alemania | Poblacion: 83149300 | Superficie: 357022 km2 | Continente: Europa
Nombre: Francia | Poblacion: 68042591 | Superficie: 551695 km2 | Continente: Europa
```

### Filtrar por continente

Entrada:

```text
Opcion: 5
Continente: Europa
```

Salida esperada:

```text
Nombre: Alemania | Poblacion: 83149300 | Superficie: 357022 km2 | Continente: Europa
Nombre: Francia | Poblacion: 68042591 | Superficie: 551695 km2 | Continente: Europa
Nombre: España | Poblacion: 48592909 | Superficie: 505990 km2 | Continente: Europa
```

### Estadisticas

Entrada:

```text
Opcion: 9
```

Salida esperada:

```text
Pais con mayor poblacion
Pais con menor poblacion
Promedio de poblacion
Promedio de superficie
Cantidad de paises por continente
```

## Participacion de los integrantes

Integrante 1: Henry Gabriel Ortiz
Tareas realizadas: desarrollo del codigo, armado del dataset CSV, pruebas funcionales, documentacion tecnica, README y preparacion de la demostracion.

Integrante 2: [COMPLETAR NOMBRE DEL INTEGRANTE]
Tareas realizadas: [COMPLETAR TAREAS REALIZADAS]

## Link al video demostrativo

[A ACTUALIZAR- ALEXIS]

## Link a la documentacion PDF

El archivo PDF se encuentra en la raiz del repositorio con el nombre:

```text
informe_TPI_paises.pdf
```

Link directo al PDF:

[A ACTUALIZAR A QUITAR - ALEXIS]

## Estado del proyecto
En proceso de actualización de repositorio.
Fase siguiente: Proyecto terminado y listo para entrega final.
