# Calibrar el dispositivo
# archivo = open('input.txt','r')
# print(archivo.read())
# archivo.close()

archive = open('input.txt','r')
items = archive.readlines()
def make(items):
    for line in items: 
        while True :
            yield line
archive.close()