# Calibrar el dispositivo
# archivo = open('input.txt','r')
# print(archivo.read())
# archivo.close()

archive = open('input.txt','r')
items = archive.readlines()

"""
    with open('ruta') as file :
        items = [int(line.strip()) for in file)]
"""

def correctAllFrequences():
    for line in items:
        yield line

ob = correctAllFrequences()

try:
    frecuency = 0
    while True:
        frecuency+=int(next(ob))
except Exception:
    pass
finally:
    print(frecuency)
    archive.close()