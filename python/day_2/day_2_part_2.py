data = [line.strip() for line in open('input.txt').readlines()]
print(data)

def groupByLetters(input):
    countLetters={}
    for letter in input :
        countLetters[letter]=countLetters.get(letter,0)+1
    return countLetters

def isValidString(input):
    pass

def removeFrom(string,position):
    return string[:position]+string[position+1:]
