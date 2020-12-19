import sys

meetings = sys.stdin.readline()
times = [] #holds both the start and end times

#adds all the values to the times list
for i in range(int(meetings)):
    start, length = sys.stdin.readline().split()
    times.append(int(start))
    times.append(int(start) + int(length)) #end = start + length

times.sort() #important because the meetings can come out of order

maximum = 0
for i in range(1, len(times) - 1, 2): #loops with an interval of 2 (all odd numbers)
    end = times[i] #all end times are at odd indices
    start = times[i + 1] #the start of the next meeting is the next item
    maximum = max(maximum, start - end) #break = start of next - end of current

print(maximum)