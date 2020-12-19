import sys

#turns a string into its initials
def get_initials(string):
    output = ''
    for i in string: #iterates over the characters in the string
        if i.isupper(): #adds the letter if it's uppercase
            output += i
    return output

initials = get_initials(sys.stdin.readline())
names = sys.stdin.readline()
conflicts = [] #the list of conflicts

for i in range(int(names)):
    name = sys.stdin.readline()
    if get_initials(name) == initials: #checks for conflicts
        conflicts.append(name)

if not conflicts: #if there are no conflicts
    conflicts.append('NONE')

#.join() lets you quickly print a list with the given separator
#all the names already have newlines at the end so we need no separator
print(''.join(conflicts)) 