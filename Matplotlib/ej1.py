import matplotlib.pyplot as plt

#1 Crea un gráfico de líneas simple usando Matplotlib
numeros = [10, 15, 7, 10, 22]

plt.plot(numeros)

#2 Modifica la apariencia de tu gráfico cambiando el color de fondo de la figura a verde.
fig = plt.figure(facecolor='green')
plt.plot(numeros)

#3 Genera un conjunto de 4 subgráficos (2 filas por 2 columnas). Asignalos a dos variables (fig y axs), para poder almacenar allí el gráfico.
graf = plt.subplots(2, 2)
plt.show()

