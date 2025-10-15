nombre = "Jhon"
apellido = "Doe"
full_name = nombre + " " + apellido

fecha = "2024-10-01"

bienvenida = f"Hola, {full_name}. Hoy es {fecha}."

dolares = 210.0

euros_para_recibir = dolares * 0.88

""" La maquina solo da billetes de 10, 1 y monedas """

billetes_10 = (euros_para_recibir // 10)
billetes_1 = (euros_para_recibir - (billetes_10 * 10)) // 1
monedas = euros_para_recibir % 1


print(bienvenida)
print(f"Dolares a convertir: {dolares}")
print(f"Euros a recibir: {euros_para_recibir:.2f}")
print(f"Billetes de 10: {billetes_10}, Billetes de 1: {billetes_1}, Monedas: {monedas:.2f}")