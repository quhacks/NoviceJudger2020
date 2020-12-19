import sys

ducks = sys.stdin.readline() #read the first number
coords = sys.stdin.readlines() #read the rest of the lines
minimum = 1e100 ##set the minimum impossibly high

#two loops lets us look at every pair of ducks
for i in range(int(ducks)):
    for j in range(int(ducks)):
        if i != j: #we don't want to compare a duck to itself!
            x1, y1 = coords[i].split()
            x2, y2 = coords[j].split()
            diff_x = abs(int(x1) - int(x2)) #horizontal distance
            diff_y = abs(int(y1) - int(y2)) #vertical distance
            diff = diff_x * diff_x + diff_y * diff_y #squared distance = squared difference in x + squared difference in y
            minimum = min(minimum, diff) #sets minimum to diff if it's lower

print(minimum)
print('YES' if minimum >= 36 else 'NO') #6 feet is 36 in squared distance