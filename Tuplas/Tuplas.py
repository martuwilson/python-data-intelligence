# =============================================================================
# MINI GUÍA: TUPLAS EN PYTHON 🔥
# =============================================================================

"""
¿QUÉ SON LAS TUPLAS?
Las tuplas son estructuras de datos ordenadas e INMUTABLES (no se pueden modificar)
que pueden contener elementos de diferentes tipos.
Se definen con paréntesis () y elementos separados por comas.
"""

# =============================================================================
# 1. CREACIÓN DE TUPLAS
# =============================================================================

# Tupla básica
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla básica:", mi_tupla)

# Tupla con diferentes tipos de datos
tupla_mixta = (1, "Hola", 3.14, True)
print("Tupla mixta:", tupla_mixta)

# Tupla sin paréntesis (también válido)
coordenadas = 10, 20
print("Coordenadas:", coordenadas)

# Tupla de un solo elemento (necesita coma)
tupla_uno = (42,)  # Sin la coma sería solo un número en paréntesis
print("Tupla de un elemento:", tupla_uno)

# Tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

print("\n" + "="*50 + "\n")

# =============================================================================
# 2. ACCESO A ELEMENTOS (INDEXACIÓN)
# =============================================================================

ciudades = ("Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao")

# Acceso por índice (empezando en 0)
print("Primera ciudad:", ciudades[0])
print("Última ciudad:", ciudades[-1])
print("Segunda ciudad:", ciudades[1])

# Slicing (rebanadas)
print("Primeras 3 ciudades:", ciudades[:3])
print("Últimas 2 ciudades:", ciudades[-2:])
print("Ciudades del 1 al 3:", ciudades[1:4])

print("\n" + "="*50 + "\n")

# =============================================================================
# 3. OPERACIONES BÁSICAS
# =============================================================================

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenación
concatenada = tupla1 + tupla2
print("Tuplas concatenadas:", concatenada)

# Repetición
repetida = tupla1 * 3
print("Tupla repetida 3 veces:", repetida)

# Verificar si un elemento está en la tupla
print("¿Está el 2 en tupla1?:", 2 in tupla1)
print("¿Está el 7 en tupla1?:", 7 in tupla1)

# Longitud de la tupla
print("Longitud de la tupla1:", len(tupla1))

print("\n" + "="*50 + "\n")

# =============================================================================
# 4. MÉTODOS PRINCIPALES DE LAS TUPLAS
# =============================================================================

numeros = (1, 2, 3, 2, 4, 2, 5)

# count() - Cuenta las ocurrencias de un elemento
print(f"El número 2 aparece {numeros.count(2)} veces")
print(f"El número 5 aparece {numeros.count(5)} veces")

# index() - Encuentra el índice de la primera ocurrencia
print(f"El primer 2 está en el índice: {numeros.index(2)}")
print(f"El número 4 está en el índice: {numeros.index(4)}")

# Intentar buscar un elemento que no existe causaría error
# print(numeros.index(10))  # Esto daría ValueError

print("\n" + "="*50 + "\n")

# =============================================================================
# 5. DESEMPAQUETADO DE TUPLAS (UNPACKING)
# =============================================================================

# Asignar valores de una tupla a variables individuales
persona = ("Juan", 25, "Ingeniero")
nombre, edad, profesion = persona

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Profesión: {profesion}")

# Desempaquetado con *
numeros_var = (1, 2, 3, 4, 5, 6)
primero, segundo, *resto, ultimo = numeros_var

print(f"Primero: {primero}")
print(f"Segundo: {segundo}")
print(f"Resto: {resto}")
print(f"Último: {ultimo}")

print("\n" + "="*50 + "\n")

# =============================================================================
# 6. TUPLAS ANIDADAS
# =============================================================================

# Tupla que contiene otras tuplas
estudiantes = (
    ("Ana", 20, "Matemáticas"),
    ("Carlos", 22, "Física"),
    ("María", 21, "Química")
)

