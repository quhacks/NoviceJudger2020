import sys

#add an extra january to account for the new year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31]

month, day = sys.stdin.readline().split()
month_index = months.index(month) #.index() finds the position in the list
meetings = sys.stdin.readline()
missed = 0

for i in range(int(meetings)):
    meeting_month, meeting_day = sys.stdin.readline().split()
    
    #if the dates fall on the same month
    if meeting_month == month:
        #check if the meeting day is in the next 14-day interval
        if int(day) <= int(meeting_day) < int(day) + 14:
            missed += 1

    #if the meeting date is next month 
    if meeting_month == months[month_index + 1]:
        #add all the days of this month before comparing
        if int(day) <= days[month_index] + int(meeting_day) < int(day) + 14:
            missed += 1

print(missed)