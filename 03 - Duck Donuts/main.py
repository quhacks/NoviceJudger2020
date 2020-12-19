import sys

lines = sys.stdin.readlines()
count = lines[0]              #first line
index = lines[int(count) + 1] #last line
donut = lines[int(index)]     #answer
print(donut)