# with open('input.txt','r') as file :
#     items = [line.strip() for line in file]
# print(items)

ids = [line.strip() for line in open('input.txt').readlines()]

def analyzeRepetitions(string)->dict:
    values = {}
    for letter in string :
        values[letter] = values.get(letter,0)+1
    return values

print(analyzeRepetitions(ids))