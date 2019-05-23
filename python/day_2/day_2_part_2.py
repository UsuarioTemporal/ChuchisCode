data = [line.strip() for line in open('input.txt').readlines()]
# print(data)

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

print(generateSublist())

# repetitions = list(map(isValidString,data))
# print(repetitions)