print("Estudiantes:")
for estudiante in estudiantes:
    nombre, edad, carrera = estudiante
    print(f"  {nombre}, {edad} años, estudia {carrera}")

# Acceso a elementos de tuplas anidadas
print(f"\nPrimer estudiante: {estudiantes[0]}")
print(f"Nombre del primer estudiante: {estudiantes[0][0]}")

print("\n" + "="*50 + "\n")

# =============================================================================
# 7. CONVERSIONES
# =============================================================================

# Lista a tupla
lista = [1, 2, 3, 4, 5]
tupla_desde_lista = tuple(lista)
print("Lista convertida a tupla:", tupla_desde_lista)

# Tupla a lista
tupla_original = (6, 7, 8, 9, 10)
lista_desde_tupla = list(tupla_original)
print("Tupla convertida a lista:", lista_desde_tupla)

# String a tupla
texto = "Python"
tupla_desde_string = tuple(texto)
print("String convertido a tupla:", tupla_desde_string)

print("\n" + "="*50 + "\n")

# =============================================================================
# 8. COMPARACIÓN: TUPLAS vs LISTAS
# =============================================================================

"""
TUPLAS:
✅ Inmutables (no se pueden modificar)
✅ Más rápidas para acceder
✅ Pueden ser claves en diccionarios
✅ Ideales para datos que no cambian
✅ Usan menos memoria

LISTAS:
✅ Mutables (se pueden modificar)
✅ Tienen más métodos disponibles
✅ Ideales para colecciones que cambian
❌ Usan más memoria
❌ No pueden ser claves en diccionarios
"""

# Ejemplo de inmutabilidad
mi_tupla_inmutable = (1, 2, 3)
# mi_tupla_inmutable[0] = 10  # Esto causaría TypeError

mi_lista_mutable = [1, 2, 3]
mi_lista_mutable[0] = 10  # Esto sí funciona
print("Lista modificada:", mi_lista_mutable)

print("\n" + "="*50 + "\n")

# =============================================================================
# 9. CASOS DE USO COMUNES
# =============================================================================

# 1. Coordenadas
punto_2d = (10, 20)
punto_3d = (10, 20, 30)
print(f"Punto 2D: {punto_2d}")
print(f"Punto 3D: {punto_3d}")

# 2. Datos de configuración
config = ("localhost", 8080, "admin", "password")
servidor, puerto, usuario, contraseña = config
print(f"Servidor: {servidor}:{puerto}")

# 3. Retorno múltiple de funciones
def obtener_datos_persona():
    return "Juan", 25, "juan@email.com"

nombre, edad, email = obtener_datos_persona()
print(f"Datos: {nombre}, {edad}, {email}")

# 4. Como claves de diccionarios
coordenadas_ciudades = {
    (40.4168, -3.7038): "Madrid",
    (41.3851, 2.1734): "Barcelona",
    (39.4699, -0.3763): "Valencia"
}

print("\nCiudades por coordenadas:")
for coordenada, ciudad in coordenadas_ciudades.items():
    print(f"  {coordenada} -> {ciudad}")

print("\n" + "="*50 + "\n")

# =============================================================================
# 10. FUNCIONES ÚTILES CON TUPLAS
# =============================================================================

numeros_tupla = (5, 2, 8, 1, 9, 3)

print("Tupla original:", numeros_tupla)
print("Máximo:", max(numeros_tupla))
print("Mínimo:", min(numeros_tupla))
print("Suma:", sum(numeros_tupla))
print("Tupla ordenada:", tuple(sorted(numeros_tupla)))
print("Tupla invertida:", tuple(reversed(numeros_tupla)))

# Enumerar tupla
print("\nElementos con índice:")
for indice, valor in enumerate(numeros_tupla):
    print(f"  Índice {indice}: {valor}")

print("\n" + "="*80)
print("🎉 ¡GUÍA COMPLETA DE TUPLAS FINALIZADA! 🎉")
print("="*80)
