frase_usuario = input("Escribe una frase de 10 palabras minimo: ")

numero_caracteres = len(frase_usuario)
print("Tu frase tiene", numero_caracteres, "caracteres")
numero_espacios = frase_usuario.count(" ")
print("Tu frase tiene", numero_espacios, "espacios")
numero_caracteres_sin_espacios = numero_caracteres - numero_espacios
print("Tu frase tiene", numero_caracteres_sin_espacios, "caracteres sin contar los espacios")

#Contar vocales en la frase
numero_vocales_a = frase_usuario.lower().count("a")
numero_vocales_e = frase_usuario.lower().count("e")
numero_vocales_i = frase_usuario.lower().count("i")
numero_vocales_o = frase_usuario.lower().count("o")
numero_vocales_u = frase_usuario.lower().count("u")

print("Tu frase tiene", numero_vocales_a, "vocales a")
print("Tu frase tiene", numero_vocales_e, "vocales e")
print("Tu frase tiene", numero_vocales_i, "vocales i")
print("Tu frase tiene", numero_vocales_o, "vocales o")
print("Tu frase tiene", numero_vocales_u, "vocales u")

#Numero total de palabras
numero_palabras = numero_espacios + 1
print("Tu frase tiene", numero_palabras, "palabras")

#eliminar primer palabra
primera_palabra = frase_usuario.split()[0]
frase_sin_primera_palabra = frase_usuario.replace(primera_palabra, "", 1).strip()
print("Tu frase sin la primera palabra es:", frase_sin_primera_palabra)

#reeplazar espacios por - 
frase_con_guiones = frase_usuario.replace(" ", "-")
print("Tu frase con guiones en lugar de espacios es:", frase_con_guiones)

#Minusculas a mayusculas y viceversa
vicecersa_frase = frase_usuario.swapcase()
print("Tu frase con mayusculas a minusculas y viceversa es:", vicecersa_frase)