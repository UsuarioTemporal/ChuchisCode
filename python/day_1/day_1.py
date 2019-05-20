# Calibrar el dispositivo
# archivo = open('input.txt','r')
# print(archivo.read())
# archivo.close()

archive = open('input.txt','r')
for line in archive.readlines(): 
    print(int(line))
archive.close()