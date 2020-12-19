import sys

days = sys.stdin.readline()
total = 0

for i in range(int(days)):
    total += int(sys.stdin.readline()) #adds every day's revenue to the total
    print(total) #prints the total after each day