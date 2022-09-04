# Importa el paquete argv
from sys import argv

# Declara las variables Script y filename pertenecientes al argv
script, filename = argv

# Abre el fichero indicado en los argumentos
txt = open(filename)

# Imprime el nombre del fichero
print(f"Here's your file {filename}:")
# Una vez abierto el fichero, lee el contenido del mismo y lo imprime
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

# Se repite lo anterior, abre fichero, lee fichero, imprime fichero.
txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()