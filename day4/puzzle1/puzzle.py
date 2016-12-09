# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

sector_sum = 0

def sort_characters(characters):
    

for line in input:
    words = line.split('-')
    sector_and_hash = words.pop(-1)
    sector_and_hash = sector_and_hash.split('[')
    sector = int(sector_and_hash[0])
    hash = sector_and_hash[1].split(']')
    hash = hash[0]
    words = ''.join(words)
    characters = {}
    for character in words:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    print(characters)
    
print(sector_sum)

