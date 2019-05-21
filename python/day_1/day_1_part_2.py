with open('input_2.txt','r') as file :
    # items = file.readlines()
    items = [int(line.strip()) for line in file]
# You notice that the device repeats the same frequency change list over
#  and over. To calibrate the device, you need to find the first frequency 
# it reaches twice.
# For example, using the same list of changes above, the device would loop
#  as follows:

#     Current frequency  0, change of +1; resulting frequency  1.
#     Current frequency  1, change of -2; resulting frequency -1.
#     Current frequency -1, change of +3; resulting frequency  2.
#     Current frequency  2, change of +1; resulting frequency  3.
#     (At this point, the device continues from the start of the list.)
#     Current frequency  3, change of +1; resulting frequency  4.
#     Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
def allFrequencies(items: list,start: int=0):
    frequency=start
    while True :
        for item in items :
            yield frequency
            frequency+=item
def findRepetition(items:list):
    noRepeat =set()
    for frequency in allFrequencies(items) :
        if frequency in noRepeat : return frequency
        noRepeat.add(frequency)
# findRepetition(items)
# print(sum(items))
print(findRepetition(items))