def turnRight(direction):
    return {
        'north': 'east',
        'east': 'south',
        'south': 'west',
        'west': 'north'
    }.get(direction)

def turnLeft(direction):
    return {
        'north': 'west',
        'west': 'south',
        'south': 'east',
        'east': 'north'
    }.get(direction)

def travel(direction, distance):
    global x, y
    if direction is 'north':
        y += distance
    elif direction is 'east':
        x += distance
    elif direction is 'south':
        y -= distance
    elif direction is 'west':
        x -= distance
        
    
input = "R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3"

input = input.split(", ")

direction = 'north'

x = 0
y = 0

for i in input:
    print(i)
    for j in i:
        if j is "R":
            print("Turning right")
            direction = turnRight(direction)
            print("Facing %s" % direction)
        elif j is "L":
            print("Turning left")
            direction = turnLeft(direction)
            print("Facing %s" % direction)
        else:
            print("Travelling %s" % j)
            travel(direction, int(j))
            print("Now at %d,%d" % (x, y))

print("Total distance: %d" % (abs(x)+abs(y)))
            
            
