data = [line.strip() for line in open('input.txt').readlines()]
# print(data)
#El problema radica en que teemos que demostrar cual es la cadena que solo se diferencian en una letra
# y mostrar la cadena restante
# Ejm fghij y fguij solo se diferencian en h y u en la tercera posicion(2) entonces la cadena a mostrar será fgij
#

# data =[
#     'abcde',
#     'fghij',
#     'klmno',
#     'pqrst',
#     'fguij',
#     'axcye',
#     'wvxyz'
# ]
def groupByLetters(input):
    countLetters={}
    for letter in input :
        countLetters[letter]=countLetters.get(letter,0)+1
    return countLetters

def isValidString(input):
    items = groupByLetters(input)
    return (2 in items.values(),3 in items.values())


def removeFrom(string,position):
    return string[:position]+string[position+1:]

def generateSublist(_list:list,index:int)->list:
    return list(map(lambda str:removeFrom(str,index),_list))

for index in range(len(data[0])):
    subListInput = generateSublist(data,index)
    if len(set(subListInput))==len(data) : continue
    # print(subListInput)
    # break
    for key,value in groupByLetters(subListInput).items():
        if value==2 : 
            print(key)
            break
        
    break

# print(generateSublist(data,0))

# repetitions = list(map(isValidString,data))
# print(repetitions)