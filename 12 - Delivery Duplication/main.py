import sys

length = sys.stdin.readline()
old = [] #the addresses from last week
for i in range(int(length)):
    old.append(sys.stdin.readline())

length = sys.stdin.readline()
new = [] #the addresses from this week
for i in range(int(length)):
    new.append(sys.stdin.readline())

duplicates = [] #the duplicate addresses
for i in old: #loops over the old address list
    if i in new: #and checks if they're in the new list
        duplicates.append(i) #if so, they're duplicated

if not duplicates: #if there are no duplicates
    duplicates.append('NONE')

print(''.join(duplicates))
