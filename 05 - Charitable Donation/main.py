import sys

friends = sys.stdin.readline() #reads the number of friends
answer, minimum = sys.stdin.readline().split() #reads the first friend

for i in range(int(friends) - 1): #loops over the rest of the friends
    name, masks = sys.stdin.readline().split() #reads the friend data
    if int(masks) < int(minimum): #compare their masks to the minimum
        answer = name #if they have less,
        minimum = masks #then they're the new minimum
print(answer)