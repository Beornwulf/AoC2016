def move_left(position):
    return {
        1:1,
        2:1,
        3:2,
        4:4,
        5:4,
        6:5,
        7:7,
        8:7,
        9:8,
    }.get(position)

def move_up(position):
    return {
        1:1,
        2:2,
        3:3,
        4:1,
        5:2,
        6:3,
        7:4,
        8:5,
        9:6,
    }.get(position)

def move_right(position):
    return {
        1:2,
        2:3,
        3:3,
        4:5,
        5:6,
        6:7,
        7:8,
        8:8,
        9:9,
    }.get(position)
    
def move_down(position):
    return {
        1:4,
        2:5,
        3:6,
        4:7,
        5:8,
        6:9,
        7:7,
        8:8,
        9:9,
    }.get(position)

# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

position = 5

for line in input:
    for character in line:
        if character is 'L':
            position = move_left(position)
        if character is 'U':
            position = move_up(position)
        if character is 'R':
            position = move_right(position)
        if character is 'D':
            position = move_down(position)
    print(position)