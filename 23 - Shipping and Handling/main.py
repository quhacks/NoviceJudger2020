import sys

items, capacity = sys.stdin.readline().split()
weights = sys.stdin.readlines()

#index - the item that was last placed on the truck
#weight - the current weight of the truck
def recursive(index, weight):
    if weight > int(capacity): 
        return 0 #don't run the function if the truck is overloaded

    maximum = weight #maximum weight that can be added to the truck
    for i in range(index + 1, len(weights)): #only looks at items after the last one to prevent duplicates
        #this function calls itself to find the maximum possible weight
        #that can be added to the current weight using only the remaining items
        maximum = max(maximum, recursive(i, weight + int(weights[i])))

    return maximum

#we call recursive(-1, 0) to indicate that the truck is empty
#it will return the maximum possible weight using all the items
print(recursive(-1, 0))