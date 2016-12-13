from string import ascii_lowercase

# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

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
    coded_name = ' '.join(words)
    room_name = ''
    for character in coded_name:
        if character is ' ':
            room_name += character
        else:
            character_index = ascii_lowercase.index(character)
            new_character_index = (character_index + sector) % 26
            new_character = ascii_lowercase[new_character_index]
            room_name += new_character
    if 'north' in room_name:
        print(room_name, str(sector))
