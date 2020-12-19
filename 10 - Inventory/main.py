import sys

tables = sys.stdin.readline()
total = 0 #the total sum
sums = [] #the sum of each table

for i in range(int(tables)):
    boxes = sys.stdin.readline()
    masks = 0 #the number of masks on this table
    
    for j in sys.stdin.readline().split(): #iterates over every number on the line
        masks += int(j)
    
    total += masks #adds to the total
    sums.append(masks) #and stores the amount on this table

print(total)
for i in sums: #print every sum
    print(i)