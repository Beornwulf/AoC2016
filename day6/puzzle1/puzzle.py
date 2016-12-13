# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

word_length = len(input[0])
password = ''

for index, i in enumerate(range(word_length)):
    characters = {}
    for line in input:
        character = line[index]
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    characters = sorted(zip(characters.values(), characters.keys()), reverse=True)
    password += characters[0][1]

print(password)

