# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

possible_triangles = 0
trios = []
triangles = [range(3) for x in range(3)]

for i in range(0, len(input), 3):
    trio = input[i:i+3]
    trios.append(trio)

for trio in trios:
    for index_j, line in enumerate(trio):
        line = line.split()
        triangles[0][index_j] = int(line[0])
        triangles[1][index_j] = int(line[1])
        triangles[2][index_j] = int(line[2])
    for triangle in triangles:
        triangle = sorted(triangle)
        if (triangle[0] + triangle[1]) > triangle[2]:
            possible_triangles += 1
    
print(possible_triangles)