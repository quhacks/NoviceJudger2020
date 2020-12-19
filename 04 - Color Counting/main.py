import sys

#reads the first line and uses .split() to get multiple numbers
colors, needed = sys.stdin.readline().split() 

count = 0
for i in range(int(colors)): #loops over every color
    color = sys.stdin.readline() #reads the next line
    if int(color) >= int(needed): #checks if there's enough fabric
        count += 1 #adds one to count if there is
print(count)