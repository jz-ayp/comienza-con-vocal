"""
Comienza con vocal
"""

# Declaraciones
VOCALES = "aeiouáéíóúü"

# Entradas
palabra = input("Escriba una palabra: ")

# Proceso
if len(palabra) > 0 and palabra[0].lower() in VOCALES:
    comienza = "comienza"
else:
    comienza = "no comienza"
respuesta = "'" + palabra + "' " + comienza + " con vocal"

# Salidas
print(respuesta)
