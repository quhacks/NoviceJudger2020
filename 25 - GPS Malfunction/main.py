import sys

intersections, roads = sys.stdin.readline().split()
connections = sys.stdin.readlines()
distances = [None] * int(intersections) #holds the distance to each intersection
distances[0] = 0 #Freddy is 0 minutes from his starting position

#we check all the roads multiple times to account for indirect connections
for i in range(int(roads)):
    for j in connections:
        a, b = j.split()

        #if a is reachable and b is not, set b
        if distances[int(a)] == i and distances[int(b)] == None:
            distances[int(b)] = i + 1
        
        #if b is reachable and a is not, set b
        if distances[int(b)] == i and distances[int(a)] == None:
            distances[int(a)] = i + 1

print(distances[-1]) #return the distance to the last intersection