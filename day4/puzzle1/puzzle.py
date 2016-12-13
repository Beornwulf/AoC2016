# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

sector_sum = 0

def sort_characters(characters):
    characters = sorted(zip(characters.values(), characters.keys()), reverse=True)
    changed = True
    while changed:
        changed = False
        for index, i in enumerate(characters):
            (count, character) = i
            last_index = index - 1
            if (i > 0 and count == characters[last_index][0] and character < characters[last_index][1]):
                characters[index], characters[last_index] = characters[last_index], characters[index]
                changed = True
    return(characters)

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
    characters = sort_characters(characters)
    generated_hash = ''
    for i in range(5):
        generated_hash += characters[i][1]
    print(characters)
    print(generated_hash)
    if generated_hash == hash:
        sector_sum += sector

print(sector_sum)

