import sys

items = sys.stdin.readline() 
maximum = 100000 #set the minimum impossibly high
factors = [] #the list of limiting factors

for i in range(int(items)): #loops over the items
    stock, needed = sys.stdin.readline().split() 
    masks = int(stock) // int(needed) #the operator // divides and rounds down
    if masks < maximum: #compare the masks this item makes to the current maximum
        factors.clear() #if this item makes less masks, the other items are not limiting factors
        maximum = masks #set the new maximum
    if masks <= maximum: #this code will run even if the first if statement runs
        factors.append(i) #add this item to the limiting factors list

print(maximum)
for i in factors: #print every limiting factor
    print(i)