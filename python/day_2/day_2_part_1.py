# with open('input.txt','r') as file :
#     items = [line.strip() for line in file]
# print(items)

ids = [line.strip() for line in open('input.txt').readlines()]
ids = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
def analyzeRepetitions(string)->dict:
    values = {}
    for letter in string :
        values[letter] = values.get(letter,0)+1
    return values

def isValid(input): 
    values = analyzeRepetitions(input)
    return (2 in values.values(),3 in values.values())

repetitions = list(map(isValid,ids))
print(repetitions)
# print(analyzeRepetitions(ids))
# print(isValid(ids))