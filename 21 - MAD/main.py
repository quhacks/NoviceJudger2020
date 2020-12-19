import sys

#finds the average of the data
def avg(data):
    total = 0

    for i in data:
        total += int(i) #adds the value
    
    return total / len(data) #returns the average

#finds the mean absolute deviation of the data
def mad(data): 
    mean = avg(data)
    total = 0
    
    for i in data:
        total += abs(int(i) - mean) #adds the absolute difference
    
    return total / len(data) #returns the average difference

masks, judges = sys.stdin.readline().split()
avgs = [] #the mean of each mask's scores
mads = [] #the mean absolute deviation of each mask's scores

for i in range(int(masks)):
    scores = sys.stdin.readline().split()
    avgs.append(avg(scores)) #adds the avg
    mads.append(mad(scores)) #adds the mad

print(int(mad(avgs))) #the mad of the data as a whole
for i in mads:
    print(int(i)) #the mad of each mask's scores