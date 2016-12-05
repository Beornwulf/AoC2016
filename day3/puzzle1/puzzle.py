# Open the input file and dump the contents into a variable
inputfile = open("input.txt", "r")
input = inputfile.read()
inputfile.close()

input = input.splitlines()

possible_triangles = 0

for line in input:
    sides = line.split()
    sides = [int(i) for i in sides]
    triangle = sorted(sides)
    print(triangle)
    if (triangle[0] + triangle[1]) > triangle[2]:
        possible_triangles += 1
    
print(possible_triangles)