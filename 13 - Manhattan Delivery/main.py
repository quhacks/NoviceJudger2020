import sys

freddy_x, freddy_y = sys.stdin.readline().split()
addresses = sys.stdin.readline()

for i in range(int(addresses)):
    x, y = sys.stdin.readline().split()
    diff_x = abs(int(freddy_x) - int(x)) #number of horizontal blocks
    diff_y = abs(int(freddy_y) - int(y)) #number of vertical blocks
    print(diff_x + diff_y) #manhattan distance = difference in x + difference in y