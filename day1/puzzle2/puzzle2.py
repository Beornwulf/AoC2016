def turn_right(direction):
    return {
        'north': 'east',
        'east': 'south',
        'south': 'west',
        'west': 'north'
    }.get(direction)

def turn_left(direction):
    return {
        'north': 'west',
        'west': 'south',
        'south': 'east',
        'east': 'north'
    }.get(direction)

def travel(direction, distance):
    global x, y, logs, duplicate_logs
    for i in range(distance):
        if direction is 'north':
            y += 1
        elif direction is 'east':
            x += 1
        elif direction is 'south':
            y -= 1
        elif direction is 'west':
            x -= 1
        location = (x,y)
        if location in logs:
            duplicate_logs.append(location)
        else:
            logs.append(location)
        
    
input = "R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3"

input = input.split(", ")

logs = []
duplicate_logs = []

direction = 'north'

x = 0
y = 0

for i in input:
    turn = i[0]
    distance = int(i[1:])
    if turn is "R":
        direction = turn_right(direction)
    elif turn is "L":
        direction = turn_left(direction)
    travel(direction, distance)

print("Total distance: %d" % (abs(x)+abs(y)))

first_duplicate = duplicate_logs[0]
first_duplicate_distance = (abs(first_duplicate[0])+abs(first_duplicate[1]))

print("First duplicated location: %s, %d away" % (first_duplicate, first_duplicate_distance))
            
            
