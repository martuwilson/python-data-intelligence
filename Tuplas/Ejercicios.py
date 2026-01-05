# =============================================================================
# EJERCICIOS PRÁCTICOS: TUPLAS EN PYTHON 💪
# =============================================================================

print("="*60)
print("🔥 EJERCICIOS PRÁCTICOS DE TUPLAS 🔥")
print("="*60)

# =============================================================================
# EJERCICIO 1: Información de productos
# =============================================================================

print("\n📦 EJERCICIO 1: Catálogo de productos")
print("-" * 40)

# Crear tuplas con información de productos (nombre, precio, stock)
producto1 = ("Laptop", 999.99, 15)
producto2 = ("Mouse", 25.50, 100)
producto3 = ("Teclado", 75.00, 45)

# Desempaquetar y mostrar información
nombre1, precio1, stock1 = producto1
print(f"Producto: {nombre1}")
print(f"Precio: ${precio1}")
print(f"Stock: {stock1} unidades")

# =============================================================================
# EJERCICIO 2: Coordenadas geográficas
# =============================================================================

print("\n🌍 EJERCICIO 2: Sistema de coordenadas")
print("-" * 40)

# Tuplas con coordenadas de ciudades importantes
ciudades_coordenadas = (
    ("Madrid", 40.4168, -3.7038),
    ("París", 48.8566, 2.3522),
    ("Londres", 51.5074, -0.1278),
    ("Nueva York", 40.7128, -74.0060),
    ("Tokio", 35.6762, 139.6503)
)

print("Ciudades y sus coordenadas:")
for ciudad, lat, lon in ciudades_coordenadas:
    print(f"  {ciudad}: Lat {lat}°, Lon {lon}°")

# Encontrar la ciudad más al norte (mayor latitud)
ciudad_norte = max(ciudades_coordenadas, key=lambda x: x[1])
print(f"\nCiudad más al norte: {ciudad_norte[0]} ({ciudad_norte[1]}°)")

# =============================================================================
# EJERCICIO 3: Estadísticas de estudiantes
# =============================================================================

print("\n🎓 EJERCICIO 3: Calificaciones de estudiantes")
print("-" * 40)

estudiantes = (
    ("Ana", (85, 92, 78, 95)),
    ("Carlos", (76, 84, 91, 73)),
    ("María", (94, 89, 96, 92)),
    ("Pedro", (82, 78, 85, 88))
)

print("Promedios de estudiantes:")
for nombre, calificaciones in estudiantes:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"  {nombre}: {promedio:.1f}")

# Encontrar al mejor estudiante
mejor_estudiante = max(estudiantes, 
                      key=lambda x: sum(x[1]) / len(x[1]))
mejor_promedio = sum(mejor_estudiante[1]) / len(mejor_estudiante[1])
print(f"\nMejor estudiante: {mejor_estudiante[0]} con promedio {mejor_promedio:.1f}")

# =============================================================================
# EJERCICIO 4: Sistema de colores RGB
# =============================================================================

print("\n🎨 EJERCICIO 4: Paleta de colores RGB")
print("-" * 40)

# Tuplas representando colores RGB
colores = (
    ("Rojo", (255, 0, 0)),
    ("Verde", (0, 255, 0)),
    ("Azul", (0, 0, 255)),
    ("Amarillo", (255, 255, 0)),
    ("Magenta", (255, 0, 255)),
    ("Cian", (0, 255, 255)),
    ("Blanco", (255, 255, 255)),
    ("Negro", (0, 0, 0))
)

print("Paleta de colores:")
for nombre, (r, g, b) in colores:
    print(f"  {nombre}: RGB({r}, {g}, {b})")

# Calcular intensidad promedio de cada color
print("\nIntensidad promedio de colores:")
for nombre, rgb in colores:
    intensidad = sum(rgb) / 3
    print(f"  {nombre}: {intensidad:.1f}")

# =============================================================================
# EJERCICIO 5: Inventario de biblioteca
# =============================================================================

print("\n📚 EJERCICIO 5: Inventario de biblioteca")
print("-" * 40)

# Tupla con información de libros (título, autor, año, disponible)
biblioteca = (
    ("1984", "George Orwell", 1949, True),
    ("El Quijote", "Miguel de Cervantes", 1605, False),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, True),
    ("El principito", "Antoine de Saint-Exupéry", 1943, True),
    ("Orgullo y prejuicio", "Jane Austen", 1813, False)
)

# Mostrar libros disponibles
print("📖 Libros disponibles:")
libros_disponibles = tuple(libro for libro in biblioteca if libro[3])
for titulo, autor, año, _ in libros_disponibles:
    print(f"  • '{titulo}' por {autor} ({año})")

# Contar libros por siglo
siglo_20 = sum(1 for libro in biblioteca if 1900 <= libro[2] < 2000)
siglo_19 = sum(1 for libro in biblioteca if 1800 <= libro[2] < 1900)
siglo_17 = sum(1 for libro in biblioteca if 1600 <= libro[2] < 1700)

