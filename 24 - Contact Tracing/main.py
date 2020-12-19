import sys

count = sys.stdin.readline()
contacts = sys.stdin.readlines()
needs_test = {'0'} #this is a set, which is a list that doesn't allow duplicates
tests = 1 #Freddy needs a test

#we check all the contacts multiple times to account for indirect contacts
for i in range(int(count)):
    for j in contacts:
        a, b = j.split()

        #if one needs a test, both need a test
        if a in needs_test or b in needs_test:
            #adding to a set has no effect if the item is already present
            needs_test.add(a)
            needs_test.add(b)

print(len(needs_test)) #count the number of people who need tests