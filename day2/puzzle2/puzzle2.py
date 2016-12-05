def move_left(position):
    return {
        '1':'1',
        '2':'2',
        '3':'2',
        '4':'3',
        '5':'5',
        '6':'5',
        '7':'6',
        '8':'7',
        '9':'8',
        'A':'A',
        'B':'A',
        'C':'B',
        'D':'D',
    }.get(position)

def move_up(position):
    return {
        '1':'1',
        '2':'2',
        '3':'1',
        '4':'4',
        '5':'5',
        '6':'2',
        '7':'3',
        '8':'4',
        '9':'9',
        'A':'6',
        'B':'7',
        'C':'8',
        'D':'B',
    }.get(position)

def move_right(position):
    return {
        '1':'1',
        '2':'3',
        '3':'4',
        '4':'4',
        '5':'6',
        '6':'7',
        '7':'8',
        '8':'9',
        '9':'9',
        'A':'B',
        'B':'C',
        'C':'C',
        'D':'D',
    }.get(position)
    
def move_down(position):
    return {
        '1':'3',
        '2':'6',
        '3':'7',
        '4':'8',
        '5':'5',
        '6':'A',
        '7':'B',
        '8':'C',
        '9':'9',
        'A':'A',
        'B':'D',
        'C':'C',
        'D':'D',
    }.get(position)

# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

position = '5'

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