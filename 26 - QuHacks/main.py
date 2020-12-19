import sys

machines, tests = sys.stdin.readline().split()
times = sys.stdin.readlines()
last = [0] * int(machines) #the time each machine is working until

for i in range(int(tests)): #schedule each test, one by one
    minimum = last[0] + int(times[0]) #the earliest time this test can be finished
    mindex = 0 #the index of the machine that can finish this test earliest
    
    for j in range(1, len(last)): #loops over all the machines
        if last[j] + int(times[j]) < minimum: #checks if this one can finish the test earlier
            minimum = last[j] + int(times[j])
            mindex = j

    last[mindex] = minimum #schedules the test to the machine which can finish it earliest

print(max(last)) #the total time taken is the the time the last machine takes