print(f"\n📊 Distribución por siglos:")
print(f"  Siglo XVII: {siglo_17} libros")
print(f"  Siglo XIX: {siglo_19} libros")
print(f"  Siglo XX: {siglo_20} libros")

# =============================================================================
# EJERCICIO 6: Menú de restaurante
# =============================================================================

print("\n🍽️ EJERCICIO 6: Menú del restaurante")
print("-" * 40)

# Tupla con platos (nombre, precio, categoría, vegetariano)
menu = (
    ("Pizza Margherita", 12.50, "Principal", True),
    ("Ensalada César", 8.75, "Entrada", False),
    ("Pasta Carbonara", 14.00, "Principal", False),
    ("Sopa de Verduras", 6.50, "Entrada", True),
    ("Tiramisu", 5.25, "Postre", True),
    ("Salmón Grillado", 18.90, "Principal", False),
    ("Helado de Vainilla", 4.00, "Postre", True)
)

# Mostrar menú por categorías
categorias = ("Entrada", "Principal", "Postre")

for categoria in categorias:
    print(f"\n🍴 {categoria.upper()}S:")
    platos_categoria = tuple(plato for plato in menu if plato[2] == categoria)
    for nombre, precio, _, vegetariano in platos_categoria:
        veggie_icon = "🌱" if vegetariano else "🥩"
        print(f"  {veggie_icon} {nombre}: €{precio}")

# Calcular precio promedio
precio_promedio = sum(plato[1] for plato in menu) / len(menu)
print(f"\n💰 Precio promedio: €{precio_promedio:.2f}")

# Opciones vegetarianas
opciones_vegetarianas = tuple(plato for plato in menu if plato[3])
print(f"\n🌱 Opciones vegetarianas disponibles: {len(opciones_vegetarianas)}")

# =============================================================================
# EJERCICIO 7: Sistema de versiones de software
# =============================================================================

print("\n💻 EJERCICIO 7: Historial de versiones")
print("-" * 40)

# Tupla con versiones (número, fecha, características)
versiones = (
    ((1, 0, 0), "2023-01-15", ("Lanzamiento inicial", "Interface básica")),
    ((1, 1, 0), "2023-03-20", ("Nuevas funciones", "Corrección de bugs")),
    ((1, 2, 0), "2023-06-10", ("Mejoras de rendimiento", "Nueva API")),
    ((2, 0, 0), "2023-09-05", ("Rediseño completo", "Nuevas características")),
    ((2, 1, 0), "2023-11-18", ("Optimizaciones", "Soporte móvil"))
)

print("📋 Historial de versiones:")
for (mayor, menor, parche), fecha, caracteristicas in versiones:
    print(f"\n  Versión {mayor}.{menor}.{parche} - {fecha}")
    for caracteristica in caracteristicas:
        print(f"    • {caracteristica}")

# Última versión
ultima_version = versiones[-1]
print(f"\n🚀 Versión actual: {ultima_version[0][0]}.{ultima_version[0][1]}.{ultima_version[0][2]}")

# =============================================================================
# EJERCICIO 8: Análisis de datos meteorológicos
# =============================================================================

print("\n🌡️ EJERCICIO 8: Datos meteorológicos semanales")
print("-" * 40)

# Tupla con datos diarios (día, temperatura_min, temperatura_max, lluvia_mm)
semana_meteorologica = (
    ("Lunes", 15, 22, 0),
    ("Martes", 18, 25, 2),
    ("Miércoles", 16, 21, 8),
    ("Jueves", 14, 19, 15),
    ("Viernes", 12, 18, 5),
    ("Sábado", 11, 17, 0),
    ("Domingo", 13, 20, 0)
)

print("🌤️ Pronóstico de la semana:")
for dia, temp_min, temp_max, lluvia in semana_meteorologica:
    lluvia_txt = f"🌧️ {lluvia}mm" if lluvia > 0 else "☀️ Sin lluvia"
    print(f"  {dia}: {temp_min}°C - {temp_max}°C, {lluvia_txt}")

# Estadísticas
temperaturas_min = tuple(dia[1] for dia in semana_meteorologica)
temperaturas_max = tuple(dia[2] for dia in semana_meteorologica)
total_lluvia = sum(dia[3] for dia in semana_meteorologica)

print(f"\n📊 Estadísticas semanales:")
print(f"  Temperatura mínima: {min(temperaturas_min)}°C")
print(f"  Temperatura máxima: {max(temperaturas_max)}°C")
print(f"  Total de lluvia: {total_lluvia}mm")
print(f"  Días con lluvia: {sum(1 for dia in semana_meteorologica if dia[3] > 0)}")

print("\n" + "="*80)
print("🎉 ¡TODOS LOS EJERCICIOS COMPLETADOS! 🎉")
print("="*80)