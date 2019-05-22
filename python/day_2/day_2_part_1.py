# with open('input.txt','r') as file :
#     items = [line.strip() for line in file]
# print(items)
from functools import reduce
ids = [line.strip() for line in open('input.txt').readlines()]
# ids = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
def analyzeRepetitions(string)->dict:
    values = {}
    for letter in string :
        values[letter] = values.get(letter,0)+1
    return values

def isValid(input): 
    values = analyzeRepetitions(input)
    return (2 in values.values(),3 in values.values())

repetitions = list(map(isValid,ids))

boxesWith2 = reduce(lambda acc,tup: acc+1 if tup[0]==True else acc,repetitions,0)
boxesWith3 = reduce(lambda acc,tup:acc+1 if tup[-1]==True else acc,repetitions,0)
# print(repetitions)
print(boxesWith2*boxesWith3)
# print(analyzeRepetitions(ids))
# print(isValid(ids))