import pandas as pd

libros = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 'El Principito']
})

autores = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 'J.K. Rowling']
})

cursos = pd.DataFrame({
    'curso_id': [101, 102, 103],
    'nombre_curso': ['Introducción a Python', 'Data Science con Python', 'Machine Learning Avanzado']
})

inscripciones = pd.DataFrame({
    'curso_id': [102, 102, 101, 104],
    'fecha_inscripcion': ['2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']
})

""" Objetivo: fusionar libros con autores para obtener un DataFrame que contenga toda la información disponible, asociando cada libro con su autor correspondiente. """

df_fusionado = pd.merge(libros, autores, on='ID') ## how=inner por defecto
##print(df_fusionado)

## con outer
df_outer = pd.merge(libros, autores, on='ID', how='outer', indicator=True)


""" Tu tarea es fusionar cursos con inscripciones (en un DataFrame llamado: cursos_inscripciones) de tal manera que el resultado final incluya todos los registros de inscripciones, completándolos con la información disponible en cursos.

Utiliza el método de fusión adecuado para garantizar que no se pierda ninguna inscripción, incluso si el curso correspondiente no está listado en el DataFrame cursos. Es importante que el DataFrame resultante cursos_inscripciones muestre claramente qué inscripciones no tienen un curso correspondiente, rellenando esos espacios con NaN. """

cursos_inscripciones = pd.merge(inscripciones, cursos, on='curso_id', how='left')
print(cursos_inscripciones)